from math import sin, cos, radians, atan, sqrt, degrees


class Projectile:
    def __init__(self, vel=0, angle=0, height=0):
        self.angle = angle
        self.vel = vel
        self.height = height
        self.equations = {}
        self.make_equations()

        self.values = {"impact": {}, "maxheight": {}}

    def make_equations(self):
        self.equations["velx"] = self.vel * cos(radians(self.angle))
        self.equations["vely"] = lambda x: -32 * x + self.vel * sin(radians(self.angle))

        self.equations["distx"] = lambda x: self.vel * x * cos(radians(self.angle))
        self.equations["disty"] = (
            lambda x: -16 * x ** 2
            + self.vel * x * sin(radians(self.angle))
            + self.height
        )

    def set_values(self, cat, **kwargs):
        self.values[cat] = kwargs

    def plug(self, which: str, x):
        return self.equations[which](x)

    def impact(self, h=0):
        if not self.values["impact"]:
            t = self.quadratic(
                -16, self.vel * sin(radians(self.angle)), self.height - h
            )
            vy = self.plug("vely", t)
            vx = self.equations["velx"]
            v = sqrt(vy ** 2 + vx ** 2)
            angle = degrees(atan(vy / vx))
            self.set_values("impact", v=v, t=t, h=h, angle=angle)
        return self.values["impact"]

    def max_height(self):
        if not self.values["maxheight"]:
            t = self.vel * sin(radians(self.angle)) / 32
            h = self.plug("disty", t)
            self.set_values("maxheight", v=0, t=t, h=h)
        return self.values["maxheight"]

    @staticmethod
    def quadratic(a, b, c):
        d = (b ** 2) - (4 * a * c)
        sol1 = (-b - sqrt(d)) / (2 * a)
        sol2 = (-b + sqrt(d)) / (2 * a)
        return max(sol1, sol2)

    def full_calculate(self):
        self.max_height()
        self.impact()

    def approach_problem(self, approach, endHeight=0, oncoming=True):
        self.impact(h=endHeight)
        t = self.values.get("impact").get("t")
        print("Time:", t)
        if oncoming:
            print("Distance:", self.plug("distx", t) + abs(approach) * t)
        else:
            print("Distance:", self.plug("distx", t) + abs(approach) * -t)

    def get_equation(self, which: str):
        return self.equations[which]

    # def run_accessor(self):
    #     self.full_calculate()
    #     ans = True
    #     yeahno = {"y": True, "n": False}
    #     while ans:
    #         opt = self.option_print(list(self.values.keys()))
    #         data = self.option_print(list(self.values.get(opt).keys()))
    #         print(self.values.get(opt).get(data))
    #         ans = yeahno.get(input("\nRun again (y/n): ")[0].lower())

    # @staticmethod
    # def option_print(dataset: list):
    #     print("\nOptions")
    #     print("-" * 10)
    #     print(*dataset, sep="\n")
    #     print("-" * 10)
    #     return input("Enter choice: ")


# approach_problem(600, 25, 44, oncoming=True)

# p = Projectile(vel=600, angle=25, height=0)
# p.approach_problem(44, endHeight=300)

p = Projectile(vel=100, angle=40, height=200)
p.full_calculate()
t = p.values.get("impact").get("t")
print(t)
print(p.plug("distx", t))

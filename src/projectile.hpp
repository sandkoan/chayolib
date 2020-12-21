#ifndef quadratic_h
#define quadratic_h
namespace chayolib{
    class projectile{
        private:
            double angle;
            int velocity;
            int height;
            // Map for values
        public:
            projectile(int vel, double ang, int h);
            ~projectile();
            void make_equations();
            int set_velocity(int z);
            int set_height(int h);
            double set_angle(double a);
            double impact();
            double max_height();
            double quadratic(double a, double b, double c);
            void full_calculate();
            void get_equation();
    };
}
#endif
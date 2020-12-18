import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
global xdata, ydata
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

global z
z = -0.6

def update(frame):
    global z
    if frame == 0:
        z = z + 0.2
    print(frame)
    xdata.append(frame)
    ydata.append(np.sin(frame)-z)
    ln.set_data(xdata, ydata)

    return ln,


ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 20),
                    init_func=init, blit=True)
plt.show()
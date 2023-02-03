# visual.py
# Max Liang
# created 02/03/2022
# Description:
#


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from rigid_object import *

test_object = rigid_object(vel=np.array([1, 1, 1]), ang_vel=np.array([1, 1, 1]))

# def pos_update():
#     pass
#
# def line_update():
#     line.set_data()
#     line.set_3d_properties()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# x, y, z = test_object.pos[0], test_object.pos[1], test_object.pos[2]
# ang_x, ang_y, ang_z = test_object.ang_pos[0], test_object.ang_pos[1], test_object.ang_pos[2]
# ax.plot(x, y, z, 'ro')
# ax.plot([x, ang_x], [y, ang_y], [z, ang_z], lw=2)
# plt.show()

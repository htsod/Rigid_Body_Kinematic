# filed_functions.py
# Max Liang
# created 01/03/2023
# Description:
#
#
#
#


import numpy as np


def uniform_x(pos):
    return [1, 0, 0]


def central_force(pos):
    x, y, z = pos[0], pos[1], pos[2]
    r = -pos
    r_abs = np.sqrt(x**2 + y**2 + z**2)
    return r / r_abs**3





# rho_functions.py
# Max Liang
# created 01/01/23
# Description:
#
#
#
#


import numpy as np


def spherical_coor(vec, origin):
    x, y, z = vec[0]-origin[0], vec[1]-origin[1], vec[2]-origin[2]
    r = np.sqrt(x**2 + y**2 + z**2)
    try:
        theta = np.arctan(np.sqrt(x**(2) + y**(2)) / z)
    except ZeroDivisionError:
        theta = np.pi / 2
    try:
        phi = np.arctan(y / x)
    except ZeroDivisionError:
        phi = np.pi / 2
    return r, theta, phi



def asymmetric_sphere(grid, pos, constraint):
    r, theta, phi = spherical_coor(grid, pos)
    if r < constraint:
        return np.sin(theta) * np.cos(phi)**2
    else:
        return 0


def box(grid, pos, constraint):
    cond1 = 0 < (grid[0] - pos[0]) < constraint[0]
    cond2 = 0 < (grid[1] - pos[1]) < constraint[1]
    cond3 = 0 < (grid[2] - pos[2]) < constraint[2]
    if cond1 and cond2 and cond3:
        return 1
    else:
        return 0


# rigid_object.py
# Max Liang
# created 02/03/2023
# Description:


import numpy as np


class rigid_object:
    def __init__(self, pos=np.array([0, 0, 0]), vel=np.array([0, 0, 0]),
                 ang_pos=np.array([0, 0, 1]), ang_vel=np.array([0, 0, 0])):
        self.vel = vel
        self.pos = pos
        self.ang_pos = ang_pos
        self.ang_vel = ang_vel

    def _update_pos(self):
        self.pos += self.vel

    def _update_ang_pos(self):
        theta_x, theta_y, theta_z = self.ang_vel[0], self.ang_vel[1], self.ang_vel[2]
        cx, sx = np.cos(theta_x), np.sin(theta_x)
        cy, sy = np.cos(theta_y), np.sin(theta_y)
        cz, sz = np.cos(theta_z), np.sin(theta_z)
        R_tensor = np.array([[cy*cz, cy*sz, -sy],
                      [sx*sy*cz - cx*sz, sx*sy*sz + cx*cz, sx*cy],
                      [cx*sy*cz + sx*sz, cx*sy*sz - sx*cz, cx*cy]])
        self.ang_pos *= R_tensor

    def _update_ang_vel(self, ang_acl_vec):
        self.ang_vel += ang_acl_vec

    def _update_vel(self, acl_vec):
        self.vel += acl_vec

    def apply_forces(self, acl_vec, ang_acl_vec):
        self._update_vel(acl_vec)
        self._update_ang_vel(ang_acl_vec)

    def update_frame(self):
        self._update_pos()
        self._update_ang_pos()

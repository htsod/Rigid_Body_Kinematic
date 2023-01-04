# kinematic_class.py
# Max Liang
# created 12/28/2022
# Description:
#
#
#


import numpy as np


class rigid_object:
    def __init__(self, rho=None, initial_position=np.array([0, 0, 0]), velocity=np.array([0, 0, 0]),
                 angular_velocity=np.array([0, 0, 0])):
        self.rho = rho
        self.init_pos = initial_position
        self.vel = velocity
        self.ang_vel = angular_velocity
        self.mass = 0
        self.cm_pos = np.array([0, 0, 0])
        self.pos_vec = np.array([0, 0, 0])
        self.in_tensor = np.zeros((3, 3))

    # functions to initialize object's variables
    def _init_rho(self, grid_class, geo_func, constraint):
        emp_vals = grid_class.empty_vals()
        pos_vec = []
        for index, g in enumerate(grid_class.grid):
            emp_vals[index] += geo_func(g, self.init_pos, constraint)
            pos_vec.append(g)
        self.rho = (emp_vals, pos_vec)

    def _get_mass(self):
        self.mass = np.sum(self.rho[0])

    def _init_cm_pos(self, grid_class):
        r_cm = np.array([0, 0, 0])
        iterator = 0
        for index, g in enumerate(grid_class.grid):
            r = self.rho[0][iterator] * np.array(g)
            r_cm += r
        r_cm = r_cm / self.mass
        self.cm_pos = r_cm

    def _init_rho_cm(self):
        for vec in range(len(self.rho[1])):
            self.rho[1][vec] = self.cm_pos - self.rho[1][vec]

    def _inertia_tensor(self):
        in_tensor = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                if i == j:
                    refer_list = [0, 1, 2]
                    refer_list.remove(i)
                    for val, coor in zip(self.rho[0], self.rho[1]):
                        a, b = refer_list[0], refer_list[1]
                        sub_tot = val * ((coor[a] - self.cm_pos[a]) ** 2 + (coor[b] - self.cm_pos[b]) ** 2)
                        in_tensor[i][j] += sub_tot
                elif i != j:
                    for val, coor in zip(self.rho[0], self.rho[1]):
                        sub_tot = - val * (coor[i] - self.cm_pos[i]) * (coor[j] - self.cm_pos[j])
                        in_tensor[i][j] += sub_tot
        self.in_tensor = in_tensor

    # update object kinematic from given forces
    def _convert_pos_vec(self):
        for index, vec in self.rho[1]:
            self.pos_vec[index] = vec + self.cm_pos

    def _eval_force(self, forces):
        net_force = np.array([0, 0, 0])
        net_torque = np.array([0, 0, 0])
        for index, vec in enumerate(self.pos_vec):
            for force in forces:
                if vec == force[0]:
                    net_force += force[1]
                    net_torque += np.cross(force[1], self.rho[1][index])
        return net_force, net_torque

    def _apply_force(self, net_force, net_torque, in_tensor):
        self.vel += net_force / self.mass
        self.ang_vel += in_tensor * net_torque

    def _theta_rotate(self):
        rot_mag = self.ang_vel.dot(self.ang_vel)
        rot_dir = self.ang_vel / rot_mag
        cosine = np.cos(rot_mag)
        sine = np.sin(rot_mag)
        rot_matrix = np.zeros((3, 3))
        flip = 1
        for i in range(3):
            flip *= -1
            for j in range(3):
                if i == j:
                    rot_matrix[i][j] = cosine + rot_dir[i] ** 2 * (1 - cosine)
                    flip *= -1
                if i != j:
                    refer_list = [0, 1, 2]
                    refer_list.remove(i)
                    refer_list.remove(j)
                    if flip:
                        rot_matrix[i][j] = rot_dir[i] * rot_dir[j] * (1 - cosine) - (-1) ** (i + j) * rot_dir[
                            refer_list[0]] * sine
                    else:
                        rot_matrix[i][j] = rot_dir[i] * rot_dir[j] * (1 - cosine) - (-1) ** (i + j + 1) * rot_dir[
                            refer_list[0]] * sine
        return rot_matrix

    def _update_ang_pos(self):
        for vec in range(len(self.rho[1])):
            self.rho[1][vec] *= self._theta_rotate()

    def _update_cm_pos(self):
        self.cm_pos += self.vel

    def _update_rho_cm(self):
        for vec in range(len(self.rho[1])):
            self.rho[1][vec] += self.cm_pos

    def initialize_object(self, grid_class, geo_function, constraint):
        self._init_rho(grid_class, geo_function, constraint)
        self._get_mass()
        self._init_cm_pos(grid_class)
        self._init_rho_cm()
        self._inertia_tensor()

    def update_object(self, forces):
        self._convert_pos_vec()
        net_force, net_torque = self._eval_force(forces)
        self._apply_force(net_force, net_torque)
        self._update_ang_pos()
        self._update_cm_pos()







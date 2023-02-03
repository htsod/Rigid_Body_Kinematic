# test.py
# Max Liang
# created 01/01/23
# Description:
#
#
#
#


from grid_class import *
from kinematic_class import *
from force_class import *
from field_functions import *
from rho_functions import *
from numpy.random import rand

coordinate = grid(100, [0, 0, 0])
sphere_obj = rigid_object()
sphere_obj.initialize_object(coordinate, asymmetric_sphere, 10)

forces = [force(rand(3), rand(3)), force(rand(3), rand(3))]
f_field = force_field(coordinate)
f_field.generate_field(coordinate, uniform_x)

sphere_obj.update_object(forces)
sphere_obj.update_object(f_field.field)




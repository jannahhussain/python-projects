# task: write a function that takes in:
# 3 inputs
import math
from datetime import date

def calculate_side_AB_by_pythag(side_bc, side_ac):
    sum_of_input_squared = (side_bc * side_bc) + (side_ac * side_ac)
    side_ab = math.sqrt(sum_of_input_squared)
    return side_ab

def calculate_side_BC_by_pythag(AB, AC):
    sum_of_input_squared = (AB^2) - (AC^2)
    BC = math.sqrt(sum_of_input_squared)
    return BC

def calculate_side_AC_by_pythag(AB, BC):
    sum_of_input_squared = (AB * AB) - (BC * BC)
    AC = math.sqrt(sum_of_input_squared)
    return AC

# print(calculate_side_AB_by_pythag(2, 2))
# print(calculate_side_BC_by_pythag(5, 4))
# print(calculate_side_AC_by_pythag(8, 3))

def calculate_unknown_side(AB, AC, BC):
    if AB is None:
        return calculate_side_AB_by_pythag(BC, AC)
    if BC is None:
        return calculate_side_BC_by_pythag(AB, AC)
    if AC is None:
        return calculate_side_AC_by_pythag(AB, BC)

# print(calculate_unknown_side(None, 2, 2))
print(calculate_unknown_side(5, 4, None))
# print(calculate_unknown_side(8, None, 3))




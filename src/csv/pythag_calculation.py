import math


def square_function(length):
    square = length * length
    return square


def pythagorean(a_side, b_side):
    hypotenuse_squared = a_side + b_side
    hypotenuse = math.sqrt(hypotenuse_squared)
    print "hypotenuse= ", hypotenuse


first_side = input("side A: ")
second_side = input("side B: ")


first_side_squared = square_function(first_side)
second_side_squared = square_function(second_side)

pythagorean(first_side_squared, second_side_squared)

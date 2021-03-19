import math


def area_of_circles(radius):
    area = (math.pi * radius) * (math.pi * radius)
    return area


def circ_of_circles(radius):
    circ = 2 * math.pi * radius
    return circ


def do_build_data(current_position, line_array):
    build_data = ""

    if current_position > 1:
        name = line_array[0]
        radius = int(line_array[1])

        a = " area = "
        c = " circumference = "
        area_of_circle = area_of_circles(radius)
        circ_of_circle = circ_of_circles(radius)
        build_data += name + a + str(area_of_circle) + c + str(circ_of_circle)

    return build_data

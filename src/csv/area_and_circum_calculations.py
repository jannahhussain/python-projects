import math


def area_of_circle(radius):
    # area of circle  pi  * radius squared
    area = math.pi * (radius * radius)
    return area


def circ_of_circle(radius):
    circ = 2 * math.pi * radius
    return circ


def do_build_data(current_position, line_array):
    build_data = ""

    if current_position > 1:
        name = line_array[0]
        radius = int(line_array[1])

        area = " area = "
        circumference = " circumference = "
        circle_area = area_of_circle(radius)
        circle_circ = circ_of_circle(radius)
        build_data += name + area + str(circle_area) + circumference + str(circle_circ)

    return build_data





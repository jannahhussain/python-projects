def trapezium_area(side_a, side_b, distance_between):
    length_of_parallel = (side_a + side_b) / 2
    area = length_of_parallel * distance_between
    return area


def do_build_data(current_position, line_array):
    build_data = ""

    if current_position > 1:
        name = line_array[0]
        side_a = int(line_array[1])
        side_b = int(line_array[2])
        distance_between = int(line_array[3])

        area = ": area = "
        area_of_trapezium = trapezium_area(side_a, side_b, distance_between)
        build_data += name + str(area) + str(area_of_trapezium) + "cm^2"

    return build_data

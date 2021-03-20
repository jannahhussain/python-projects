import csv
import area_and_circum_calculations as acc


with open('radius_of_circles.csv') as circles_file:
    csv_reader = csv.reader(circles_file, delimiter=",")

    current_position = 1

    for line_array in csv_reader:
        build_data = acc.do_build_data(line_array, current_position)

        if build_data != "":
            print(build_data)

        current_position += 1

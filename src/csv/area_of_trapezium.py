import csv
import trapezium_area_calculator as tac


with open('trapezium.csv') as trapezium_file:
    csv_reader = csv.reader(trapezium_file, delimiter=",")

    current_position = 1

    for line_array in csv_reader:
        build_data = tac.do_build_data(current_position, line_array)

        if build_data != "":
            print(build_data)

        current_position += 1

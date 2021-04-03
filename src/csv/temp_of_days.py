import csv
import temperature_calculations as tc

with open('days_and_temp.csv') as temp_file:
    csv_reader = csv.reader(temp_file, delimiter=",")

    current_position = 1
    header = []
    for line_array in csv_reader:
        if current_position == 1:
            header = line_array

        build_data = tc.do_build_data(line_array, current_position, header)
        if build_data is not None:
            print(build_data)

        current_position += 1

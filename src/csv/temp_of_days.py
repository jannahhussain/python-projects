import csv
import temperature_calculations as tc

with open('days_and_temp.csv') as temp_file:
    csv_reader = csv.reader(temp_file, delimiter=",")

    current_position = 1
    header = 1
    for line_array in csv_reader:
        build_data = tc.do_build_record(current_position, line_array, header)
        print(line_array)

        current_position += 1

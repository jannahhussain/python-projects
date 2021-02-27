import csv


with open('family.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = 1

    for line_array in csv_reader:
        build_record = ""

        if header > 1:
            build_record += line_array[0] + " " + line_array[1] + " " + line_array[2] + " " + line_array[3]
            print(build_record)

        header += 1


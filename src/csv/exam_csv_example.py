import csv
import build_record as br

# ***********************************************************
# Build the record so that it adds up all the marks and
# appends it to the users name as a report
#
# e.g. Jannah - Score: 40
# ***********************************************************


with open('gcse_scores.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = 1

    for line_array in csv_reader:
        build_record = br.do_build_record(line_array, header)
        header += 1

        if build_record != "":
            print(build_record)








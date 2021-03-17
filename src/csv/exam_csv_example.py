import csv
import build_record as br

# ***********************************************************
# Build the record so that it adds up all the marks and
# appends it to the users name as a report
#
# e.g. Jannah - Score: 40
# changed: 13 March
# ***********************************************************


with open('gcse_scores.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # what is our current position
    current_position = 1

    for line_array in csv_reader:
        build_record = br.do_build_record(line_array, current_position)

        if build_record != "":
            print(build_record)

        # move (or increment) the position to the next line
        current_position += 1









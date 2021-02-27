import csv
import math

# ***********************************************************
# Build the record so that it adds up all the marks and
# appends it to the users name as a report
#
# e.g. Jannah - Score: 40
# ***********************************************************


def add_scores(maths, english, science, french, history):
    total_score = maths + english + science + french + history
    return total_score


with open('exam_results.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = 1

    for line_array in csv_reader:
        build_record = ""

        if header > 1:
            name = line_array[0]
            maths = int(line_array[1])
            english = int(line_array[2])
            science = int(line_array[3])
            french = int(line_array[4])
            history = int(line_array[5])

            scores = add_scores(maths, english, science, french, history)
            build_record += name + " - Score: " + str(scores)

        header += 1
        print(build_record)






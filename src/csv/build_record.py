def add_scores(maths, english, science, french, history):
    total_score = maths + english + science + french + history
    return total_score


def average_scores(maths, english, science, french, history):
    average_score = (maths + english + science + french + history) / 5
    return average_score


def do_build_record(line_array, current_position):
    build_record = ""

    # only process when we are NOT at the header which is line 1
    if current_position > 1:
        name = line_array[0]
        maths = int(line_array[1])
        english = int(line_array[2])
        science = int(line_array[3])
        french = int(line_array[4])
        history = int(line_array[5])

        average_score = average_scores(maths, english, science, french, history)
        build_record += name + " - average score: " + str(average_score)

    return build_record

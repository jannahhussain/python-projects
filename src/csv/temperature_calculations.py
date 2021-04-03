def do_build_data(line_array, current_position, header):
    build_data = ""


    if current_position > 1:
        day = line_array[0]
        morning = int(line_array[1])
        afternoon = int(line_array[2])
        evening = int(line_array[3])
        night = int(line_array[4])

        highest = max(morning, afternoon, evening, night)
        position = line_array.index(str(highest))
        highest_period = header[position]

        lowest = min(morning, afternoon, evening, night)
        position = line_array.index(str(lowest))
        lowest_period = header[position]

        build_data += day + ": highest temp = " + str(highest) + " the period is: " + highest_period + \
                      ", lowest temp = " + str(lowest) + " the period is: " + lowest_period

        return build_data

def get_highest_period(highest, line_array, header):
    pass

def get_lowest_period(lowest, line_array, header):
    pass


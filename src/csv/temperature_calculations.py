def do_build_data(line_array, current_position):
    build_data = ""

    if current_position > 1:
        day = line_array[0]
        morning = int(line_array[1])
        afternoon = int(line_array[2])
        evening = int(line_array[3])
        night = int(line_array[4])

        highest = max(morning, afternoon, evening, night)
        lowest = min(morning, afternoon, evening, night)

        build_data += day + ": highest temp = " + str(highest) + ", lowest temp = " + str(lowest)

        return build_data

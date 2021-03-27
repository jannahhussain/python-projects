def temperature(morning, afternoon, evening, night):
    highest = max(morning, afternoon, evening, night)
    lowest = min(morning, afternoon, evening, night)
    return highest and lowest


def do_build_record(line_array, current_position):
    build_record = ""

    if current_position <= 0:
        day = line_array[0]
        morning = line_array[1]
        afternoon = line_array[2]
        evening = line_array[3]
        night = line_array[4]

        temp = temperature(day, morning, afternoon, evening, night)
        build_record += day + " high of " + str(temp) + "low of " + str(temp)

    return build_record


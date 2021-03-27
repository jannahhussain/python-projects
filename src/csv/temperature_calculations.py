def temperature(morning, afternoon, evening, night):
    highest = max(morning, afternoon, evening, night)
    lowest = min(morning, afternoon, evening, night)
    return highest and lowest


def do_build_record(line_array, current_position, header):
    if current_position > 1:
        return line_array


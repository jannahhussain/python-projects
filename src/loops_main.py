import src.loops.loops_examples as counters

# counters.looping_counters_5_times()
# counters.printing_numbers_backwards()
# count = 10
#
# while counters.loop_when_gt_zero(count):
#     print("hello", count)
#     count -= 1
#
# if 1 == 1:
#     print("hello")

size_of_array = len(counters.my_array)
start_position = 0
end_position = size_of_array - 1

# while start_position <= end_position:
#     print(counters.my_array[start_position])
#     start_position += 1

sentence = ""
while start_position <= end_position:
    if start_position == end_position:
        sentence += counters.my_array[start_position] + "."
    else:
        sentence += counters.my_array[start_position] + " "

    start_position += 1

print(sentence.capitalize())

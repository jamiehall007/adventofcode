from twentytwentytwo import utils


# Part 1
def day_six_one(inp):
    start = marker_length = 4
    idx = 0
    for i in range(len(inp) - start + 1):
        possible_marker = inp[idx:start]
        if len(set(possible_marker)) == marker_length:
            return start
        else:
            start += 1
            idx += 1


# Part 2
def day_six_two(inp):
    start = marker_length = 14
    idx = 0
    for i in range(len(inp) - start + 1):
        possible_marker = inp[idx:start]
        if len(set(possible_marker)) == marker_length:
            return start
        else:
            start += 1
            idx += 1


if __name__ == "__main__":
    day_six_input = utils.get_file_obj("day6.txt").readline().strip("\n")

    part_one_result = day_six_one(day_six_input)
    print(f"Part 1: {part_one_result}")

    part_two_result = day_six_two(day_six_input)
    print(f"Part 2: {part_two_result}")

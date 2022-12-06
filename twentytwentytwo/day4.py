def get_file_obj(filename: str):
    fh = open(f"inputs/{filename}", "r")
    return fh


def does_it_overlap(start1, end1, start2, end2):
    """Does the range (start1, end1) overlap with (start2, end2)?"""
    return end1 >= start2 and end2 >= start1


fully_contained = 0
overlapping = 0
for line in get_file_obj("day4.txt"):
    left, right = line.split(',')
    l_start, l_stop = left.split("-")
    x = range(int(l_start), int(l_stop) + 1)

    r_start, r_stop = right.split("-")
    y = range(int(r_start), int(r_stop) + 1)

    if overlap := does_it_overlap(x[0], x[-1], y[0], y[-1]):
        overlapping += 1

    if overlap and (set(x).intersection(y) == set(x) or set(y).intersection(x) == set(y)):
        fully_contained += 1

print(f"{overlapping=}")
print(f"{fully_contained=}")

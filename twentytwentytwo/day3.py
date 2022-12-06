

def get_file_obj(filename: str):
    fh = open(f"inputs/{filename}", "r")
    return fh


# Part 1
total = 0
for line in get_file_obj("day3.txt"):
    compartment_1 = set(line[:len(line)//2])
    compartment_2 = set(line[len(line)//2:])

    overlap = compartment_1.intersection(compartment_2)

    for item in overlap:
        value = ord(item) - 96
        if value < 0:
            value += 58

        total += value
        print(item, value)

print("Part 1")
print(total)

# Part 2
rucksacks = []
counter = 0
total = 0
for line in get_file_obj("day3.txt"):
    rucksacks.append(set(line.strip()))
    counter += 1

    if counter == 3:
        overlap = rucksacks[0].intersection(rucksacks[1])
        full_overlap = overlap.intersection(rucksacks[2])

        for item in full_overlap:
            value = ord(item) - 96
            if value < 0:
                value += 58

            total += value

        rucksacks.clear()
        counter = 0

print("Part 2")
print(total)

from collections import defaultdict

records = defaultdict(lambda: 0)

with open("inputs/day1.txt", "r") as fh:
    elf = 1
    for line in fh:
        try:
            calories = int(line)
        except Exception:
            elf += 1
        else:
            records[elf] += calories

# part 1
max_calories = max(records.values())
print(f"Total calories from elf carrying most calories: {max_calories}")

# part 2
all_calories = sorted(list(records.values()), reverse=True)
print(f"Total calories from top three elves carrying most calories: {sum(all_calories[:3])}")

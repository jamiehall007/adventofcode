from collections import defaultdict


def get_file_obj(filename: str):
    fh = open(f"inputs/{filename}", "r")
    return fh


def parse_dock(filename):
    dock = defaultdict(lambda: [])
    for line in get_file_obj(filename):
        if line == '\n':
            break

        crates = line.replace('    ', ' * ').strip().split()
        tidy_crates = [crate.replace('[', '').replace(']', '').replace('*', '') for crate in crates]

        for i, crate in enumerate(tidy_crates):
            try:
                int(crate)
            except ValueError:
                if crate:
                    dock[i + 1].append(crate)
            else:
                continue

    cargo = {}
    for key, value in dock.items():
        cargo[key] = value[::-1]

    return cargo


# Part 1
def process_movements(dock):
    for line in get_file_obj("day5.txt"):
        if not line.startswith('move'):
            continue

        commands = []
        for command in line.strip().split():
            try:
                action = int(command)
            except Exception:
                continue

            commands.append(action)

        for i in range(commands[0]):
            moved = dock[commands[1]].pop()
            dock[commands[2]].append(moved)

    return dock


print("Part 1")
setup = parse_dock("day5.txt")
result = process_movements(setup)
for col, stack in result.items():
    print(stack[-1], end='')

print('\n-----------------')


# Part 2
def process_movements(dock):
    for line in get_file_obj("day5.txt"):
        if not line.startswith('move'):
            continue

        commands = []
        for command in line.strip().split():
            try:
                action = int(command)
            except Exception:
                continue

            commands.append(action)

        moved = dock[commands[1]][-1 * commands[0]:]
        dock[commands[1]] = dock[commands[1]][:-1 * commands[0]]
        dock[commands[2]].extend(moved)

    return dock


print("Part 2")
setup = parse_dock("day5.txt")
result = process_movements(setup)
for col, stack in result.items():
    print(stack[-1], end='')

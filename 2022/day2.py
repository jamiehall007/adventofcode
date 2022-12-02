# PART 1

scores = {
    ('A', 'X'): 4,  # 3+1
    ('A', 'Y'): 8,  # 6+2
    ('A', 'Z'): 3,  # 0+3
    ('B', 'X'): 1,  # 0+1
    ('B', 'Y'): 5,  # 3+2
    ('B', 'Z'): 9,  # 6+3
    ('C', 'X'): 7,  # 6+1
    ('C', 'Y'): 2,  # 0+2
    ('C', 'Z'): 6,  # 3+3
}

with open("inputs/day2.txt", "r") as fh:
    total = 0
    for line in fh:
        parts = line.split()
        total += scores[(parts[0], parts[1])]

    print(f'part 1: {total}')

# PART 2
scores = {
    'result': {
        'X': 0,
        'Y': 3,
        'Z': 6
    },
    'Y': {
        'A': 1,
        'B': 2,
        'C': 3
    },
    'Z': {
        'A': 2,
        'B': 3,
        'C': 1
    },
    'X': {
        'A': 3,
        'B': 1,
        'C': 2
    }
}

with open("inputs/day2.txt", "r") as fh:
    total = 0
    for line in fh:
        played, option = line.split()

        total += scores['result'][option]

        if option == 'X':
            total += scores[option][played]
        elif option == 'Y':
            total += scores[option][played]
        elif option == 'Z':
            total += scores[option][played]

    print(f'part 2: {total}')

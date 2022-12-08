f = open("input", "r")
file = f.read()


def part1():
    marker = 0
    sequence = []
    for letter in file:
        marker += 1
        if letter in sequence:
            sequence = []
        sequence.append(letter)
        if len(sequence) == 4:
            return marker


def part2():
    marker = 0
    sequence = []
    for letter in file:
        marker += 1
        if letter in sequence:
            sequence = []
            continue
        sequence.append(letter)
        if len(sequence) == 14:
            return marker


print(part2())
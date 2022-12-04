file = open("input", "r")
lines = file.readlines()


def part1():
    count = 0
    for line in lines:
        line = line.split(",")
        elf1, elf2 = line[0].split("-"), line[1].split("-")
        elf1start, elf1end = int(elf1[0]), int(elf1[1])
        elf2start, elf2end = int(elf2[0]), int(elf2[1])
        if (elf1start >= elf2start and elf2end >= elf1end) or (elf2start >= elf1start and elf1end >= elf2end):
            count += 1
    return count


def part2():
    count = 0
    for line in lines:
        line = line.split(",")
        elf1, elf2 = line[0].split("-"), line[1].split("-")
        elf1start, elf1end = int(elf1[0]), int(elf1[1])
        elf2start, elf2end = int(elf2[0]), int(elf2[1])
        for i in range(elf1start, elf1end + 1):
            if i in range(elf2start, elf2end + 1):
                count += 1
                break
    return count


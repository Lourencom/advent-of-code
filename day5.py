def part1():
    stacks = []
    for i in range(9):
        stacks.append([])
    f = open("input", "r")
    lines = f.readlines()
    currstack = 0
    for col in range(1, 3*9 + 8, 4):
        for row in range(8):
            if lines[row][col] == " ":
                continue
            stacks[currstack].append(lines[row][col])
        currstack += 1

    for i in range(9):
        stacks[i].reverse()

    for i in range(10, len(lines)):
        line = lines[i].split()
        quantity = int(line[1])
        stackFrom = stacks[int(line[3]) - 1]
        stackTo = stacks[int(line[5]) - 1]
        toMove = stackFrom[-quantity:]
        stackFrom = stackFrom[:-quantity]
        print(toMove)
        toMove.reverse()
        for elem in toMove:
            stackTo.append(elem)
        stacks[int(line[3]) - 1] = stackFrom
        stacks[int(line[5]) - 1] = stackTo

    out = ""
    for i in stacks:
        out += i[len(i) - 1]
    print(out)


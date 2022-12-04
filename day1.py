import math
# This is a sample Python script.

inp = open("input", "r")
def maximumelf():
    value = 0
    lines = inp.readlines()
    elfs = []
    for line in lines:
        if line == "\n":
            elfs.append(value)
            value = 0
        else:
            value += int(line)
    elfs.sort(reverse=True)
    print(elfs[0] + elfs[1] + elfs[2])

maximumelf()

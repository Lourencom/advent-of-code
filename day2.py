# he plays Rock, Paper, Scissor
him = {"A": 0, "B": 1, "C": 2}
# I play Rock Paper Scissor
me = {"X": 0, "Y": 3, "Z": 6}
f = open("input", "r")
points = 0
for line in f.readlines():
    he = him.get(line[0])
    outcome = me.get(line[2])
    if outcome == 6:
        i = (he + 1) % 3
    elif outcome == 3:
        i = he
    else:
        i = (he - 1 + 3) % 3
    points += i + outcome + 1
print(points)


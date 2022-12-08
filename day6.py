file = open("input", "r")
f = file.read()
marker = 0
sequence = []
for letter in f:
    marker += 1
    if letter in sequence:
        sequence = []
    sequence.append(letter)
    if len(sequence) == 4:
        print(marker)
        break

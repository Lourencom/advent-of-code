def getPriority(char):
    num = 0
    if char.isupper():
        num += 26
    num += ord(char.lower()) - 96
    return num


file = open("input", "r")
lines = file.readlines()
priority = 0
for i in range(0, len(lines), 3):
    line1, line2, line3, done = lines[i], lines[i + 1], lines[i + 2], False
    for char1 in line1:
        if done:
            break
        for char2 in line2:
            if done:
                break
            if char2 != char1:
                continue
            for char3 in line3:
                if char3 == char1:
                    priority += getPriority(char3)
                    done = True
                    break
print(priority)

with open("inp03.txt") as file:
    for row in file.read().splitlines():
        st = row

# Part 1
houses= [(0,0)]
sx, sy = 0, 0
for i in range(len(st)):
    if st[i] == "^":
        sy += 1
    elif st[i] == "v":
        sy -= 1
    elif st[i] == ">":
        sx += 1
    elif st[i] == "<":
        sx -= 1
    houses.append((sx, sy))
print(len(set(houses)))

# Part 2
houses= [(0,0)]
sx, sy = 0, 0
rx, ry = 0,0
for i in range(len(st)):
    if i % 2 == 0:
        if st[i] == "^":
            sy += 1
        elif st[i] == "v":
            sy -= 1
        elif st[i] == ">":
            sx += 1
        elif st[i] == "<":
            sx -= 1
        houses.append((sx, sy))
    else:
        if st[i] == "^":
            ry += 1
        elif st[i] == "v":
            ry -= 1
        elif st[i] == ">":
            rx += 1
        elif st[i] == "<":
            rx -= 1
        houses.append((rx, ry))
print(len(set(houses)))

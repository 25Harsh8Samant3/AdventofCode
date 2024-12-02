# Part 1
paper = 0
with open("inp2.txt") as file:
    for row in file.read().splitlines():
        l, w, h = map(int, row.split("x"))
        small = min(l * w, w * h, h * l)
        paper += (2 * (l * w + w * h + h * l) + small)
print(paper)

# Part 2
ribbon = 0
with open("inp2.txt") as file:
    for row in file.read().splitlines():
        l, w, h = map(int, row.split("x"))
        small = min(2 * (l + w), 2 * (w + h), 2 * (h + l))
        ribbon += (small + (l * w * h))
print(ribbon)
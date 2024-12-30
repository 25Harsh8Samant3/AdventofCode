# Part 1
grid = [[0 for i in range(1000)] for j in range(1000)]

with open("inp06.txt") as file:
    for row in file.read().splitlines():
        ops = row.split(" ")
        if ops[0] == "toggle":
            x1, y1 = map(int, ops[1].split(","))
            x2, y2 = map(int, ops[3].split(","))
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] = 1 - grid[i][j]
        
        elif ops[0] == "turn":
            x1, y1 = map(int, ops[2].split(","))
            x2, y2 = map(int, ops[4].split(","))
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if ops[1] == "on":
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
lit = 0
for i in grid:
    for j in i:
        if j == 1:
            lit += 1
print(lit)


# Part 2
grid = [[0 for i in range(1000)] for j in range(1000)]

with open("inp06.txt") as file:
    for row in file.read().splitlines():
        ops = row.split(" ")
        if ops[0] == "toggle":
            x1, y1 = map(int, ops[1].split(","))
            x2, y2 = map(int, ops[3].split(","))
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] += 2
        
        elif ops[0] == "turn":
            x1, y1 = map(int, ops[2].split(","))
            x2, y2 = map(int, ops[4].split(","))
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if ops[1] == "on":
                        grid[i][j] += 1
                    else:
                        grid[i][j] -= 1
                        if grid[i][j] < 0:
                            grid[i][j] = 0 
bright = 0
for i in grid:
    bright += sum(i)
print(bright)
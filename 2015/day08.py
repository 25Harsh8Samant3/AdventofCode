# Part 1
ans = 0
with open("inp08.txt") as file:
    for row in file.read().splitlines():
        ans += len(row) - len(eval(row))
print(ans)

# Part 2
ans = 0 
with open("inp08.txt") as file:
    for row in file.read().splitlines():
        ans += 2 + row.count("\\") + row.count("\"")
print(ans)
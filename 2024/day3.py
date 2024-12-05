import re

# Part 1
mul = 0
with open("inp3.txt") as file:
    data = file.read()
matches = re.findall(r"mul\((\d+),(\d+)\)", data)
for op in matches:
    no1, no2 = map(int, op)
    mul += no1 * no2
print(mul)

# Part 2
enable = 0
with open("inp3.txt") as file:
    data = file.read()
matches = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
flag = True
for op in matches:
    if op == "do()":
        flag = True
    elif op == "don't()":
        flag = False
    else:
        if flag:
            no1, no2 = map(int, op[4:-1].split(","))
            enable += no1 * no2
print(enable)
with open("input.txt") as f:
    for row in f.read().splitlines():
        st = row
ans = 0

# Part 1
for i in st:
    if i == "(":
        ans += 1
    elif i == ")":
        ans -= 1
print(ans)

# Part 2
i = 0
while ans != -1:
    if st[i] == "(":
        ans += 1
    elif st[i] == ")":
        ans -= 1
    i += 1
print(i)
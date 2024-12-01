# Part 1
l1, l2 = [], []
dist = 0
with open("inp1.txt") as f:
    for row in f.read().splitlines():
        n1, n2 = map(int, row.split("   "))
        l1.append(n1)
        l2.append(n2)
l1.sort()
l2.sort()
for i, j in zip(l1, l2):
    dist += abs(i-j)
print(dist)

# Part2
l1, freq = [], {}
similarity = 0
with open("inp1.txt") as f:
    for row in f.read().splitlines():
        n, k = map(int, row.split("   "))
        l1.append(n)
        freq[k] = freq.get(k, 0) + 1
for i in l1:
    similarity += i * freq.get(i, 0)
print(similarity)
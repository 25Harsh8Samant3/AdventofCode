from collections import defaultdict
from itertools import permutations

graph = defaultdict(list)
cities = set()

with open("inp09.txt") as file:
    for row in file.read().splitlines():
        src, _, dest, _, distance = row.strip().split()
        graph[src].append((dest, int(distance)))
        graph[dest].append((src, int(distance)))
        cities.add(src)
        cities.add(dest)

# Part 1
ans = float("inf")
for perm in permutations(cities):
    dist = 0
    for i in range(len(perm) - 1):
        for dest, distance in graph[perm[i]]:
            if dest == perm[i + 1]:
                dist += distance
    if dist > 0:
        ans = min(ans, dist)
print(ans)

# Part 2
ans = float("-inf")
for perm in permutations(cities):
    dist = 0
    for i in range(len(perm) - 1):
        for dest, distance in graph[perm[i]]:
            if dest == perm[i + 1]:
                dist += distance
    if dist > 0:
        ans = max(ans, dist)
print(ans)

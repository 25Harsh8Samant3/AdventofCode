import json
import re

# Part 1
ans = 0
with open('inp12.txt') as file:
    for row in file.read().splitlines():
        array = re.findall(r'-?\d+', row)
for i in array:
    ans += int(i)
print(ans)

# Part 2
with open('inp12.txt') as file:
    def decoder(obj):
        if isinstance(obj, dict) and 'red' in obj.values():
            return {}
        return obj
    doc = json.load(file, object_hook=decoder)
pattern = re.compile(r'-?\d+')
result = sum(map(int, pattern.findall(json.dumps(doc))))
print(result)

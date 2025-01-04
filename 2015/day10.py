string = input()
copy = string

# Part 1
for _ in range(40):
    updated_string = ""
    i = 0
    while i < len(string):
        cnt = 1
        while i + cnt < len(string) and string[i] == string[i + cnt]:
            cnt += 1
        updated_string += str(cnt) + string[i]
        i += cnt
    string = updated_string
print(len(updated_string))

# Part 2
string = copy
for _ in range(50):
    updated_string = ""
    i = 0
    while i < len(string):
        cnt = 1
        while i + cnt < len(string) and string[i] == string[i + cnt]:
            cnt += 1
        updated_string += str(cnt) + string[i]
        i += cnt
    string = updated_string
print(len(updated_string))

# Part 1
def nice_string(string):
    vowels = "aeiou"
    forbidden = ["ab", "cd", "pq", "xy"]
    vowels_count = 0
    has_double, has_forbidden = False, False

    for i in range(len(string)):
        if string[i] in vowels:
            vowels_count += 1
        if i > 0 and string[i] == string[i - 1]:
            has_double = True
        if i > 0 and string[i - 1] + string[i] in forbidden:
            has_forbidden = True

    return vowels_count >= 3 and has_double and not has_forbidden

with open("inp05.txt") as file:
    nice = 0
    for row in file.read().splitlines():
        st = row
        if nice_string(st):
            nice += 1
        # print(st, nice_string(st))
    print(nice)

# Part 2
def nice_string(string):
    is_twice, is_repeat = False, False
    
    for i in range(len(string) - 3):
        sub = string[i: i + 2]
        if sub in string[i + 2:]:
            is_twice = True
            break
    if not is_twice:
        return False
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            is_repeat = True
            break
    return is_repeat

with open("inp05.txt") as file:
    nice = 0
    for row in file.read().splitlines():
        st = row
        if nice_string(st):
            nice += 1
        # print(st, nice_string(st))
    print(nice)
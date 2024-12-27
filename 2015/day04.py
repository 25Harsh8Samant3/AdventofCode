from hashlib import md5

string = input().strip()

# Part 1
flag = True
no = 0
while flag:
    message = string + str(no)
    hash = md5(message.encode()).hexdigest()
    if hash[:5] == "00000":
        flag = False
        print(message[len(string):])
    no += 1

# Part 2
flag = True
no = 0
while flag:
    message = string + str(no)
    hash = md5(message.encode()).hexdigest()
    if hash[:6] == "000000":
        flag = False
        print(message[len(string):])
    no += 1
password = input()
alphabet = list("abcdefghjkmnpqrstuvwxyz")
convert, revert = {}, {}
for idx, alp in enumerate(alphabet):
    convert[alp] = idx
    revert[idx] = alp

def update(input):
    pwd= [convert[c] for c in input]
    incr_st, non_pair = False, False 
    
    while not incr_st or not non_pair:
        incr_st, non_pair = False, False
        pair_count, unique_pair = 0, [] 

        pwd[-1] = pwd[-1] + 1 
        for i in range(len(pwd)):
            if pwd[i] > 22:
                pwd[i] = 0
                pwd[i-1] = pwd[i-1]+1

        for i in range(len(pwd)-2):
            if pwd[i] + 1 == pwd[i+1] and pwd[i] + 2 == pwd[i+2]:
                incr_st = True

        for i in range(len(pwd)-1):
            if pwd[i] == pwd[i+1] and pwd[i] not in unique_pair:
                pair_count += 1
                unique_pair.append(pwd[i])
        if pair_count >= 2:
            non_pair = True
    
    return "".join(revert[p] for p in pwd)

# Part 1
next_password = update(password)
print(next_password)

#Part 2
next_password = update(next_password)
print(next_password)
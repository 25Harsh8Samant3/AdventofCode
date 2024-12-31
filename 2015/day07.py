def get_val(var):
    if var.isnumeric():
        return int(var)
    if vars[var] is not None:
        return vars[var]
    if len(ops[var]) == 1:
        if ops[var][0].isnumeric():
            return int(ops[var][0])
        else:
            return get_val(ops[var][0])
    if ops[var][0] == "NOT":
        vars[var] = ~ get_val(ops[var][1])
    elif ops[var][1] == "AND":
        vars[var] = get_val(ops[var][0]) & get_val(ops[var][2])
    elif ops[var][1] == "OR":
        vars[var] = get_val(ops[var][0]) | get_val(ops[var][2])
    elif ops[var][1] == "LSHIFT":
        vars[var] = get_val(ops[var][0]) << get_val(ops[var][2])
    elif ops[var][1] == "RSHIFT":
        vars[var] = get_val(ops[var][0]) >> get_val(ops[var][2])
    return vars[var]

# Part 1
vars, ops = {}, {}
with open("inp07.txt") as file:
    for row in file.read().splitlines():
        ins, var = row.split("->")
        ops[var.strip()] = ins.strip().split()
        vars[var.strip()] = None
        if len(ops[var.strip()]) == 1:
            if ops[var.strip()][0].isnumeric():
                vars[var.strip()] = int(ops[var.strip()][0])

ans = get_val("a")
print(ans)

# Part 2
vars, ops = {}, {}
with open("inp07.txt") as file:
    for row in file.read().splitlines():
        ins, var = row.split("->")
        ops[var.strip()] = ins.strip().split()
        vars[var.strip()] = None
        if len(ops[var.strip()]) == 1:
            if ops[var.strip()][0].isnumeric():
                vars[var.strip()] = int(ops[var.strip()][0])

vars["b"] = ans
ans = get_val("a")
print(ans)
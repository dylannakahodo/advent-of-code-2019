with open("input.txt") as f:
    l = f.read().strip()

l = l.split(',')
l = list(map(int, l))

# 99 ends program
# 1 is addition
# 2 is multiplication

i = 0
l[1] = 12
l[2] = 2

op_code = l[i]

while op_code != 99:
    op_code = l[i]
    pos_1 = l[i+1]
    pos_2 = l[i+2]
    dest = l[i+3]

    if op_code == 1:
        l[dest] = l[pos_1] + l[pos_2]
    elif op_code == 2:
        l[dest] = l[pos_1] * l[pos_2]

    i += 4
print(f'Answer: {l[0]}')
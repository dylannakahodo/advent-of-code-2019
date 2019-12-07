with open("input.txt") as f:
    l = f.read().strip()
l = l.split(',')
l = list(map(int,l))

for noun in range(100):
    for verb in range(100):
        l_copy = l[:]
        i = 0
        op_code = l_copy[i]
        l_copy[i+1] = noun
        l_copy[i+2] = verb
        
        while op_code != 99:
            op_code = l_copy[i]
            pos_1 = l_copy[i+1]
            pos_2 = l_copy[i+2]
            dest = l_copy[i+3]

            if op_code == 1:
                l_copy[dest] = l_copy[pos_1] + l_copy[pos_2]
            elif op_code == 2:
                l_copy[dest] = l_copy[pos_1] * l_copy[pos_2]
            elif op_code == 99:
                break
            i += 4

        if l_copy[0] == 19690720:
            print(f"Answer = {100 * noun+verb}")
            exit
        
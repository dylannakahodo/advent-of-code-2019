with open('input.txt') as f:
    lines = f.read().splitlines()

print(sum((int(num)//3)-2 for num in lines))

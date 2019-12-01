def calculate_fuel(mass):
    return (mass//3) - 2

with open('input.txt') as f:
    lines = f.read().splitlines()

masses = map(int, lines)
total_cost = 0

for mass in masses:
    while (calculate_fuel(mass) > 0):
        mass = calculate_fuel(mass)
        total_cost += mass
print(total_cost)
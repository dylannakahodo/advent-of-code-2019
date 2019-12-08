# - It is a six-digit number.
# - The value is within the range given in your puzzle input.
# - Two adjacent digits are the same (like 22 in 122345).
# - Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# How many different passwords in your range?
# Range = 137683-596253

total_passwords = 0
for num in range(137683, 597254):
    num = list(str(num))
    is_increasing = (num == sorted(num))
    no_adjacent = (len(num) == len(set(num)))

    if is_increasing and not no_adjacent:
        total_passwords += 1

print(f"Total passwords = {total_passwords}")
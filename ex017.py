any_str = input("Please enter a string: ")
count_of_letter = 0
count_of_number = 0
count_of_space = 0
count_of_other = 0

for ch in any_str:
    if ch.isalpha():
        count_of_letter += 1
    elif ch.isdigit():
        count_of_number += 1
    elif ch.isspace():
        count_of_space += 1
    else:
        count_of_other += 1

print('space: ', count_of_space)
print('digit: ', count_of_number)
print('alpha: ', count_of_letter)
print('other: ', count_of_other)

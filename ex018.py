number = input("Please enter a number: ")
repeat = int(input("Please enter how many times it will repeat: "))

result = 0
for i in range(1, repeat + 1):
    result += int(number * i)

print(result)

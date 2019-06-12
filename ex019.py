def perfect_number(number):
    total = []
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            total.append(i)

    if sum(total) == number:
        return total


if __name__ == '__main__':
    for num in range(1, 1001):
        if perfect_number(num) is not None:
            print(num, "=", " + ".join([str(x) for x in perfect_number(num)]))

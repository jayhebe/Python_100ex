# **题目：**判断101-200之间有多少个素数，并输出所有素数。


def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
        return True


def print_prime_numbers(start, end):
    for j in range(start, end + 1):
        if is_prime(j):
            print(j, end=" ")


if __name__ == '__main__':
    print_prime_numbers(1, 100)

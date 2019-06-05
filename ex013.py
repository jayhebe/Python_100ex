# **题目：**打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
# 其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，
# 因为153=1的三次方＋5的三次方＋3的三次方。


for number in range(100, 1000):
    x, y, z = [int(i) for i in list(str(number))]
    if x ** 3 + y ** 3 + z ** 3 == number:
        print(number, end=" ")

# **输入三个整数x,y,z，请把这三个数由小到大输出。

x, y, z = input("Please enter 3 integers and seperated by comma: ").split(",")
print(sorted([int(i) for i in (x, y, z)]))

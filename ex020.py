# **题目：**一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

dis = 100
total = 0

for i in range(1, 10):
    total += 2 * dis * (0.5 ** i)

print("total = ", dis + total)

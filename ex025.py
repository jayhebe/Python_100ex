# 求1+2!+3!+...+20!的和。


res = 1
for i in range(20, 1, -1):
    res = i * res + 1
print(res)

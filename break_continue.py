# coding:utf8
# 计算 0 - 100奇数的和:

sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x%2 == 0:
        continue
    sum = sum + x 
print sum
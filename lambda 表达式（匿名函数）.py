# coding:utf8
# 编程中提到的 lambda 表达式，通常是在需要一个函数，
# 但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
print  map( lambda x: x*x, [y for y in range(10)] )


def sq(x):
    return x * x

print map(sq, [y for y in range(10)])
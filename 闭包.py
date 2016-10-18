# coding:utf8
# 内层函数引用了外层函数的变量（参数也算变量）
# 然后返回内层函数的情况，称为闭包（Closure）
#def calc_sum(lst):
#    def lazy_sum():
#        return sum(lst)
#    return lazy_sum

# 返回闭包不能引用循环变量，请改写count()函数，
# 让它正确返回能计算1x1、2x2、3x3的函数。
def count():
    fs = []
    for i in range(1, 4):
        def f(a=i):
        	return a*a
        fs.append(f)
    return fs

f1, f2, f3= count()
print f1,f2,f3,f1()
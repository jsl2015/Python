# coding:utf8
#reduce()函数接收的参数和 map()类似，一个函数 f，一个list，
#但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，
#reduce()对list的每个元素反复调用函数f，并返回最终结果值。
a = [2, 4, 5, 7, 12]
def f(x, y):
	return x*y
print reduce(f, a)


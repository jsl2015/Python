# coding:utf8
# Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。
# 使用 decorator 用Python提供的 @ 语法，装饰函数的参数是被装饰的函数，return返回原函数
# 目的就是为了简化编程，减少重复代码

def log(f):
	def fn(x):
		print 'call ' + f.__name__+'()...'
		return f(x)
	return fn

@log('DEBUG')  # 装饰的实质语句是：f=factorial(n) ; factorial=log(factorial(n)) (装饰函数返回的是原函数)
def my_func():
	pass 

print my_func()
# coding: utf8
#map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，
#并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
import math
def add(x, y, f):
	return f(x) + f(y)
print add(25, 9, math.sqrt)

a = ['adam', 'LISA', 'barT']
def f(x):
	return x.capitalize()
print map(f,a)
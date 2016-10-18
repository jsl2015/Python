# coding:utf8
# 比较函数的定义是，传入两个待比较的元素 x, y，
# 如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
def reversed_cmp(x, y):
	if x> y:
		return -1
	if x< y:
		return 1
	return 0

print sorted([36, 5, 12, 9, 21],cmp =reversed_cmp)

def cmp_ignore_case(s1, s2):
	return cmp(s1.lower(), s2.lower())

print sorted(['bod', 'abount', 'Zoo', 'Credit'], cmp = cmp_ignore_case)


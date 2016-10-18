# coding:utf8
# method 1：
try:
	f = open(r'C:\Users\jsl\Desktop\py\1.py', 'r')
	print f.readline()
finally:
	if f:
		f.close()

# method 2：
with open(r'C:\Users\jsl\Desktop\py\1.py', 'r') as f:
	print f.read()

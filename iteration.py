L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
	print index, '-', name

for t in enumerate(L):
	index = t[0]
	name = t[1]
	print index, '-' , name

L = ['Adam', 'Lisa', 'Bart', 'Paul']
a = [1, 2, 3, 4]
b = zip(a, L)
for index, name in b:
	print index,'-',name

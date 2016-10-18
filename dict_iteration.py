d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
#a = d.values()
#print (a[0] + a[1] + a[2] + a[3]) / 4
sum = 0.0
for i in d.values():
	sum = sum + i

print sum / 4

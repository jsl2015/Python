import re

a = 'someone@gmail.com'
b = 'bill.gates@microsoft.com'
for i in [a,b]:
	if re.match(r'^[a-z\.]+@[a-z]+\.com',i):
		print 'OK.'
	else:
		print 'Fail.' 
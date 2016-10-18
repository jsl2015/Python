try:
	import cPickle as pickle
except ImportError:
	import pickle

d = dict(name='Bob', age=20, score=88)
f = open('dump.txt', 'wb')
pickle.dump(d,f)
f.close()
print f

e = open('dump.txt', 'rb')
d = pickle.load(e)
f.close()
print d
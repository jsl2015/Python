# encoding:utf8
# 如果一个属性由双下划线开头(__)，该属性就无法被外部访问

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print p.name
try:
	print p.__score
except AttributeError:
	print 'attributeerror'


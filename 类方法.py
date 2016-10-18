# coding:utf8
# 通过 @classmethod 将一个方法绑定到一个类上，而非类的实例

class Person(object):

    __count = 0   # 外部通过类方法可以访问这个  私有属性

    @classmethod
    def how_many(cls):
    	print 'I am a method of Person.'
    	return cls.__count
    def __init__(self,name):
    	self.name = name
    	Person.__count=Person.__count+1

print Person.how_many()

p1 = Person('Bob')


print Person.how_many()



# coding:utf8
#定义类属性可以直接在 class 中定义：
#
#class Person(object):
#    address = 'Earth'
#    def __init__(self, name):
#        self.name = name
#因为类属性是直接绑定在类上的，所以，访问类属性不需要创建实例，就可以直接访问：
#
#print Person.address
# => Earth

# 请给 Person 类添加一个类属性 count，每创建一个实例，
# count 属性就加 1，这样就可以统计出一共创建了多少个 Person 的实例。
class Person(object):
    count = 0
    def __init__(self,name):
    	self.name = name
    	Person.count = Person.count+1  # self为实例，Person为类，这里需要使用Person.count

p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count
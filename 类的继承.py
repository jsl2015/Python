# coding:utf8
# 函数super(Student, self)将返回当前类继承的父类，即 Person ，然后调用__init__()方法，
# 注意self参数已在super()中传入，在__init__()中将隐式传递，不需要写出（也不能写）。

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course



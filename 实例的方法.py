# coding:utf8
# 实例的方法就是在类中定义的函数，它的第一个参数永远是 self，
# 指向调用该方法的实例本身，其他参数和一个普通函数是完全一样的：

#请给 Person 类增加一个私有属性 __score，表示分数，再增加一个实例方法 get_grade()，
# 能根据 __score 的值分别返回 A-优秀, B-及格, C-不及格三档。

class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):      # 实例的方法能调用实例的私有属性__score，虽然无法被外部访问
        if self.__score >= 90:
        	return 'A-优秀'
        elif self.__score >= 60:
        	return 'B-及格'
        elif self.__score < 60:
        	return 'C-不及格'

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()


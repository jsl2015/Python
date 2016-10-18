class Person(object):
    def __init__(self, name, gender, birth, **kw ):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.__dict__.update(kw)

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job

# Python内置的@property装饰器就是负责把一个方法变成属性调用的：


class Student(object):
    def __init__(self, age=25):
        self._age = age

    @property
    def age(self):
        print("get age")
        return self._age

    @age.setter
    def age(self, age):
        if age < 0 or age > 200:
            raise ValueError("age must be an integer!")
        else:
            self._age = age


s = Student(16)
print(s.age)


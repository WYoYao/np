import types


class Student(object):
    def __init__(self, age):
        self.age = age


# 给类绑定一个属性

Student.name = "leo"


def say(self, text=""):
    print(self.name, self.age, text)


def run(self):
    print("running")


# 给 类绑定一个方法
Student.run = run

s = Student(25)

# 实例绑定一个方法
s.say = types.MethodType(say, s)

s.say("hello World")
s.run()


# 因为是动态语言所以可以自由的给实例添加属性和方法，但是可以通过 __slots__  来限定属性的实例


class Child(object):
    __slots__ = ("name", "age")


c = Child()

c.name = "leo"
c.age = 25
# c.like = "play"  添加的时候会报错
print(c.name, c.age)


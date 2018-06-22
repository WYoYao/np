
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：


class Student(object):
    # 这个属性虽然归类所有，但类的所有实例都可以访问到。
    name = "student"
    age = 25

    def __init__(self):
        self.name = "leo"

    def say():
        print("study")


print(Student().name)  # 实例上面有的时候直接方位实例的属性
print(Student().age)  # 如果实例上面没有的属性 会 继续访问类的属性

a = Student()
b = Student()

print(a.age)
print(b.age)

# 这并不是修改的 Student 类的属性,因为python 是动态语言的可以自由的添加属性,这个操作相当于给实例 a 添加一个age 属性
a.age = 26

print(a.age)  # 访问上一步 a 添加的属性 age
print(b.age)  # b 的访问仍然会先寻找自身是否拥有对应的属性,没有找到然后找到了对应的 Student 类的属性
print(Student.age)  # Student 类上面的属性并没有被修改

# 修改类的属性
Student.age = 27
# 不会修改已经
print(a.age)  # a 访问自身属性上面的属性，所以还是原来的26
print(b.age)  # b 本身没有age 属性，然后找到的对应的 Student类上面的属性
print(Student().age)  # 新的实例也和b 一样本身没有age 的属性,所以同时返回的 Student 上面的属性


def tf(obj):
    obj.age += 1
    return obj.age


class Test(object):
    add = lambda x: tf(x)

    def __init__(self):
        self.age = 0


t1 = Test()
t2 = Test()

t1.add()



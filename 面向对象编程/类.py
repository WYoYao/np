
#  class后面紧接着是类名，即Person，
# 类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，
# 如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Person(object):
    # 必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候
    def __init__(self, name="暂无", age=18):
        self.__name = name
        self.__age = age

    def say(self, world):
        print("i am %s,%s" % (self.__name, world))


stu = Person()

# <__main__.Person object at 0x000001EBE3077FD0>
#          对应的类          内存地址
print(stu)


stu.say("hello world")


# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。


class Student(dict):
    def __init__(self, name="leo"):
        self._name = name

    # 转换成为 str 类型后的返回值
    def __str__(self):
        return "Student object (name: %s)" % self._name

    __repr__ = __str__


s = str(Student("tom"))
print(s)
print(Student("tom"))

# 直接显示变量调用的不是__str__()，而是__repr__() , __repr__()是为调试服务的。


# __iter__ 用于迭代的时候的返回

import collections


class It(object):
    # 用于 for in 这样的循环
    def __iter__(self):
        return (n for n in range(100))

    # 用于返回 next() 中执行的对象
    def __next__(self):
        return 1

    # 通过下标取出元素，需要实现__getitem__()方法：
    def __getitem__(self, n):
        return [n for n in range(100)][n]


print(isinstance(It(), collections.Iterable))

print(next(It()))

for x in It():
    print(x)

print(It()[49])


# __getattr__() 获取实例的属性  可以避免直接报错的情况


class O(object):
    def __getattr__(self, key):
        print(key)
        return None


print(O().name)

# __call__ 将实例当成方法一样调用


class C(object):
    def __call__(self, num):
        print("num is " + num)


C()("leo")


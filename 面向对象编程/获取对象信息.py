
# 使用 type 来获取 实例对象的类型

import types


def fn():
    pass


#
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

print(type("123"))  # str
print(type("123") == str)
print(isinstance("123", str))

print(type(123))  # int
print(type(123) == int)
print(isinstance(123, int))

print(type(1.23))  # float
print(type(1.23) == float)
print(isinstance(1.23, float))

print(type(True))  # bool
print(type(True) == bool)
print(isinstance(True, bool))

print(type(fn))  # function
print(type(fn) == types.FunctionType)
print(isinstance(fn, types.FunctionType))

print(type([]))  # list
print(type([]) == list)
print(isinstance([], list))

print(type((0,)))  # tuple
print(type((0,)) == tuple)
print(isinstance((0,), tuple))

print(type({}))  # dict
print(type({}) == dict)
print(isinstance({}, dict))

print(type(abs))  # 内建函数  不属于 type.FunctionType
print(type(abs) == types.BuiltinFunctionType)
print(isinstance(abs, types.BuiltinFunctionType))

print(
    type(lambda x: x)
)  #  lambda  属于 LambdaType  (推测 LambdaType 可能的 父类中有 types.FunctionType)
print(type(lambda x: x) == types.LambdaType)
print(isinstance(lambda x: x, types.LambdaType))


print(type((x for x in range(10))))  # 生成器
print(type((x for x in range(10))) == types.GeneratorType)
print(isinstance((x for x in range(10)), types.GeneratorType))


# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

# ? 疑问 lambda 函数竟然和 types.FunctionType  types.LambdaType 同时属于
print(
    type(lambda x: x) == types.FunctionType,
    type(lambda x: x) == types.LambdaType,
    isinstance(lambda x: x, types.FunctionType),
    isinstance(lambda x: x, types.LambdaType),
)


class Parent(object):
    pass


class Child(Parent):
    pass


print(
    isinstance(Parent(), Parent),  # 类实例属于类
    isinstance(Child(), Parent),  # 子类实例也属于父类
    isinstance(Parent(), Child),  # 父类实例不属于子类
    type(Child()) == Parent,  # 子类不等于父类
)


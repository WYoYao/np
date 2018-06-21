# 闭包保存对象
def fn(num):
    # 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
    # 名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
    return map(lambda n: lambda: n * n, range(num))


for f in fn(10):
    print(f())

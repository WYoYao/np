# 1
def fn(o, arr=[]):
    arr.append(0)
    return arr


# print([])
# print(fn(1))
# print(fn(1))
# print(fn(1))

# 2

#  利用 * 将 Tuple 和 Set 转化成为序列参数
def total(*tp):
    total = 0
    for item in tp:
        total += item
    return total


# print(total(*[1, 2, 3, 4]))
# print(total(*(1, 2, 3, 4)))


dc = {"name": "leo", "like": "play"}

# 利用 ** 将dict转换成为 key-value 的键值序列 来的实现命名关键字参数
def test(a, b, **c):
    # 修改之前和原来相同
    print(c == dc)
    print(c)
    c["name"] = "leoleoleo"
    print(c)
    # 修改之后和原来不同 同时修改的时候不影响原来参数
    print(c == dc)
    # print(a, b, c)


# test(1, 12, **dc)
# print(dc)

# 如果需要使用命名关键字参数的时候没有可变参数, 可以使用 * 来分割进行声明命名关键字参数
def between(a, *, name):
    print(a, name)


between(123, name="leo")


# 参数类型分为 5类

# 1必填参数 必须输入
def argu1(name):
    pass


# 2默认参数 不必须输入有默认值
def argu2(name="leo"):
    pass


# 3可变参数  可以传入多个参数，参数个数不固定
def argu3(*arr):
    pass


# 4关键字参数 可以传入多个 key-value 的参数
def argu4(**dict):
    pass


# 5命名关键字参数
def argu5(*, name):
    print(name)


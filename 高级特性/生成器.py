# generator
from collections import Iterable

# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x + y for x in "123" for y in "456")

#  generator 也是可遍历的对象
print(isinstance(g, Iterable))

# 可以使用next 来进行生成
print(next(g))
print(next(g))
print(next(g))


#   可以使用for in 来进行遍历
#   通过for循环来迭代它，并且不需要关心StopIteration的错误。
for item in g:
    print(item)

# 使用 yield 通过函数生成 generator
def gg(num):
    while num < 100:
        num += 1
        yield num
    return num


for item in gg(0):
    print(item)


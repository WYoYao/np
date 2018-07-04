#class list(object)

>  ### list() -> new empty list

>  ### list(iterable) -> new list initialized from iterable's items

>  ### append(...)
>      append() 方法用于在列表末尾添加新的对象。

```
l = []
l.append(1)
# [1]
```

>  clear(...)
>      clear() 函数用于清空列表

```
l = [1, 2, 3, 4]
l.clear()
# []
```

>  copy(...)
>      L.copy() -> list -- a shallow copy of L
>      copy() 函数用于复制列表，类似于 

```
l = [[1], [2]]
ll = l.copy()
#[[1], [2]]
#[[1], [2]]

ll == l
# True

ll[0].append(2)

ll == l
# True

ll, l
# [[1, 2], [2]],[[1, 2], [2]]
# copy 方法中的执行的浅copy 引用类型的指向还是没有确定
```

>  
> count(...)
> count() 方法用于统计某个元素在列表中出现的次数。

```
a = [str(n % 10) for n in range(100)]
a.count("1")
# 10
```

>  
>  extend(...)
>      extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。

```
a = [n for n in range(10)]

b = [n for n in range(10, 20)]

a.extend(b)

print(a)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

>  index(...)
>      L.index(value, [start, [stop]]) -> index() 函数用于从列表中找出某个值第一个匹配项的索引位置。

```
a = [n % 10 for n in range(20)]

print(a.index(4))
# 4

print(a.index(4, 5, -1))
# 14
```

>  insert(...)
>      L.insert(index, object) -- insert object before index

```
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a.insert(4, "Insert")
print(a)
# [0, 1, 2, 3, 'Insert', 4, 5, 6, 7, 8, 9]
```

>  pop(...)
>      L.pop([index]) -> pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

```
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a.pop(1))
# 1
print(a)
# [0, 2, 3, 4, 5, 6, 7, 8, 9]
print(a.pop(-2))
# 8
print(a)
# [0, 2, 3, 4, 5, 6, 7, 9]
```

>  
>  remove(...)
>      L.remove(value) -> remove() 函数用于移除列表中某个值的第一个匹配项。

```
a = [1, 2, 3, 1, 2, 3]

a.remove(1)

print(a)
```

>  reverse(...)
>      L.reverse() -- reverse *IN PLACE*

```
a = [0, 1, 2, 3]
a.reverse()
print(a)
```

>  sort(...)
>      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
>  

```
a = [-5, -2, -1, 0, 1, -4, -3, 2, 3, 4, 5]
# 降序
a.sort(reverse=True)
print(a)

b = [{"name": "leo", "age": n} for n in range(10, 20)]


def takeSecond(item):
    return item["age"]


b.sort(key=takeSecond, reverse=True)

print(b)
```
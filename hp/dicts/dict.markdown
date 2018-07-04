# class dict(object)
###   dict() 
>-    返回空的字典
>     
>-    dict(mapping) -> 从映射对象初始化的新字典

```
dict({"name": "leo"})
# {'name': 'leo'}
```

>     dict(iterable) -> 迭代创建一个dict:
>         d = {}
>         for k, v in iterable:
>             d[k] = v

```
dict([[n, n] for n in range(10)])
#{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
```

>     dict(**kwargs) -> new dictionary initialized with the name=value pairs
>         in the keyword argument list.  For example:  dict(one=1, two=2)
>     
>     Methods defined here:
>     
>###     clear(...)
>         D.clear() -> None.  Remove all items from D.

```
d = dict([[n, n] for n in range(10)])
# {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
d.clear()
d
# {}
```

>###     copy(...)
>         D.copy() -> 浅拷贝

```
d = dict({"name": "leo"})
dd = d.copy()
# {'name': 'leo'}
```
  
>###     fromkeys(iterable, value=None, /) 根据迭代器生成 dict

```
d = dict.fromkeys(("name", "age", "like"), 10)
#{'name': 10, 'age': 10, 'like': 10}
```

>###     get(...)
>         D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
>         获取属性固若没有则返回None

```
d = dict.fromkeys(("name", "age", "like"), 10)

d.get("name")
# 10

d.get("sex")
# None
```

>###     items(...)
>         D.items() -> 返回 每个 k,v组成的Tuple 的集合。

```
d = dict.fromkeys(("name", "age", "like"), 10)
d.items
# [('name', 10), ('age', 10), ('like', 10)]
for k, v in d.items():
    print(k, v)
# name 10
# age 10
# like 10
```

>###     keys(...)
>         D.keys() ->  返回一个key 的集合。

```
d = dict.fromkeys(("name", "age", "like"), 10)
d.keys()
# ['name', 'age', 'like']
```
   
>     pop(...)
>         D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
       移除一个key 值，返回对应的 value

```
d = dict.fromkeys(("name", "age", "like"), 10)
# 删除 dict 对应的 key,然后返回对应value
d.pop("name")
# 10
d
# {'age': 10, 'like': 10}
```

>###     popitem(...)
>         D.popitem() -> (k, v), remove and return some (key, value) pair as a
>         方法随机返回并删除字典中的一对键和值。 如果 dict 中已经没有key了之后的再调用会报错。

```
d = dict.fromkeys(("name", "age", "like"), 10)

for item in range(3):
    print(d.popitem())
```

>###     setdefault(...)
>         D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
>         Python 字典 setdefault() 方法和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。

```
d = dict.fromkeys(("name", "age", "like"), 10)
d.setdefault("name", "leo")
# 10
d.setdefault("sex", 1)
# 1
```     

>###     update(...)
>         D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
>         If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
>         If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
>         In either case, this is followed by: for k in F:  D[k] = F[k]

```
d = {'Name': 'Runoob', 'Age': 7}
d2 = {'Sex': 'female'}

d.update(d2)
print("更新字典 dict : ", d)
```

>###     values(...)
>         D.values() -> an object providing a view on D's values
>         提供D值的视图的对象

```
d = {'Name': 'Runoob', 'Age': 7}
print(d.values())
# ['Runoob', 7]
```


# class set(object)
>   set() -> new empty set object
>   set(iterable) -> new set object
>   
>   Build an unordered collection of unique elements.
>   构建一个不重复的集合

>   ### add(...)
>       Add an element to a set.
>       
>       This has no effect if the element is already present.
```
s = set([1, 2, 3, 4, 5])
# {1, 2, 3, 4, 5}
s.add(6)
s.add(1)
# {1, 2, 3, 4, 5, 6}
```

>   
>   ### clear(...)
>       Remove all elements from this set.
>       移除所有的实例

```
s = set([1, 2, 3, 4, 5])
s.clear()
# set()
```

>   ### copy(...)
>       Return a shallow copy of a set.
>       浅copy Set对象

```
s = set([1, 2, 3, 4, 5])
ss = s.copy()
# {1, 2, 3, 4, 5} # {1, 2, 3, 4, 5}
```
 
>   ### difference(...)
>       Return the difference of two or more sets as a new set.
>       
>       (i.e. all elements that are in this set but not the others.)

```
s = set([1, 2, 3])
ss = set([2, 3, 4])
# 返回 s 有 但是 ss 没有的差集
print(s.difference(ss))
# 如果需要取全部差集 可以使用 symmetric_difference
print(s.symmetric_difference(ss))
```

>   ### difference_update(...)
>       Remove all elements of another set from this set.
>        表示集合A中存在，但是在集合B中不存在的元素，并更新A集合，没有返回值。

```
s = set([1, 2, 3])
ss = set([2, 3, 4])
s.difference_update(ss)
print(s)  # {1}
```

>   ### discard(...)
>       Remove an element from a set if it is a member.
>       
>       If the element is not a member, do nothing.
>       移除集合中的元素，且如果元素不存在，不会发生错误。

```
s = set(("Google", "Runoob", "Taobao"))
s.discard("Google")
# {'Taobao', 'Runoob'}
s.discard("Google")
# 不报错
```

>   
>   ### intersection(...)
>       Return the intersection of two sets as a new set.
>       取交集
>       (i.e. all elements that are in both sets.)

```
a = set([1, 2, 3])
b = set([2, 3, 4])

print(set.intersection(a, b))
# {2, 3}
```

>   ### intersection_update(...)
>       Update a set with the intersection of itself and another.
>   将第一个对象更新为交集

```
a = set([1, 2, 3])
b = set([2, 3, 4])

set.intersection_update(a, b)
print(a)
# {2, 3}
print(b)
# {2, 3, 4}
```

>   ### isdisjoint(...)
>       Return True if two sets have a null intersection.
>       判断两个集合是否相交

```
print(set.isdisjoint(set([1, 2]), set([2, 3])))
# False
print(set.isdisjoint(set([1, 2]), set([3, 4])))
# True
```

>   ### issubset(...)
>       Report whether another set contains this set.
>       另一个集合是否包含此集合。   

```
print(set([1, 2]).issubset(set([1, 2, 3, 4])))
# True
print(set([1, 2]).issubset(set([2, 3, 4])))
# False
```

>   ### issuperset(...)
>       Report whether this set contains another set.
>       此集是否包含另一个集。

```
print(set([1, 2, 3, 4, 5]).issuperset(set([1, 2])))
# True
print(set([1, 2, 3, 4, 5]).issuperset(set([1, 2, 8])))
# False
```

>   ### pop(...)
>       Remove and return an arbitrary set element.
>       Raises KeyError if the set is empty.
>       删除并返回任意set元素。
>       如果集合为空，则引发KeyError。

```
s = set(["a", "b", "c", "d"])
print(s.pop())
# b
print(s)
# {'d', 'c', 'a'}
```

>   ### remove(...)
>       Remove an element from a set; it must be a member.
>       
>       If the element is not a member, raise a KeyError.
>       移除 Set 的一个属性，如果传入的属性不存在则报错

```
s = set(["a", "b", "c", "d"])
s.remove("b")
# b
print(s)
# {'d', 'c', 'a'}
s.remove("leo")
# KeyError
```

>   ### symmetric_difference(...)
>       Return the symmetric difference of two sets as a new set.
>       (i.e. all elements that are in exactly one of the sets.)
>       返回两组的对称差异作为新集合。

```
set([1, 2, 3]).symmetric_difference(set([2, 3, 4]))
# {1, 4}
```

>   ### symmetric_difference_update(...)
>       Update a set with the symmetric difference of itself and another.
>       更新具有自身和另一个的对称差异的集合。

```
s = set([1, 2, 3])
s2 = set([2, 3, 4])

s.symmetric_difference_update(s2)
print(s)
# {1, 4}
```

>   ### union(...)
>       Return the union of sets as a new set.
>       将集合的并集作为新集合返回。
>       (i.e. all elements that are in either set.)

```
s = set([1, 2, 3])
s2 = set([2, 3, 4])

s.union(s2)
# {1, 2, 3, 4}
```   

>   ### update(...)
>       Update a set with the union of itself and others.
>       使用自身和其他人的联合更新集合。

```
s = set([1, 2, 3])
s2 = set([2, 3, 4])

s.update(s2)

print(s)
# {1, 2, 3, 4}
```
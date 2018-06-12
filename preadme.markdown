
### tuple

> 相当于不可变的list
> 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

```python
# 会被当成小括号
t=(1)
# 如果要声明一个tuple 的时候需要添加一个逗号，来消除歧义
t=(1,)
```

> tuple 只是第一层的数据引用地址不可变,如果tuple 中的某一项也是引用类型的情况下,只要这个引用的地址不进行改变就可以进行改变。

### if

> if(x) 可以简写为 if x

```python
#False
print(not not '') 
#True
print(not not '1')
#False
print(not not [])
#True
print(not not [1])
#False
print(not not 0)
#True
print(not not 1)
```

### for in 
> for in 用来做循环处理，但是没有传统 for 循环中还是需要进行执行 所以使用的 range 来产生对应的数组来进行循环。

```python
for num in range(10):
    print(num)
```

> continue 跳过本次循环
> break    跳过所有的循环

### Dict

> 判断是否拥有属性

```python
# 可以通过 in 来执行判断
'name' in {'name':'leo'}
# 可以用过 get() == None
{'name':'leo'}.get('name') == None
# 可以使用 pop 来删除对应的属性
{'name':'leo'}.pop('name')
```

### Set

> set可以看成数学意义上的无序和无重复元素的集合

```python
s1=set([1,2,3])
s2=set([3,4,5])

print(s1 & s2) # set([3])
print(s1 | s2) # set([1, 2, 3, 4, 5])
```

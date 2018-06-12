### 常用的语法对比

JS          | python        | 描述
--          | --            | -- 
\|\|        | or            | 或
not         | !             | 非
if else     | elif          | elif是else if的缩写





### JS Array vs Python list

JS                      | python            | 描述
--                      | --                | -- 
[].length               | len([])           | 获取数组的长度（python中叫list）
[].push(n)              | [].append(n)      | 数组尾部追加数据
[].splice(n,0,1)        | [].insert(n,1)    | 指定位置追加数据
[].splice(n,1)          | [].pop(n)         | 制定位置删除数据

### JS Object vs Python dict

JS                              | python                      |  描述  
--                              | --                          | --
Object {}                       | dict {}                     |  都是 Object 类型
{key:1}.hasOwnProperty('key')   | 'key' in {'key':1}          |  都可以判断是否用这个属性
delete {'name':'leo'}           | {'name':'leo'}.pop('name')  |  删除对应的属性

> 有些情况需要先验证是否拥有这个属性，引用不确定的属性的可能直接引起报错。

### JS Set() vs Python Set()

> set可以看成数学意义上的无序和无重复元素的集合。

JS                          | python                       | 描述  
--                          |--                            | --
add 会返回Set对象             | add 只会添加属性，不会返回对象   |在Set对象尾部添加一个元素。
delete                      | remove                       |移除Set的中与这个值相等的元素



[明天继续](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167832686474803d3d2b7d4d6499cfd093dc47efcd000)
from collections import namedtuple,deque,defaultdict,OrderedDict

# namedtuple
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
Point = namedtuple("Point",("x","y"))

p=Point(1,2)
print("x:%s y:%s" % (p.x,p.y))
print(type(p))
print(isinstance(p,Point))
print(isinstance(p,tuple))

# deque
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
d=deque([1,2,3])
d.append(4)
d.appendleft(0)
print(list(d))
d.insert(1,.5)
print(d)


# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dc=defaultdict(lambda : None)

dc["name"]="leo"
print(dc["name"],dc["age"])

# OrderedDict
# 如果要保持Key的顺序，可以用OrderedDict
# 是有序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# 是无序的
dc = dict({"a":1,"b":2,"c":3})
# OrderedDict 中的排序是根据插入的顺序排序而不是字母的顺序
od["e"]=5
od["d"]=4
print(od,dc)

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
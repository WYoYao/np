import json

d = dict(name='Bob', age=20, score=88)
# 转换成为 json 字符串
print(type(json.dumps(d)),json.dumps(d))
print(type(json.loads(json.dumps(d))),json.loads(json.dumps(d)))

# 转换 flie-like 并写入文件
with open("./src/pic/txt.txt","w+") as target:
    json.dump(d,target)
# 将 flie-like 转换成为 Dict
with open("./src/pic/txt.txt","r+") as target:
    t=json.load(target)
    print(type(t),t)

class Student(object):
    def __init__(self,name,age,like):
        self.name=name
        self.age=age
        self.like=like

s=Student('leo','25','play')
import pickle
import json

d = dict(name='Bob', age=20, score=88)

print(json.dumps(d))
print(pickle.dumps(d))

# 将对象序列化保存到文件中
with open("./src/pic/txt.txt","wb") as target:
    pickle.dump(d,target)

with open("./src/pic/txt.txt","rb") as target:
    print(pickle.load(target))

# 将对象序列化保存到文件中
with open("./src/pic/txt1.txt","w+") as target:
    json.dump(d,target)

with open("./src/pic/txt1.txt","r+") as target:
    print(json.load(target))


# 可以继承 dict 然后来处理需要序列化的内容
class Student(dict):
    def __init__(self):
        print(isinstance(self,dict))
        self["name"]="leo"
        self["age"]=23
    def say(self,txt):
        print(txt)

print(json.dumps(Student()))
Student().say("Hello World")
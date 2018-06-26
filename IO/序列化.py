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
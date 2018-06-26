from io import StringIO

f=StringIO()

f.write("hello")
f.write(" ")
f.write("world\n\n\n")
print(f.getvalue())

# 同时也可以使用字符创初始化一个 StringIO,然后像文件一样读取

f=StringIO("Hello!\nHi!\nGoodbye!")

print(f.read())

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

from io import BytesIO

f=BytesIO()

f.write("中文".encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()

# StringIO BytesIO 需要读写一致
# 通过 str      实例出来的对象  需要 read()
# 通过 write    方法写入的对象  需要 getvalue()

import os
import collections
import time

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)

# if isinstance(os.environ,collections.Iterable):
#     for item in os.environ:
#         # 要获取某个环境变量的值，可以调用os.environ.get('key')：
#         print(item+":"+ os.environ.get(item))
        
# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：


# 拼接路径
print(os.path.join(os.path.abspath("."),"testdir")) 
# 分割路径 + 文件
print(os.path.split('/Users/michael/testdir/file.txt'))
# 分割 路径后缀 + 后缀
print(os.path.splitext('/Users/michael/testdir/file.txt'))


try:
    path=os.path.join(os.path.join(os.path.abspath("."),"src"),str(int(time.time())))
    os.mkdir(path)
except expression as identifier:
    print("error")
finally:
    print("end")

# 修改文件名
# os.rename("./src/rename.rar","./src/rename1.rar")

# 利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
for dir in [x for x in os.listdir('.') if os.path.isdir(x)]:
    print(dir)

# 要列出所有的.markdown文件，也只需一行代码
for file in [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.markdown']:
    print(file)
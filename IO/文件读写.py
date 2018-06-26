


try:
    #  打开
    f = open('./src/index.txt',"r")
    # 读
    print(f.read())
except expression as identifier:
    print(identifier)
finally:
    if f:
        # 关
        f.close()

# 更简便的写法

# Python引入了with语句来自动帮我们调用close()方法：
with open('./src/index.txt',"r") as f:
    print(f.read())

#  调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
with open('./src/index.html',"r") as f:
    for item in f.readlines():
        print("leo:"+item.strip())

with open('./src/index.txt',"r") as f:
    txt = f.read(1)
    while len(txt):
        print(txt)
        txt = f.read(1)

import math

# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
with open('./src/index.png',"rb") as target:
    print(str(math.ceil(len(target.read())/1024))+"kb")

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
print(open('./src/gbk.txt','r',encoding="gbk",errors="ignore").read())
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
print(open('./src/gbk.txt','r',encoding="utf8",errors="ignore").read())


import time

# 写入
with open('./src/index.txt',"r+")  as target:
    s=target.read() + str(int(time.time()))
    target.write(s)

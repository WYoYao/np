l = list(range(0, 100))

#  截取前三个 如果是从 0 开始，0可以省略
print(l[0:3])

# 支持的负数倒取
print(l[-1])

print(l[-3:-1])

# 每n个取 1个
print(l[::5])

# 二次截取 下面两种方法相同
print(l[:10][::2])
print(l[:10:2])

# 字符串也算一个list 所以也可以进行切片

print("123456789"[::2])

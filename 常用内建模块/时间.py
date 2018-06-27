from datetime import datetime

# 获取当前时间
print(type(datetime.now()))
print(str(datetime.now()))

# 生成指定的时间
d = datetime(1993,10,20,1,20,20)

# 获取时间戳
print(int(d.timestamp()))

# 时间戳转换成为日期
print(datetime.fromtimestamp(d.timestamp()))

# str 转换为datetime
cday=datetime.strptime("2018/10/20","%Y/%m/%d")
print(cday)

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# datetime加减
from datetime import timedelta

now = datetime.now()
print(now)
now+=timedelta(hours=1,days=1)
print(now)
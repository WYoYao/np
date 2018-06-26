# 枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：

from enum import Enum, unique
import collections
import json

Month = Enum(
    "Monthaa",
    (
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ),
)

print(isinstance(Month, collections.Iterable))

for name, member in Month.__members__.items():
    print(name, "=>", member, ",", member.value)

print(Month.__members__.items())


@unique  # 装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Sat)
print(Weekday.Sat.value)

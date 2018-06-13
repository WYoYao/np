#coding=utf-8
def fn(x):
    if isinstance(x,(int,float)):
        return x+x
    else:
        raise TypeError('bad operand type') # 抛出错误


# 函数可以返回多个值

def move(x,y,step=0):
    nx=x+step
    ny=y-step
    return nx,ny

# 返回多个值的时候其实是返回一个tuple
print(isinstance(move(3,2,1),tuple))

# 传递多个参数
def calc(num1,num2,num3):
    return num1+num2+num3

print(calc(1,2,3))
print(calc(*[1,2,3]))
print(calc(*(1,2,3)))

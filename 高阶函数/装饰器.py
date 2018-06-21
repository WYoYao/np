import time
import functools

# 我们要增强函数的功能，
# 比如，在函数调用前后自动打印日志，但又不希望修改函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）


def log(text="暂无信息"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*argu, **kw):
            print(text)
            return func(*argu, **kw)

        return wrapper

    return decorator


@log("这次要打印时间")
def now():
    print(now.__name__)
    return time.time()


print(now())

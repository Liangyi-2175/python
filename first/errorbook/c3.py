# 装饰器
# 特性 注解
import time


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)

    return wrapper


@decorator
def f1(func_name):
    # print(int(time.time()))
    print("sssssss" + func_name)


@decorator
def f2(func_name1, func_name2):
    print("qqqqqqq" + func_name1)
    print("qqqqqqq" + func_name2)


@decorator
def f3(func_name1, func_name2, **kwargs):
    print("qqqqqqq" + func_name1)
    print("qqqqqqq" + func_name2)
    print(kwargs)


# f = decorator(f1)
f1('test')
f2('tt', 'yy')
f3('re', 'ty', a=32, b=56, c='123')

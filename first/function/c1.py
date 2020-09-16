# 匿名函数


def add(x, y):
    return x + y


print(add(1, 2))

f = lambda x, y: x + y

print(f(1, 2))
"""
lambada 表达式
lambda parameter_list:expression
三元表达式
x,y 是否大于y，如果是则返回x 否则返回y
x > y ? X : y
条件为真是返回的结果 if 条件判断  else 条件为假是返回的结果
x if x > y else y
"""



#闭包
def curve_pre():
    a = 25

    def curve(x):

        return a*x*x
    return curve
a = 10
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))


# def curve_pre1():
#     a = 25
#
#     def curve(x):
#
#         return a*x*x
#     return curve
# a = 10
# f = curve_pre1()
# print(f.__closure__)
# print(f.__closure__[0].cell_contents)
# print(f(2))

import re
s = 'A8C3721D86'
# 把所有s中大于6的换成9，小于6的换成0
def convert(value):
    matched = value.group()
    if int(matched)>6:
        return '9'
    else:
        return '0'
r = re.sub('\d', convert, s)
print(r)
#替换元素
# lanuage = 'PythonC#JavaC#PHPC#'
#
# def convert(value):
#     print(value)
#     matched = value.group()
#     print(matched)
#     return '!!'+matched+'!!'
#
# r = re.sub('C#', convert, lanuage,1)
#
# # lanuage=lanuage.replace('C#',convert,lanuage)
# print(r)

# #re.I 忽略大小写字母
# #re.S 如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始。
# # 而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，在整体中进行匹配。
# lanuage = """PythonC#
#     JavaPHP"""
# r = re.findall('c#.{1}', lanuage, re.I | re.S)
# print(r)
# #组
# a = 'PythonPythonPythonPythonPython'
# r = re.findall('(Python){3}', a)
# print(r)

#边界值匹配
# qq = '1000000001'
# r = re.findall('^100', qq)
# s = re.findall('0001$', qq)
# print(r)
# print(s)
# a = 'pytho0pythonpython1pythonn2'
# # *号匹配规则，匹配*号前的字符出现0次或者无限多次
# # +号匹配规则，匹配+号前的字符出现1次或者无限多次
# # ?号匹配规则，匹配?号前的字符出现0次或者1次
# r = re.findall('python?', a)
# print(r)

#正则表达式取反  ^
# s = 'abc,acc,adc,aec,afc,ahc'
# r = re.findall('a[^cf]c',s)
# print(r)


# a = 'C0C++1Java2C#3Python4  Javascript'
# r = re.findall('\S', a)
# print(r)



# a = 'C0C++1Java2C#3Python4Javascript'
# # r = re.findall('', a)
# # if len(r)>0:
# #     print('包含字符串包含的内容')
# # else:
# #     print('不包含')




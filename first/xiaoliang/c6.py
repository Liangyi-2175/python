import re
#获取life到python之间的元素
s = 'life is short,i use python'
r = re.search('life(.*)python', s)
print(r.group(1))
# s = 'Q82D3721D86'
# #match从字符的首个字符串开始匹配，匹配到第一个返回，如果没有匹配上就返回为空
# r = re.match('\d', s)
# #search从整个字符串中匹配，匹配到第一个后返回
# r1 = re.search('\d', s)
# #span() 返回匹配元素的位置
# print(r)
# print(r1.group())

# s = 'A8C3721D86'
# 把所有s中大于6的换成9，小于6的换成0
# def convert(value):
#     matched = value.group()
#     print(matched)
#     if int(matched)>6:
#         return '9'
#     else:
#         return '0'
# r = re.sub('\d', convert, s)
# print(r)

# #替换元素
# lanuage = 'PythonC#JavaC#PHPC#'
# r = re.sub('C#', 'Go', lanuage, 1)
# #lanuage = lanuage.replace('C#', 'Go')
# print(r)

# lanuage = """PythonC#
#     JavaPHP"""
# r = re.findall('c#.{0}', lanuage, re.I | re.S)
# print(r)
# qq = '1000000001'
# r = re.findall('^100*?', qq)
# s = re.findall('0001$', qq)
# print(r)
# print(s)
# import re
# a = 'pytho0pythonnpython1pythonn2'
# # *号匹配规则，匹配*号前的字符出现0次或者无限多次
# # +号匹配规则，匹配+号前的字符出现1次或者无限多次
# # ?号匹配规则，匹配?号前的字符出现0次或者1次
# r = re.findall('python?', a)
# print(r)

# a = 'python1111java&678php'
# #r = re.findall('[a-z]{-6}', a) #贪婪
# r = re.findall('[a-z]{3}', a)  #非贪婪
# print(r)


# s = 'abc,acc,adc,aec,afc,ahc'
# r = re.findall('a[c-f]c',s)
# print(r)

# a = 'C0C++1Java2C #3Python4Javascript'
# r = re.findall('\d', a)
# print(r)


# a = 'C|C++|Java|C#|Python|Javascript'
# r = re.findall('H', a, re.I) #在a里面查找是否包含‘C’
# if len(r) > 0:
#     print('包含字符串包含的内容:'+str(r))
# else:
#     print('不包含')

# example = "abbbbbbc"
# pattern = re.findall("ab?", example)
# # s = '1234567890'
# # r = re.search('^\d{1}$',s)
# print(pattern)
# # s = 'life is short,i use python'
# # r = re.search('life(.*)python',s)
# # print(r.group(0, 1))



# s = '82D3721D86'
# #match从字符的首个字符串开始匹配，匹配到第一个返回，如果没有匹配上就返回为空
# r = re.match('\d', s)
# #search从整个字符串中匹配，匹配到第一个后返回
# r1 = re.search('\d', s)
# #span() 返回匹配元素的位置
# print(r.span())
# print(r1.group())




# _notification_map = {"appliction": -1}
# notifications=[]
# for key in _notification_map:
#     notification_id = _notification_map[key]
#     print(notification_id)
#     notifications.append({
#         'namespaceName': key,
#         'notificationId': notification_id
#     })
# print(notifications)
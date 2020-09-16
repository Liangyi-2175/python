# import json
# import re
# json_str = '{"name": "Tom", "age": 18}'
# r = re.findall('')
# student = json.loads(json_str)
# print(type(student))
#print(type(json_str))


# json           python
# object         dict
# array          list
# string         str
# munber         int
# munber         float
# true           True
# false          False
# null           None
import json
#序列化  将字符串转转化成json对象的过程
#反序列化 json对象转化成字符串
student = [
    {"name": "Tom", "age": 18, "flag": False},
    {"name": "Tom", "age": 18}
    ]
json_str = json.dumps(student)
print(json_str)
print(type(json_str))
print(type(student))


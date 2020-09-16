​														***Json***
JSON 的载体：Json字符串
JSON是什么：Json是一个数据格式
Json.loads():将字符串转成json object           

```python
json中的类型对和python中对应的类型
json           python
object         dict
array          list
string         str
munber         int
munber         float
true           True
false          False
null           None
```

```python
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
>> [{"name": "Tom", "age": 18, "flag": false}, {"name": "Tom", "age": 18}]
>> <class 'str'>
>> <class 'list'>
```
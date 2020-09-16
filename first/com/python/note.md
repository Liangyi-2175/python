									   ***note***
***引号***
单引号：可以表示字符串，换行需要加入反斜杠\
双引号：如果字符串本身带有单引号，可以使用双引号
三引号：支持字符串换行

***转义字符***
1.特殊字符  无法"看见"的字符  与语言本身语法有冲突的字符
 \n  换行
 \'  单引号
 \t  横向制表符
 \r  回车
print()输出转义字符在转义字符前面再加一个\
r"字符串" :可以保持原生字符串

***字符运算***
1.两个字符串相加=两个字符串拼接
2.获取字符串中某一个元素 “hello”[0]="h".   "hello"[-1]="o"
3.字符串中空格也占用一个位置

***字符串切片***
"Hello world" [2:5]="llo"
"Hello world"[2:-1]='llo worl' 
"Hello world" [-5:]='world'
"Hello world" [-5:11]='world'
一个字符串里面存在多个相同元素，只替换其中一个元素：
value = "Hello world"
key = value.replace("l", "s", 1)
字符串元素不可变

​				

​									***基本数据类型***

***列表基本操作***
1.基本列表：[1,2,3,4,5,6]
2.列表里面可以包含任意类型，例如：["hello",1,4,True]
3.列表里面可以嵌套列表，例如：[[1,2],["hello","world"],[True]]
4.使用切片的方式获取列表：得到的结果还是一个列表，使用元素位置方式获取会得到一个字符串，
例如：[1,2,3,4,5,]\[1]=‘2’，[1,2,3,4,5]\[2:]=[3,4,5]
5.列表相加：[1,2,3]+[4,5]=[1,2,3,4,5]
6.列表相乘：[1,'无敌']*2=[1,'无敌',1,'无敌']
7.嵌套数组获取以及切片：
 		[['a','b','c'],[1,2,3],[2,1],['无敌',1]]\[1][2:]=[3]
		 [['a','b','c'],[1,2,3],[2,1],['无敌',1]]\[1][2]=3
		[['a','b','c'],[1,2,3],[2,1],['无敌',1]]\[1]=[1, 2, 3]
8.元素可变 例如：a=[1,2,3].     a.append(4).   a=[1,2,3,4]

***元组基本操作***
定义：(1,2,3,4,5)
操作：与列表字符串基本一致 
元素：元素不可变

***序列***
序列：Str list tuple
序号:序列里面每一个元素的位置
相同点：操作基本一致，全部是有序
切片：
3 in [1,2,3,4,5,6]=True
3 ont in [1,2,3,4,5,6]=False
长度：len([1,2,3,4,5,6])=6
最大值：max([1,2,3,4,5])=5
最小值：min([1,2,3,4,5])=1
算ASCll码方法 ord()

***集合***
1.无序，不能切片，没有索引，元素不可变
2.差集：可以求两个集合的差值  {1,2,3,4}-{2,3}={1,4}
3.交集：可以求两个集合相同的值 {1,2,3,4} &{2,4,5}={2,4}
4.合集：可以求两个集合之和(去重) {1,2,3,4,5} | {3,4,5,6,7}={1,2,3,4,5,6,7}

***字典***
1.键值对   key : value
2.无序
3.取值：{'a':'快乐','b':'开心'}['a']='快乐'
4.items() : 
		d={1:'a',2:'b',3:'c'}
		result=[]
		for key,vaule in d.items():
				result.append(key)
				result.append(value)
		print(result)
输出结果：[1,'a',2,'b',3,'c']

***变量***
1.命名：数字,字母,下划线。 区分大小写字母

***赋值运算符***

(a+1)= (a+=1)

***比较运算符***
1.==
2.!=
3.>
4.<
5.字符串比较：‘abc’>'bcd'. 从第一个元素ascll码相加比较直到比较出大小

***逻辑运算符***
And: 1 and 0  :1为真，0为假， and运算符其中一个为假就返回假，返回结果：0
		1 and 2 返回结果:1
		2 and 0 返回结果:0 
Or:   1 or 0  返回结果:1
		1 or 2 返回结果:1
		0 or 1 返回结果:1
		从第一个开始判断，遇到为真的就返回结果

***成员运算符***
1.判断a是否在列表中
	a=1
	a in [1,2,3,4]
	返回结果：True
2.判断b不在列表中
	b=8
	b not in [1,2,3,4,5]
	返回结果：True

***身份运算符***
1.is ==
2.is ont  !=

***位运算符***
1.&按位与： a=2,b=3 a&b=2 原理:2和3转换成二进制分别是10，11，每个位置上面的元素对比，如果都是1的返回1，都是0或者其中一个是0则返回0，所以10和11对比结果位10，转化10进制之后就是2
2.|按位或: a=2,b=3 a&b=2 原理:2和3转换成二进制分别是10，11，每个位置上面的元素对比，如果其中一个是1的返回1，都是0则返回0，所以10和11对比结果位11，转化10进制之后就是3
3.^按位异或
4.～按位去反
5.<<左位移
6.>>右位移

​								***分支 循环 条件与枚举***

***循环***

1. while

   ```python
   CONDITION = 1
   while CONDITION <= 10:
       CONDITION += 1
       #代码块
       print(CONDITION)
   else:
       print('erroy')
   ```

2.for #主要用来遍历/循环 序列或者集合 字典

```python
a = [['aaple','orange','banana','grape'],(1,2,3)]
for x in a:
    for k in x:
        print(k,)
else:
    print('fruit is gone')
```

​	输出：aaple||orange||banana||grape||1||2||3||fruit is gone   ===》end='||':结尾使	用"||"替换

​	break: 跳出循环

```python
# a = [1,2,3]
# for x in a:
#     if x==2:
#         break
#     print(x)
```

​	输出：1

​	continue：跳出指定循环

```python
a = [1,2,3]
for x in a:
    if x==2:
        continue
    print(x)
```

​	输出：1 ，3

切片取值

```python
a=[1,2,3,4,5,6,7,8]
b=a[0:len(a):2]
print(b)
```

​	输出：[1, 3, 5, 7]

***生成器***
list = [x*x for x in range(10)]
print(list)
generator_ex = (x*x for x in range(10))
b = []
for i in range(8):
 c = next(generator_ex)
 b.append(c)
print(b)

***打印佩波那契数列***
def fib(s):
 n, a, b = 0, 0, 1
 while n < s:
   a, b = b, a+b
   n += 1
   print(a)
print(fib(10))

**导入函数 \__all__\**
C7.py :
 __all__=['a','c']
a=2
c=3
d=4

C8.py:
from C7 import *
print(a)
print(c)
print(d)
输出：2   3。输出d的时候报错因为d没有没引入

***面向对象的三大特性***

1.继承

```python
class Human():
    sum=0

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getname(self):
        print(self.name)
```

```python
from c3 import Human


class Student(Human):

    def __init__(self, school, name, age):
        self.school = school
        #super 继承父类
        super(Student, self).__init__(name, age)
        # Human.__init__(self, name, age)

    def do_homework(self):
        super(Student, self).do_homework()
        print('end...')

student = Student('永济中学', '张飞', 18)
student.do_homework()
```

输出：
张飞
18

*args,**kwargs 用法

```python
def testao(*args,**kwargs):
    return args, kwargs

test=testao(5,9,5,6,7,a=4,b=5)
print(test)
```

输出：((5, 9, 5, 6, 7), {'a': 4, 'b': 5})


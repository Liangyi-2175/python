from c3 import Human


class Student(Human):

    def __init__(self, school, name, age):
        self.school = school
        print("ssss")
        #super 继承父类
        super(Student, self).__init__(name, age)
        # Human.__init__(self, name, age)

    def do_homework(self):
        super(Student, self).do_homework()
        print('end...')

student = Student('永济中学', '张飞', 18)
student.do_homework()
# Student('永济中学', '张飞', 18).do_homework()
# print(student.sum)
# print(student.name)
# student.do_homework()
# print(student.age)
# print(Student.sum)
# student.getname()
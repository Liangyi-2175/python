

class Student():

    sum1 = 0

    def __init__(self, name1, age):
        self.name = name1
        self.age = age
        self.__score = 0
        self.__class__.sum1 += 1
        # print(str(self.__class__.sum1))
        # print(name1)

    def test01(self, man, min):

        return min+man

    def marking(self, score):
        if score < 0:
            return '不能小于0'
        self.__score = score
        print(self.name+'的分数'+str(self.score))


    @classmethod
    def puls_sum1(cls):
        cls.sum1 += 1
        print(cls.sum1)

    @staticmethod
    def add(x):
        print(Student.sum1)

student = Student('张飞', 3)
# student.__score=-1
# print(student.__dict__)
# student.marking(9)

# student.puls_sum1()
# Student.puls_sum1()
# print(student.test01())
# print(Student(6,6).test01(9,9))
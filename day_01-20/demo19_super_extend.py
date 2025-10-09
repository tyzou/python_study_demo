# 继承和多态
class Person:
    """ 人 """
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭。')

    def sleep(self):
        print(f'{self.name}正在睡觉。')

class Student(Person):
    """ 学生 """
    def __init__(self,name,age):
        super().__init__(name,age)

    def study(self,course_name):
        print(f'{self.name}正在学习{course_name}')

class Teacher(Person):
    """老师"""

    def __init__(self,name,age,title):
        super().__init__(name,age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')


if __name__ == '__main__':
    stu1 = Student('白元芳', 21)
    stu2 = Student('狄仁杰', 22)
    tea1 = Teacher('武则天', 35, '副教授')
    stu1.eat()
    stu2.sleep()
    tea1.eat()
    stu1.study('Python程序设计')
    tea1.teach('Python程序设计')
    stu2.study('数据科学导论')



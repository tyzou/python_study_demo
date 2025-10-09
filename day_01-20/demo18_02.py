# 初始化方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print(f"{self.name}正在学习{course_name}")
    def play(self):
        print(f"{self.name}玩游戏")


stu1 = Student("张三",14)
stu2 = Student("李四",20)

stu1.study("java开发")
stu2.play()


# 创建对象
class Student:
    def study(self,course_name):
        print(f"学生正在学习{course_name}")
    def play(self):
        print("玩游戏")

stu1 = Student()
stu2 = Student()
print(stu1,stu2)
print(hex(id(stu1)), hex(id(stu2)))

Student.study(stu1,"Python程序设计")

stu1.study('Python程序设计')

Student.play(stu2)
stu2.play()


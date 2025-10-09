class Student:
    def __init__(self,name,age):
        # `__name`表示一个私有属性，`_name`表示一个受保护属性
        self.__name = name
        self.__age = age

    def study(self,course_name):
        print(f"{self.__name}正在学习{course_name}")

stu = Student("张三",20)
stu.study("python开发")
# Python 语言并没有从语义上做出最严格的限定
print(stu._Student__name)
# 报错：AttributeError: 'Student' object has no attribute '__name'
print(stu.__name)

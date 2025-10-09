# 动态为对象添加属性
class Student:
    def __init__(self,name,age):
        # `__name`表示一个私有属性，`_name`表示一个受保护属性
        self.__name = name
        self.__age = age


stu = Student("张三",20)
# 给学生对象动态添加sex属性
stu.sex = "女";

print(stu.sex)
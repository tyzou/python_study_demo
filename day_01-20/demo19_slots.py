class Student:
    # 限制实例只能有这2个属性
    __slots__ = ('name','age')

    def __init__(self,name,age):
        self.name = name
        self.age = age

stu = Student('王大锤', 20)
# 因为slots限制了只能有两个属性，所以这里会报错AttributeError
stu.sex = '男'


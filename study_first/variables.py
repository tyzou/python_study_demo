#2. 变量和数据类型
name = "John"
age = 25
height = 1.75
is_student = True

print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"身高：{height}")
print(f"是否是学生：{is_student}")

# 查看变量的类型
print(f"name的类型是:{type(name)}")
print(f"age的类型是:{type(age)}")
print(f"height的类型是:{type(height)}")
print(f"is_student的类型是:{type(is_student)}")
print(type(name))

# 判断两个变量的类型是否相同
print("\n判断变量类型是否相同的示例：")
# 使用type()函数直接比较
print(f"name和age的类型是否相同：{type(name) == type(age)}")
print(f"age和height的类型是否相同：{type(age) == type(height)}")

# 使用isinstance()函数判断
print("\n使用isinstance()函数判断类型：")
print(f"name是否为字符串类型：{isinstance(name, str)}")
print(f"age是否为整数类型：{isinstance(age, int)}")
print(f"height是否为浮点数类型：{isinstance(height, float)}")
print(f"is_student是否为布尔类型：{isinstance(is_student, bool)}")

# 多类型判断示例
print("\n判断变量是否为多种类型之一：")
# isinstance可以判断多个类型，如果是其中任意一个都返回True
print(f"age是否为整数或浮点数：{isinstance(age, (int, float))}")
print(f"height是否为整数或浮点数：{isinstance(height, (int, float))}")
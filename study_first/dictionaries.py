student = {
    "name" : "邹先生",
    "age" : 20,
    "majoir" : "计算机",
    "grades" : {"数学": 90, "英语": 85, "编程": 95}
}

# 访问字典元素
print(f"学生姓名：{student['name']}")
print(f"年龄：{student['age']}")
print(f"数学成绩：{student['grades']['数学']}")


# 添加或者修改元素
student['phone'] = '18312341234'
student['age'] = 22
print(f'更新后的信息{student}')


# 遍历字典
print('\n遍历字典')
for key,value in student.items() : 
    if key != "grands":
        print(f"key:{key} value:{value}")


for key,value in student["grades"].items():
    print(f"key={key}    value={value}" )


json_array = [
    {"name": "apple", "color": "red"},
    {"name": "banana", "color": "yellow"},
    {"name": "cherry", "color": "red"}
]
for item in json_array:
    print(f"name:{item['name']}    color:{item['color']}")
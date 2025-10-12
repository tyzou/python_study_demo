"""
使用变量保存数据并进行加减乘除运算
"""
a = 45  # 定义变量a，赋值45
b = 12  # 定义变量b，赋值12
print(a, b)  # 45 12
print(a + b)  # 57
print(a - b)  # 33
print(a * b)  # 540
print(a / b)  # 3.75

"""
使用type函数检查变量的类型
"""
a = 100
b = 123.45
c = 'hello, world'
d = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>

"""
变量的类型转换操作
"""
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))  # 100.0
print(int(b))  # 123
print(int(c))  # 123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))  # str类型的100按二进制转成int，输出4
print(float(e))  # 123.45
print(bool(f))  # str类型的'hello, world'转成bool，输出True
print(int(g))  # bool类型的True转成int,输出1
print(chr(a))  # int类型的100转成str，输出'd'
print(ord('d'))  # str类型的'd'转成int，输出100

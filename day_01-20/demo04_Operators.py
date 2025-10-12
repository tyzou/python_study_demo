"""
算术运算符
"""
print('\n============== 算术运算符 =================')
print(321 + 12)  # 加法运算，输出333
print(321 - 12)  # 减法运算，输出309
print(321 * 12)  # 乘法运算，输出3852
print(321 / 12)  # 除法运算，输出26.75
print(321 // 12)  # 整除运算，输出26
print(321 % 12)  # 求模运算，输出9
print(321 ** 12)  # 求幂运算，输出1196906950228928915420617322241

"""
算术运算的优先级
"""
print('\n============== 算术运算的优先级 =================')
print(2 + 3 * 5)  # 17
print((2 + 3) * 5)  # 25
print((2 + 3) * 5 ** 2)  # 125
print(((2 + 3) * 5) ** 2)  # 625

print('\n============== 赋值运算符和复合赋值运算符 =================')
a = 10
b = 3
a += b  # 相当于：a = a + b
a *= a + 2  # 相当于：a = a * (a + 2)
print(a)

"""
海象运算符: 作用是在表达式中同时完成赋值和返回值
这里的a := 10做了两件事：1、把 10 赋值给变量a   2、同时返回 10 这个值
"""
print('\n============== 海象运算符 =================')
print((a := 10))  # 10
print(a)  # 10

print('\n============== 比较运算符和逻辑运算符的使用 =================')
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print(f'flag0: {flag0}')
print(f'flag1: {flag1}')
print(f'flag2: {flag2}')
print(f'flag3: {flag3}')
print(f'flag4: {flag4}')
print(f'flag5: {flag5}')

print('\n============== 将华氏温度转换为摄氏温度 =================')
f = 100.0
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

print('\n============== 计算圆的周长和面积 =================')
# radius = float(input('请输入圆的半径: '))
radius = 100
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)

print('\n============== 输入半径计算圆的周长和面积 =================')
import math

# radius = float(input('请输入⚪的半径：'))
radius = 100
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'{perimeter = :.2f}')
print(f'{area = :.2f}')


print('\n============== 输入年份，闰年输出True，平年输出False =================')
# year = int(input('请输入年份: '))
year = 2025
is_leap = year % 4 ==0 and year % 100 !=0 or year % 400 == 0
print(f'是否是闰年：{is_leap=}')



from math import factorial as f
from random import randrange


class Demo001:

    @staticmethod
    def demo1():
        print('----------------demo-------------------')

        # 通过关键字def定义求阶乘的函数
        # 自变量（参数）num是一个非负整数
        # 因变量（返回值）是num的阶乘
        def fac(num):
            result = 1
            for n in range(2, num + 1):
                result *= n
            return result

        m = int(input('m = '))
        n = int(input('n = '))
        # 计算阶乘的时候不需要写重复的代码而是直接调用函数
        # 调用函数的语法是在函数名后面跟上圆括号并传入参数
        print(fac(m) // fac(n) // fac(m - n))

    @staticmethod
    def demo2():
        print('----------------输入m和n，计算组合数C(m,n)的值-------------------')
        m = int(input('m = '))
        n = int(input('n = '))
        print(f(m) // f(n) // f(m - n))

    @staticmethod
    def demo3():
        print('----------------位置参数和关键字参数-------------------')

        def make_judgement(a, b, c):
            """判断三条边的长度能否构成三角形"""
            return a + b > c and b + c > a and a + c > b

        print(make_judgement(1, 2, 3))  # False
        print(make_judgement(4, 5, 6))  # True
        # 使用关键字参数，通过“参数名=参数值”的形式为函数传入参数
        print(make_judgement(b=2, c=3, a=1))  # False
        print(make_judgement(c=6, b=4, a=5))  # True

        print('----------------强制位置参数-------------------')

        # 用`/`设置**强制位置参数**（*positional-only arguments*），用`*`设置**命名关键字参数**。
        # 所谓强制位置参数，就是调用函数时只能按照参数位置来接收参数值的参数；
        # 而命名关键字参数只能通过“参数名=参数值”的方式来传递和接收参数

        def make_judgement2(a, b, c, /):
            """判断三条边的长度能否构成三角形"""
            return a + b > c and b + c > a and a + c > b

        # print(make_judgement2(b=2, c=3, a=1)) # 报错：TypeError

        def make_judgement3(*, a, b, c):
            """用`*`设置**命名关键字参数**"""
            return a + b > c and b + c > a and a + c > b

    @staticmethod
    def demo4():
        print('----------------参数的默认值-------------------')

        # 定义摇色子的函数
        # 函数的自变量（参数）n表示色子的个数，默认值为2
        # 函数的因变量（返回值）表示摇n颗色子得到的点数
        def roll_dice(n=2):
            total = 0
            for _ in range(n):
                total += randrange(1, 7)
            return total

        # 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
        print(roll_dice())
        # 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
        print(roll_dice(3))

        def add(a=0, b=0, c=0):
            """三个数相加求和"""
            return a + b + c

        # 调用add函数，没有传入参数，那么a、b、c都使用默认值0
        print(add())  # 0
        # 调用add函数，传入一个参数，该参数赋值给变量a, 变量b和c使用默认值0
        print(add(1))  # 1
        # 调用add函数，传入两个参数，分别赋值给变量a和b，变量c使用默认值0
        print(add(1, 2))  # 3
        # 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
        print(add(1, 2, 3))  # 6

    @staticmethod
    def demo5():
        print('----------------可变参数-------------------')

        # 用星号表达式来表示args可以接收0个或任意多个参数
        # 调用函数时传入的n个参数会组装成一个n元组赋给args
        # 如果一个参数都没有传入，那么args会是一个空元组
        def add(*args):
            total = 0
            for val in args:
                if type(val) in (int, float):
                    total += val
            return total

        print(add())
        print(add(1))
        print(add(1, 2, 3))
        print(add(1, 2, 'hello', 3.45, 6))

        # 参数列表中的**kwargs可以接收0个或任意多个关键字参数
        # 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
        # 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
        def foo(*args, **kwargs):
            print('args : ',args)
            print('kwargs : ',kwargs)

        foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)
        foo(name='骆昊', age=43, gpa=4.95)

    @staticmethod
    def demo6():
        print('----------------用模块管理函数-------------------')
        def foo():
            print('hello, world!')

        def foo():
            print('goodbye, world!')
        foo() # goodbye, world!


if __name__ == '__main__':
    # Demo001.demo1()
    # Demo001.demo2()
    Demo001.demo3()
    Demo001.demo4()
    Demo001.demo5()
    Demo001.demo6()

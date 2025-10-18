import functools
import operator

class Demo16:
    """
    函数使用进阶
    """

    @staticmethod
    def demo1():
        print('----------------高阶函数-------------------')
        def calc(*args,**kwargs):
            items = list(args) + list(kwargs.values())
            result = 0
            for item in items:
                if type(item) in (int, float):
                    result += item
            return result

        def is_even(num):
            """判断num是不是偶数"""
            return num % 2 == 0

        def square(num):
            """求平方"""
            return num ** 2

        old_nums = [35, 12, 8, 99, 60, 52]
        # `filter`和`map`函数就是高阶函数，前者可以实现对序列中元素的过滤，后者可以实现对序列中元素的映射
        new_nums = list(map(square, filter(is_even, old_nums)))
        print(new_nums)  # [144, 64, 3600, 2704]

        old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
        new_strings = sorted(old_strings)
        print(new_strings)  # ['apple', 'in', 'pear', waxberry', 'zoo']

        new_strings = sorted(old_strings, key=len)
        print(new_strings)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']




    @staticmethod
    def demo2():
        print('----------------Lambda函数-------------------')
        old_nums = [35, 12, 8, 99, 60, 52]
        new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
        print(new_nums)  # [144, 64, 3600, 2704]

        # 用一行代码实现计算阶乘的函数
        fac = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)
        # 用一行代码实现判断素数的函数
        is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))
        # 调用Lambda函数
        print(fac(6))  # 720
        print(is_prime(37))  # True


    @staticmethod
    def demo3():
        """
        偏函数是指固定函数的某些参数，生成一个新的函数，这样就无需在每次调用函数时都传递相同的参数。
        在 Python 语言中，我们可以使用`functools`模块的`partial`函数来创建偏函数。
        例如，`int`函数在默认情况下可以将字符串视为十进制整数进行类型转换，如果我们修修改它的`base`参数，
        就可以定义出三个新函数，分别用于将二进制、八进制、十六进制字符串转换为整数，代码如下所示。
        :return:
        """
        print('----------------偏函数-------------------')
        int2 = functools.partial(int, base=2)
        int8 = functools.partial(int, base=8)
        int16 = functools.partial(int, base=16)

        print(int('1001'))  # 1001
        print(int2('1001'))  # 9
        print(int8('1001'))  # 513
        print(int16('1001'))  # 4097







if __name__ == '__main__':
    Demo16.demo1()
    Demo16.demo2()
    Demo16.demo3()
    Demo16.demo4()
    Demo16.demo5()
    Demo16.demo6()

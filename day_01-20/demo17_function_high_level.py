import random
import time
from functools import wraps
from functools import lru_cache


class Demo17:
    """
    函数高级应用
    """

    @staticmethod
    def demo1():
        print('----------------装饰器-------------------')
        """下载文件"""

        def download(filename):
            """下载文件"""
            print(f'开始下载《{filename}》.')
            time.sleep(random.random() * 6)
            print(f'《{filename}》下载完成.')

        def upload(filename):
            """上传文件"""
            print(f'开始上传《{filename}》.')
            time.sleep(random.random() * 8)
            print(f'《{filename}》上传完成.')

        # download('MySQL从删库到跑路.avi')
        # upload('Python从入门到住院.pdf')

        def record_time(func):
            def wrapper(*args, **kwargs):
                # 在执行被装饰的函数之前记录开始时间
                start = time.time()
                # 执行被装饰的函数并获取返回值
                result = func(*args, **kwargs)
                # 在执行被装饰的函数之后记录结束时间
                end = time.time()
                # 计算和显示被装饰函数的执行时间
                print(f'{func.__name__}执行时间: {end - start:.2f}秒')
                # 返回被装饰函数的返回值
                return result

            return wrapper

        download = record_time(download)
        upload = record_time(upload)
        download('MySQL从删库到跑路.avi')
        upload('Python从入门到住院.pdf')

    @staticmethod
    def demo2():
        print('----------------装饰器函数-------------------')

        def record_time(func):
            def wrapper(*args, **kwargs):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                print(f'{func.__name__}执行时间: {end - start:.2f}秒')
                return result

            return wrapper

        @record_time
        def download(filename):
            print(f'开始下载{filename}.')
            time.sleep(random.random() * 6)
            print(f'{filename}下载完成.')

        @record_time
        def upload(filename):
            print(f'开始上传{filename}.')
            time.sleep(random.random() * 8)
            print(f'{filename}上传完成.')

        download('MySQL从删库到跑路.avi')
        upload('Python从入门到住院.pdf')

    @staticmethod
    def demo3():
        """
        可以通过被装饰函数的`__wrapped__`属性获得被装饰之前的函数
        """
        print('----------------demo-------------------')

        def record_time(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                print(f'{func.__name__}执行时间：{end - start:.2f}秒')
                return result

            return wrapper

        @record_time
        def download(filename):
            print(f'开始下载{filename}.')
            time.sleep(random.random() * 6)
            print(f'{filename}下载完成.')

        @record_time
        def upload(filename):
            print(f'开始上传{filename}.')
            time.sleep(random.random() * 8)
            print(f'{filename}上传完成.')

        # 调用装饰后的函数会记录执行时间
        download('MySQL从删库到跑路.avi')
        upload('Python从入门到住院.pdf')
        # 取消装饰器的作用不记录执行时间
        download.__wrapped__('MySQL必知必会.pdf')
        upload.__wrapped__('Python从新手到大师.pdf')

    @staticmethod
    def demo4():
        print('----------------递归调用-------------------')

        def fac(num):
            if num in (0, 1):
                return 1
            return num * fac(num - 1)

        print(fac(5))  # 120

        def fib1(n):
            if n in (1, 2):
                return 1
            return fib1(n - 1) + fib1(n - 2)

        for i in range(1, 21):
            print(fib1(i))

        def fib2(n):
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b
            return a

    @staticmethod
    def demo5():
        print('----------------优化上面的递归代码-------------------')

        @lru_cache()  # 装饰函数
        def factorial(n):
            print(f"计算 {n}!")  # 用于观察是否重复计算
            if n <= 1:
                return 1
            return n * factorial(n - 1)

        # 第一次调用：会计算并缓存
        print('第一次调用：', factorial(5))  # 输出：120（过程会打印计算5!、4!、3!、2!、1!）

        # 第二次调用：直接使用缓存，不重复计算
        print('第二次调用：', factorial(5))  # 输出：120（无打印，直接返回结果）


if __name__ == '__main__':
    # Demo17.demo1()
    # Demo17.demo2()
    # Demo17.demo3()
    # Demo17.demo4()
    Demo17.demo5()
    Demo17.demo6()

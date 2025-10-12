import time


class Demo06:

    @staticmethod
    def demo1():
        print('每隔1秒输出一次“hello, world”，持续5秒')
        for i in range(5):
            print('hello world')
            time.sleep(1)

    @staticmethod
    def demo2():
        """从1到100的偶数求和"""
        total = 0
        for i in range(1, 101):
            if i % 2 == 0:
                total += i
        print(total)

    @staticmethod
    def demo3():
        """从1到100的偶数求和(将起始值和跨度修改为2)"""
        total = 0
        for i in range(2, 101, 2):
            total += i
        print(total)  # 输出2550

    @staticmethod
    def demo4():
        print('使用 Python 内置的`sum`函数求和')
        print(sum(range(2, 101, 2)))  # 输出2550

    @staticmethod
    def demo5():
        print('while循环 >>> 从1到100的整数求和')
        total = 0
        i = 1
        while i <= 100:
            total += i
            i += 1
        print(total)

    @staticmethod
    def demo6():
        print('while循环 >>> 从1到100的偶数求和')
        total = 0
        i = 1
        while i <= 100:
            total += i
            i += 2
        print(total)

    @staticmethod
    def demo7():
        print('while循环 >>> break >>>> 从1到100的偶数求和')
        total = 0
        i = 2
        while True:
            total += i
            i += 2
            if i > 100:
                break
        print(total)

    @staticmethod
    def demo8():
        print('while循环 >>> continue >>>> 从1到100的偶数求和')
        total = 0
        for i in range(1, 101):
            if i % 2 != 0:
                continue
            total += i
        print(total)

    @staticmethod
    def demo9():
        print("for循环 >>> 打印乘法口诀表")
        for i in range(1, 10):
            for j in range(1, i + 1):
                print(f'{i} x {j} = {i * j}', end='\t')
            print()

    @staticmethod
    def demo10():
        print("输入一个大于 1 的正整数，判断它是不是素数。")
        num = int(input('请输入一个正整数:'))
        end = int(num ** 0.5)
        is_prime = True
        for i in range(2, end + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f'{num}是素数')
        else:
            print(f'{num}不是素数')

    @staticmethod
    def demo11():
        x = int(input('x = '))
        y = int(input('y = '))
        for i in range(x, 0, -1):
            if x % i == 0 and y % i == 0:
                print(f'最大公约数: {i}')
                break

if __name__ == '__main__':
    # Demo06.demo1()
    # Demo06.demo2()
    # Demo06.demo3()
    # Demo06.demo4()
    # Demo06.demo5()
    # Demo06.demo6()
    # Demo06.demo7()
    # Demo06.demo8()
    # Demo06.demo9()
    # Demo06.demo10()
    Demo06.demo11()

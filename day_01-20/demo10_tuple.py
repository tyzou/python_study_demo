import timeit

class Demo10:
    """元组（tuple）"""

    @staticmethod
    def demo1():
        # 定义一个三元组
        t1 = (35, 12, 98)
        t2 = ('邹哥', 45, True, '四川成都')
        print('查看变量的类型', type(t1))
        print('查看元组中元素的数量', len(t1))
        print('查看t1中0号下标的元素值：', t1[0])
        print('查看t2最后一个元素的值：', t2[-1])
        print('切片运算[start:end:stride]（终止位置的元素无法访问）:', t2[:2])
        print('切片运算[start:end:stride]（终止位置的元素无法访问）:', t2[::2])
        for elem in t1:
            print('for遍历：', elem)
        print('成员运算(in)：', 12 in t1)
        print('成员运算(in)：', 22 in t1)
        print('成员运算(not in)：', '邹哥' not in t2)
        print('拼接运算(合并一个新的数组)：', t1 + t2)
        print('比较运算:', t1 == t2)
        print('比较运算:', t1 == (35, 12, 98))

    @staticmethod
    def demo2():
        """一个元组中如果有两个元素，我们就称之为二元组；一个元组中如果五个元素，我们就称之为五元组。
        需要提醒大家注意的是，`()`表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则`()`就不是代表元组的字面量语法，
        而是改变运算优先级的圆括号，所以`('hello', )`和`(100, )`才是一元组，
        而`('hello')`和`(100)`只是字符串和整数。我们可以通过下面的代码来加以验证。"""
        a = ()
        print(' a = (): ', type(a))  # <class 'tuple'>
        b = ('hello')
        print("('hello'): ", type(b))  # <class 'str'>
        c = (100)
        print(type(c))  # <class 'int'>
        d = ('hello',)
        print(type(d))  # <class 'tuple'>
        e = (100,)
        print(type(e))  # <class 'tuple'>

    @staticmethod
    def demo3():
        print("打包和解包操作")
        # 打包操作
        a = 1, 10, 100
        print(type(a))
        # 解包操作
        i, j, k = a
        print(i, j, k)

        # 在解包时，如果解包出来的元素个数和变量个数不对应，
        # 会引发`ValueError`异常，错误信息为：`too many values to unpack`（解包的值太多）
        # 或`not enough values to unpack`（解包的值不足）。
        a = 1, 10, 100, 1000
        # i, j, k = a             # ValueError: too many values to unpack (expected 3)
        # i, j, k, l, m, n = a    # ValueError: not enough values to unpack (expected 6, got 4)

    @staticmethod
    def demo4():
        """有一种解决变量个数少于元素的个数方法，就是使用星号表达式。"""
        a = 1, 10, 100, 1000
        i, j, *k = a
        print(i, j, k)  # 1 10 [100, 1000]
        i, *j, k = a
        print(i, j, k)  # 1 [10, 100] 1000
        *i, j, k = a
        print(i, j, k)  # [1, 10] 100 1000
        *i, j = a
        print(i, j)  # [1, 10, 100] 1000
        i, *j = a
        print(i, j)  # 1 [10, 100, 1000]
        i, j, k, *l = a
        print(i, j, k, l)  # 1 10 100 [1000]
        i, j, k, l, *m = a
        print(i, j, k, l, m)  # 1 10 100 1000 []

        a, b, *c = range(1, 10)
        print(a, b, c) # 1 2 [3, 4, 5, 6, 7, 8, 9]
        a, b, c = [1, 10, 100]
        print(a, b, c)
        a, *b, c = 'hello'
        print(a, b, c)

    @staticmethod
    def demo5():
        """交换变量的值"""
        a,b = 1,2
        a,b = b,a
        print(a,b)

    @staticmethod
    def demo6():
        """  元组和列表的比较
        使用`timeit`模块的`timeit`函数来看看创建保存相同元素的元组和列表各自花费的时间，`timeit`函数
        的`number`参数表示代码执行的次数。  下面的代码中，我们分别创建了保存`1`到`9`的整数的列表和元组，
        每个操作执行`10000000`次，统计运行时间。
        """
        print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
        print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))
    @staticmethod
    def demo7():
        infos = ('骆昊', 43, True, '四川成都')
        # 将元组转换成列表
        print(list(infos))  # ['骆昊', 43, True, '四川成都']
        frts = ['apple', 'banana', 'orange']
        print(tuple(frts))


if __name__ == '__main__':
    # Demo10.demo1()
    # Demo10.demo2()
    # Demo10.demo3()
    # Demo10.demo4()
    # Demo10.demo5()
    # Demo10.demo6()
    Demo10.demo7()

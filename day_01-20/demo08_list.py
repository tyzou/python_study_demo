class Demo08:

    @staticmethod
    def demo1():
        print("创建列表")
        items1 = [35, 12, 99, 68, 55, 35, 87]
        items2 = ['Python', 'Java', 'Go', 'Kotlin']
        items3 = [100, 12.3, 'Python', True]
        print(items1)
        print(items2)
        print(items3)

    @staticmethod
    def demo2():
        print("创建列表")
        items4 = list(range(1, 10))
        items5 = list('hello')
        print(items4)
        print(items5)

    @staticmethod
    def demo3():
        print('列表的运算')
        items5 = [35, 12, 99, 45, 66]
        items6 = [45, 58, 29]
        items7 = ['Python', 'Java', 'JavaScript']
        print(items5 + items6)
        print(items6 + items7)
        items5 += items6
        print(items5)
        print('使用`*`运算符实现列表的重复运算:', items6 * 3)
        print('使用`*`运算符实现列表的重复运算:', items7 * 2)
        print('使用`in`或`not in`运算符判断一个元素在不在列表中:', 29 in items6)
        print('使用`in`或`not in`运算符判断一个元素在不在列表中:', 99 in items6)
        print('使用`in`或`not in`运算符判断一个元素在不在列表中:', 'C++' not in items7)
        print('使用`in`或`not in`运算符判断一个元素在不在列表中:', 'Python' not in items7)

    @staticmethod
    def demo4():
        print('\n使用`[]`运算符，通过在`[]`中指定元素的位置来访问该元素')
        items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
        print(items8[1])
        items8[2] = 'durian'
        print('当前队列值：', items8)
        print('访问倒数第5个：', items8[-5])
        print('访问倒数第2个：', items8[-2])
        items8[-4] = 'strawberry'
        print('替换倒数第四个后，当前队列值：', items8)

    @staticmethod
    def demo5():
        """
        切片运算是形如`[start:end:stride]`的运算符，其中`start`代表访问列表元素的起始位置，
        `end`代表访问列表元素的终止位置（终止位置的元素无法访问），而`stride`则代表了跨度，
        简单的说就是位置的增量，
        """
        items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
        print(items8[0: 3: 2])


if __name__ == '__main__':
    # Demo08.demo1()
    # Demo08.demo2()
    # Demo08.demo3()
    # Demo08.demo4()
    Demo08.demo5()

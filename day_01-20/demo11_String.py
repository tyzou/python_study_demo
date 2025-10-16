class Demo001:
    """ 字符串的定义: 所谓字符串，就是由零个或多个字符组成的有限序列 """

    def demo1(self):
        s1 = 'hello, world!'
        s2 = "你好，世界！❤️"
        s3 = '''
        hello,
        wonderful
        world!
        '''
        print(s1)
        print(s2)
        print(s3)

    def demo2(self):
        # 转义字符
        print()
        s1 = '\'HELLO,WORLD\''
        s2 = '\\HELLO,WORLD\\'
        print(s1)
        print(s2)

        s3 = '\time \to \read \now'
        s4 = r'\it \is \time \to \read \now'
        print(s3)
        print(s4)

        print('字符的特殊表示')
        s5 = '\141\142\143   \x61\x62\x63'  # 前者是八进制的表示法，后者是十六进制的表示法
        s6 = '\u9a86\u660a'  # Unicode 字符编码
        print(s5)
        print(s6)

    def demo3(self):
        print('----------------------拼接和重复------------------')
        s1 = 'hello' + ', ' + 'world'
        print(s1)  # hello, world

        s2 = '!' * 3
        print(s2)  # !!!

        s1 += s2
        print(s1)  # hello, world!!!

        s1 *= 2
        print(s1)  # hello, world!!!hello, world!!!

    def demo4(self):
        """
        对于两个字符串类型的变量，可以直接使用比较运算符来判断两个字符串的相等性或比较大小。
        需要说明的是，因为字符串在计算机内存中也是以二进制形式存在的，那么字符串的大小比较比的是每个字符对应的编码的大小。
        例如`A`的编码是`65`， 而`a`的编码是`97`，所以`'A' < 'a'`的结果相当于就是`65 < 97`的结果
        """
        print("------------------- 比较运算 ----------------------")
        s1 = 'a whole new world'
        s2 = 'hello world'
        print(s1 == s2)
        print(s1 < s2)
        print(s1 == 'hello world')
        print(s2 == 'hello world')
        print(s2 != 'hello world')

        # 通过ord获取编码
        print(ord('邹'))  # 37049
        print(ord('哥'))  # 21733
        print(ord('邹'))  # 37049
        print(ord('名'))  # 21517

        print('邹哥' < '邹名')
        print('邹哥' > '邹名')  # 左转紧，右转松

    def demo5(self):
        """
            切片运算是形如`[start:end:stride]`的运算符，其中`start`代表访问列表元素的起始位置，
            `end`代表访问列表元素的终止位置（终止位置的元素无法访问），而`stride`则代表了跨度，
            简单的说就是位置的增量
        """
        print('--------------获取字符串长度------------')
        s = 'hello, world'
        print(len(s))
        print(len('goodbye, world'))
        print('--------------索引和切片------------')
        s = 'abc123456'
        n = len(s)
        print('s[0] = ', s[0], '   ', 's[-n] = ', s[-n])  # a a
        print(s[n - 1], s[-1])  # 6 6
        # 正数是从0开始，负数是从-1开始
        print(s[2], s[-7])  # c c
        print(s[5], s[-4])  # 3 3
        print(s[2:5])  # c12
        print(s[-7:-4])  # c12
        print(s[2:])  # c123456
        print(s[:2])  # ab
        print(s[::2])
        print(s[::-1])

    def demo6(self):
        print('--------字符的遍历-----------')
        # 如果希望遍历字符串中的每个字符，可以使用`for-in`循环，有如下所示的两种方式。
        # 方式一：
        s = 'hello'
        for i in range(len(s)):
            print(s[i])
        # 方式二：
        s = 'hello'
        for elem in s:
            print(elem)

    def demo7(self):
        s1 = 'hello, world!'
        print('字符串首字母大写: ', s1.capitalize())
        print('字符串每个单词首字母大写: ', s1.title())
        print('字符串所有单词大写：',s1.upper())
        print('字符串变小写：',s1.upper().lower())
        print(s1.find('or'))      # 8
        print(s1.find('or', 9))  # -1




if __name__ == '__main__':
    demo = Demo001()
    demo.demo1()
    demo.demo2()
    demo.demo3()
    demo.demo4()
    demo.demo5()
    demo.demo6()
    demo.demo7()

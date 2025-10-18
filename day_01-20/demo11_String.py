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
        print('字符串所有单词大写：', s1.upper())
        print('字符串变小写：', s1.upper().lower())
        print(s1.find('or'))  # 8
        print(s1.find('or', 9))  # -1
        print(s1.find('of'))  # -1
        print(s1.index('or'))  # 8
        # `find`方法找不到指定的字符串会返回`-1`，`index`方法找不到指定的字符串会引发`ValueError`错误。
        # print(s1.index('or', 9))  # ValueError: substring not found

        # `find`和`index`方法还有逆向查找（从后向前查找）的版本，分别是`rfind`和`rindex`，代码如下所示。
        s = 'hello world!'
        print(s.find('o'))  # 4
        print(s.rfind('o'))  # 7
        print(s.rindex('o'))  # 7
        # print(s.rindex('o', 8))  # ValueError: substring not found

    def demo8(self):
        s1 = 'hello, world!'
        print(s1.startswith("He"))
        print(s1.startswith('hel'))
        print(s1.endswith('!'))
        s2 = 'abc123456'
        # `isdigit`用来判断字符串是不是完全由数字构成的
        print(s2.isdigit())
        # `isalnum`用来判断字符串是不是由字母和数字构成的
        print(s2.isalnum())  # True
        # `isalpha`用来判断字符串是不是完全由字母构成的，这里的字母指的是 Unicode 字符但不包含 Emoji 字符
        print(s2.isalpha())

    def demo9(self):
        """
        格式化：
        在 Python 中，字符串类型可以通过`center`、`ljust`、`rjust`方法做居中、左对齐和右对齐的处理。
        如果要在字符串的左侧补零，也可以使用`zfill`方法。
        :return:
        """
        s = 'hello, world'
        print(s.center(20, '*'))  # ****hello, world****
        print(s.rjust(20))  # hello, world
        print(s.ljust(20, '~'))  # hello, world~~~~~~~~
        print('33'.zfill(5))  # 00033
        print('-33'.zfill(5))  # -0033

        a = 321
        b = 123
        print('%d * %d = %d' % (a, b, a * b))  # 321 * 123 = 39483

        print('{0} * {1} = {2}'.format(a, b, a * b))

        print(f'{a} * {b} = {a * b}')

        # 修剪操作
        s1 = '   jackfrued@126.com  '
        print(s1.strip())  # jackfrued@126.com
        s2 = '~你好，世界~'
        print(s2.lstrip('~'))  # 你好，世界~
        print(s2.rstrip('~'))  # ~你好，世界

        """
        #### 替换操作

        如果希望用新的内容替换字符串中指定的内容，
        可以使用`replace`方法，代码如下所示。
        `replace`方法的第一个参数是被替换的内容，第二个参数是替换后的内容，
        还可以通过第三个参数指定替换的次数。
        """
        s = 'hello, good world'
        print(s.replace('o', '@'))  # hell@, g@@d w@rld
        print(s.replace('o', '@', 1))  # hell@, good world

        print("----------------拆分与合并-------------------")
        """
            #### 拆分与合并
            可以使用字符串的`split`方法将一个字符串拆分为多个字符串（放在一个列表中），
            也可以使用字符串的`join`方法将列表中的多个字符串连接成一个字符串，代码如下所示。
        """
        s = 'I love you'
        words = s.split()
        print(words)  # ['I', 'love', 'you']
        print('~'.join(words))  # I~love~you

        """
        Python 中除了字符串`str`类型外，还有一种表示二进制数据的字节串类型（`bytes`）。
        所谓字节串，就是**由零个或多个字节组成的有限序列**。通过字符串的`encode`方法，
        我们可以按照某种编码方式将字符串编码为字节串，我们也可以使用字节串的`decode`方法，
        将字节串解码为字符串，代码如下所示。
        """
        print("----------------编码和解码-------------------")
        a = '骆昊'
        b = a.encode('utf-8')
        c = a.encode('gbk')
        print(b)  # b'\xe9\xaa\x86\xe6\x98\x8a'
        print(c)  # b'\xc2\xe6\xea\xbb'
        print(b.decode('utf-8'))  # 骆昊
        print(c.decode('gbk'))  # 骆昊


    def demo10(self):
        print('..')


if __name__ == '__main__':
    demo = Demo001()
    # demo.demo1()
    # demo.demo2()
    # demo.demo3()
    # demo.demo4()
    # demo.demo5()
    # demo.demo6()
    # demo.demo7()
    # demo.demo8()
    demo.demo9()
    demo.demo10()

class Demo001:

    @staticmethod
    def demo1():
        print('----------------创建和使用字典-------------------')
        xinhua = {
            '麓': '山脚下',
            '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
            '蕗': '甘草的别名',
            '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
        }
        print(xinhua)
        person = {
            'name': '王大锤',
            'age': 55,
            'height': 168,
            'weight': 60,
            'addr': '成都市武侯区科华北路62号1栋101',
            'tel': '13122334455',
            'emergence contact': '13800998877'
        }
        print(person)

        # dict函数(构造器)中的每一组参数就是字典中的一组键值对
        person = dict(name='王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋101')
        print(person)

        # 可以通过Python内置函数zip压缩两个序列并创建字典
        items1 = dict(zip('ABCDE', '12345'))
        print(items1)

        items2 = dict(zip('ABCDE', range(1, 10)))
        print(items2)

        # 用字典生成式语法创建字典
        items3 = {x: x ** 3 for x in range(1, 6)}
        print(items3)

        person = {
            'name': '王大锤',
            'age': 55,
            'height': 168,
            'weight': 60,
            'addr': '成都市武侯区科华北路62号1栋101'
        }
        print(len(person))
        for key in person:
            print(key, ' = ', person[key])

    @staticmethod
    def demo2():
        print('----------------字典的运算-------------------')
        person = {
            'name': '王大锤',
            'age': 55,
            'height': 168,
            'weight': 60,
            'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
            'car': {
                'brand': 'BMW X7',
                'maxSpeed': '250',
                'length': 5170,
                'width': 2000,
                'height': 1835,
                'displacement': 3.0
            }
        }
        print(person)
        person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}
        print('name' in person)
        print('tel' in person)

        print('----------------索引运算-------------------')
        print(person['name'])
        print(person['addr'])
        print(person['addr'])
        person['age'] = 25
        person['height'] = 178
        person['tel'] = '13122334455'
        person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
        print(person)

        print('----------------循环遍历-------------------')
        for key in person:
            print(f'{key}:\t{person[key]}')








    @staticmethod
    def demo3():
        print('----------------字典的方法-------------------')
        person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
        print(person.get('name'))  # 王大锤
        print(person.get('sex'))  # None
        # 设置默认值：
        print(person.get('sex', True))  # True
        print(person.keys())
        print(person.values())
        print(person.items())
        for key,value in person.items():
            print(f'{key} : \t {value}')

        print('----------------字典更新-------------------')
        person1 = {'name': '王大锤', 'age': 55, 'height': 178}
        person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
        person1.update(person2)
        #  Python 3.9 以上的版本更新，可以用下面的方法
        # person1 |= person2
        print(person1)





    @staticmethod
    def demo4():
        print('----------------字典删除-------------------')
        person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
        print(person.pop('age')) # 25
        print(person)

        print(person.popitem())
        print(person)

        person.clear()
        print(person)

        person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
        del person['age']
        del person['addr']
        print(person)

    @staticmethod
    def demo5():
        print('----------------字典的应用-------------------')
        sentence = input('请输入一段话: ')
        counter = {}
        for ch in sentence:
            if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
                counter[ch] = counter.get(ch, 0) + 1
        sorted_keys = sorted(counter, key=counter.get, reverse=True)
        for key in sorted_keys:
            print(f'{key} 出现了 {counter[key]} 次.')



    @staticmethod
    def demo6():
        print('----------------在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。-------------------')
        stocks = {
            'AAPL': 191.88,
            'GOOG': 1186.96,
            'IBM': 149.24,
            'ORCL': 48.44,
            'ACN': 166.89,
            'FB': 208.09,
            'SYMC': 21.29
        }
        stocks2 = {key: value for key, value in stocks.items() if value > 100}
        print(stocks2)


if __name__ == '__main__':
    Demo001.demo1()
    Demo001.demo2()
    Demo001.demo3()
    Demo001.demo4()
    # Demo001.demo5()
    Demo001.demo6()

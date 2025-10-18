class Demo001:

    @staticmethod
    def demo1():
        print('----------------创建集合-------------------')
        set1 = {1, 2, 3, 3, 3, 2}
        print(set1)

        set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
        print(set2)

        # 用 Python 内置函数`set`来创建一个集合，准确的说`set`并不是一个函数，而是创建集合对象的构造器
        set3 = set('hello')
        print(set3)

        set4 = set([1, 4, 4, 185, 85, 8, 77])
        print(set4)

        set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
        print(set5)

        print('----------------元素的遍历-------------------')
        set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
        for elem in set1:
            print(elem)

        print('----------------成员运算-------------------')
        set1 = {11, 12, 13, 14, 15}
        print(10 in set1)
        print(15 in set1)
        set2 = {'python', 'java', 'c++', 'swift'}
        print('go' in set2)
        print('java' in set2)

    @staticmethod
    def demo2():
        print('----------------二元运算-------------------')
        set1 = {1, 2, 3, 4, 5, 6, 7}
        set2 = {2, 4, 6, 8, 10}

        #  交集
        print(set1 & set2)  # {2, 4, 6}
        print(set1.intersection(set2))  # {2, 4, 6}

        # 并集
        print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 10}
        print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8, 10}

        # 差集 (set1里面有，set2没有的)
        print(set1 - set2)  # {1, 3, 5, 7}
        print(set1.difference(set2))

        # 对称差 (set1里面有set2没有的元素，set2里面有set1里面没有的元素，加起来的集合)
        print(set1 ^ set2)  # {1, 3, 5, 7, 8, 10}
        print(set1.symmetric_difference(set2))

        set1 = {1, 3, 5, 7}
        set2 = {2, 4, 6}
        # set1 |= set2
        set1.update(set2)
        print(set1)  # {1, 2, 3, 4, 5, 6, 7}

        set3 = {3, 6, 9}
        set1 &= set3
        set1.intersection_update(set3)
        print(set1)

        set2 -= set1
        # set2.difference_update(set1)
        print(set2)  # {2, 4}

    @staticmethod
    def demo3():
        print('----------------比较运算-------------------')
        set1 = {1, 3, 5}
        set2 = {1, 2, 3, 4, 5}
        set3 = {5, 4, 3, 2, 1}
        print(set1 < set2)  # True
        print(set1 <= set2)  # True
        print(set2 < set3)  # False
        print(set2 <= set3)  # True
        print(set2 > set1)  # True
        print(set2 == set3)  # True

    @staticmethod
    def demo4():
        print('----------------集合的方法-------------------')
        set1 = {1, 10, 100}
        set1.add(1000)
        set1.add(10000)
        print(set1)

        # 删除元素
        # discard(x)：如果元素 x 在集合中，则删除它；如果 x 不存在，不会做任何操作，也不会报错。
        set1.discard(10)
        if 100 in set1:
            # remove(x)：如果元素 x 在集合中，则删除它；如果 x 不存在，会直接抛出 KeyError 错误。
            set1.remove(100)
        print(set1)
        print('长度：', len(set1))

        # 清空元素
        set1.clear()
        print(set1)  # set()

        set1 = {'Java', 'Python', 'C++', 'Kotlin'}
        set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
        set3 = {'HTML', 'CSS', 'JavaScript'}

        # 集合类型还有一个名为`isdisjoint`的方法可以判断两个集合有没有相同的元素，
        # 如果没有相同元素，该方法返回`True`，否则该方法返回`False`，代码如下所示。
        print(set1.isdisjoint(set2))  # False
        print(set1.isdisjoint(set3))  # True

    @staticmethod
    def demo5():
        print('----------------不可变集合-------------------')
        fset1 = frozenset({1, 3, 5, 7})
        fset2 = frozenset(range(1, 6))
        print(fset1)  # frozenset({1, 3, 5, 7})
        print(fset2)  # frozenset({1, 2, 3, 4, 5})
        print('交集(两个集合都存在的元素):', fset1 & fset2)
        print('并集(两个集合合并起来的元素):', fset1 | fset2)
        print('差集(第一个集合有，第二个集合没有的元素):', fset1 - fset2)
        print(fset1 < fset2)

        """
        ### 总结

        Python 中的**集合类型是一种无序容器**，**不允许有重复运算**，由于底层使用了哈希存储，
        集合中的元素必须是`hashable`类型。集合与列表最大的区别在于**集合中的元素没有顺序**、
        所以**不能够通过索引运算访问元素**、但是集合可以执行交集、并集、差集等二元运算，
        也可以通过关系运算符检查两个集合是否存在超集、子集等关系。
        """

    @staticmethod
    def demo6():
        print()


if __name__ == '__main__':
    Demo001.demo1()
    Demo001.demo2()
    Demo001.demo3()
    Demo001.demo4()
    Demo001.demo5()
    Demo001.demo6()

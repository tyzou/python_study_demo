import heapq
import itertools
from collections import Counter


class Demo31:
    """
    Python语言进阶
    """

    @staticmethod
    def demo1():
        print('----------------生成式（推导式）的用法-------------------')
        prices = {
            'AAPL': 191.88,
            'GOOG': 1186.96,
            'IBM': 149.24,
            'ORCL': 48.44,
            'ACN': 166.89,
            'FB': 208.09,
            'SYMC': 21.29
        }
        # 字典推导式的等价写法（传统循环方式）
        prices2 = {}
        for key, value in prices.items():
            if value > 100:
                prices2[key] = value
        print('字典推导式的等价写法（传统循环方式）: ', prices2)

        # 字典推导式（简洁写法）：
        prices3 = {key: value for key, value in prices.items() if value > 100}
        print('字典推导式: ', prices3)

        # 基本字典推导式（无条件）
        squares = {x: x ** 2 for x in range(1, 6)}
        # 结果: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        print(squares)

        # 带条件的字典推导式
        even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
        # 结果: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
        print(even_squares)

        # 带转换的字典推导式
        names = {'alice': 25, 'bob': 30, 'charlie': 35}
        uppercase_names = {name.upper(): age for name, age in names.items()}
        # 结果: {'ALICE': 25, 'BOB': 30, 'CHARLIE': 35}
        print(uppercase_names)

    @staticmethod
    def demo2():
        print('----------------从列表中找出最大的或最小的N个元素堆结构(大根堆/小根堆)-------------------')
        list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
        list2 = [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.75},
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'ACME', 'shares': 75, 'price': 115.65}
        ]
        print('返回可迭代对象中 最大的 n 个元素，按降序排列:', heapq.nlargest(3, list1))
        print('返回可迭代对象中 最小的 n 个元素，按升序排列:', heapq.nsmallest(3, list1))
        print('从 list2 中找出 价格（price）最高的 2 支股票:', heapq.nlargest(2, list2, key=lambda x: x['price']))
        print('找出 持股数量（shares）最多的 2 家公司:', heapq.nlargest(2, list2, key=lambda x: x['shares']))

    @staticmethod
    def demo3():
        print('----------------迭代工具模块-------------------')

        print("=== ABCD的全排列 ===")
        permutations_result = list(itertools.permutations('ABCD'))
        for i, perm in enumerate(permutations_result, 1):
            print(f"{i:2d}. {''.join(perm)}")
        print(f"总共 {len(permutations_result)} 种排列\n")

        print("=== ABCDE的五选三组合 ===")
        combinations_result = list(itertools.combinations('ABCDE', 3))
        for i, combo in enumerate(combinations_result, 1):
            print(f"{i:2d}. {''.join(combo)}")
        print(f"总共 {len(combinations_result)} 种组合\n")

        print("=== ABCD和123的笛卡尔积 ===")
        product_result = list(itertools.product('ABCD', '123'))
        for i, prod in enumerate(product_result, 1):
            print(f"{i:2d}. {''.join(prod)}")
        print(f"总共 {len(product_result)} 个笛卡尔积元素\n")

        print("=== ABC的无限循环序列（前10个元素）===")
        cycle_iter = itertools.cycle(('A', 'B', 'C'))
        for i in range(10):
            print(f"{i + 1}. {next(cycle_iter)}")
        print("...")

    @staticmethod
    def demo4():
        print('----------------找出序列中出现次数最多的元素-------------------')
        words = [
            'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
            'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
            'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
            'look', 'into', 'my', 'eyes', "you're", 'under'
        ]
        counter = Counter(words)
        print(counter.most_common(3))

    @staticmethod
    def demo5():
        """
        公鸡5元一只 母鸡3元一只 小鸡1元三只
        用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
        """
        print('----------------百钱百鸡-------------------')
        # 公鸡5元一只 母鸡3元一只 小鸡1元三只
        # 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
        for x in range(20):
            for y in range(33):
                z = 100 - x - y
                if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
                    print(x, y, z)

    @staticmethod
    def demo6():
        # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
        # 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
        # B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
        # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
        print('----------------五人分鱼-------------------')
        fish = 6
        while True:
            total = fish
            enough = True
            for _ in range(5):
                if(total - 1) % 5 == 0:
                    total = (total - 1) // 5 * 4
                else:
                    enough = False
                    break
            if enough:
                print(fish)
                break
            fish += 5



if __name__ == '__main__':
    Demo31.demo1()
    Demo31.demo2()
    Demo31.demo3()
    Demo31.demo4()
    Demo31.demo5()
    Demo31.demo6()

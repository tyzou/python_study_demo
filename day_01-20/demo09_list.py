import random
from rich.console import Console
from rich.table import Table

class Demo09:

    @staticmethod
    def demo1():
        print("添加和删除元素")
        languages = ['Python', 'Java', 'C++']
        languages.append('javascript')
        print(languages)
        languages.insert(2, 'SQL')
        print(languages)

    @staticmethod
    def demo2():
        print("删除指定元素")
        languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
        if 'Java' in languages:
            languages.remove('Java')
        if 'Go' in languages:
            languages.remove('Go')
        print(languages)
        languages.pop()  # `pop`方法默认删除列表中的最后一个元素
        print(languages)
        temp = languages.pop(1)
        print(temp)
        print(languages)
        languages.append(temp)
        print(languages)
        languages.clear()
        print(languages)

        # 多个同名，删除只删除第一个
        languages.append("python")
        languages.append("java")
        languages.append("python")
        print(languages)
        languages.remove('python')
        print(languages)

    @staticmethod
    def demo3():
        print('元素位置和频次')
        items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
        print(items)
        print(items.index('Python'))  # 0
        # 从索引位置1开始查找'Python'
        print(items.index('Python', 1))  # 5
        print(items.count('Python'))
        # print(items.index('Java', 3))  # ValueError: 'Java' is not in list

        print('元素排序和反转')
        items.sort()
        print('排序：', items)
        items.reverse()
        print('反转：', items)

    @staticmethod
    def demo4():
        print('列表生成式')
        items = []
        for i in range(1, 100):
            if i % 3 == 0 or i % 4 == 0:
                items.append(i)
        print(items)
        # 使用列表生成式做同样的事情
        items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
        print(items)

        print('场景二：有一个整数列表`nums1`，创建一个新的列表`nums2`，`nums2`中的元素是`nums1`中对应元素的平方。')
        nums1 = [22, 854, 488, 44]
        nums2 = []
        for num in nums1:
            nums2.append(num ** 2)
        print(nums2)
        # 另一种实现方式
        nums3 = [num ** 2 for num in nums1]
        print(nums3)

        print('场景三： 有一个整数列表`nums1`，创建一个新的列表`nums2`，将`nums1`中大于`50`的元素放到`nums2`中。')
        nums1 = [35, 12, 97, 64, 55]
        nums2 = []
        for num in nums1:
            if num > 50:
                nums2.append(num)
        print(nums2)
        # 另一种是实现方式
        nums2 = [num for num in nums1 if num > 50]
        print(nums2)

    @staticmethod
    def demo5():
        print('嵌套列表')
        scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
        print(scores[0])
        print(scores[0][0])

        print('随机数的方式来生成5个学生3门课程的成绩并保存在列表中，我们可以使用列表生成式，代码如下所示。')
        scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
        print(scores)

    @staticmethod
    def demo6():
        print('双色球随机选号程序')
        red_balls = list(range(1, 34))
        selected_balls = []
        # 添加6个红色球到选中列表
        for _ in range(6):
            # 生成随机整数代表选中的红色球的索引位置
            length = len(red_balls)
            # 将选中的球从红色球列表中移除并添加到选中列表
            index = random.randrange(length)
            selected_balls.append(red_balls.pop(index))
        selected_balls.sort()
        print(selected_balls)
        for ball in selected_balls:
            print(f'\033[031m{ball:0>2d}\033[0m', end=' ')

        # 随机选择1个蓝色球
        blue_ball = random.randrange(1, 17)
        # 输出选中的蓝色球
        print(f'\033[034m{blue_ball:0>2d}\033[0m')

    @staticmethod
    def demo7():
        print('双色球随机选号程序')
        red_balls = [i for i in range(1, 34)]
        blue_balls = [i for i in range(1, 17)]
        # 从红色球列表中随机抽出6个红色球（无放回抽样）
        selected_balls = random.sample(red_balls, 6)
        # 对选中的红色球排序
        selected_balls.sort()
        # 输出选中的红色球
        for ball in selected_balls:
            print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
        # 从蓝色球列表中随机抽出1个蓝色球
        blue_ball = random.choice(blue_balls)
        # 输出选中的蓝色球
        print(f'\033[034m{blue_ball:0>2d}\033[0m')

    @staticmethod
    def demo8():
        print('双色球随机选号程序')
        n = int(input('生成几注号码: '))
        red_balls = [i for i in range(1, 34)]
        blue_balls = [i for i in range(1, 17)]
        for _ in range(n):
            # 从红色球列表中随机抽出6个红色球（无放回抽样）
            selected_balls = random.sample(red_balls, 6)
            # 对选中的红色球排序
            selected_balls.sort()
            # 输出选中的红色球
            for ball in selected_balls:
                print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
            # 从蓝色球列表中随机抽出1个蓝色球
            blue_ball = random.choice(blue_balls)
            # 输出选中的蓝色球
            print(f'\033[034m{blue_ball:0>2d}\033[0m')

    @staticmethod
    def demo9():
        # 创建控制台
        console = Console()
        n = int(input('生成几注号码: '))
        red_balls = [i for i in range(1, 34)]
        blue_balls = [i for i in range(1, 17)]
        # 创建表格并添加表头
        table = Table(show_header=True)
        for col_name in ('序号', '红球', '蓝球'):
            table.add_column(col_name, justify='center')

        for i in range(n):
            selected_balls = random.sample(red_balls, 6)
            selected_balls.sort()
            blue_ball = random.choice(blue_balls)
            # 向表格中添加行（序号，红色球，蓝色球）
            table.add_row(
                str(i + 1),
                f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
                f'[blue]{blue_ball:0>2d}[/blue]'
            )

        # 通过控制台输出表格
        console.print(table)


if __name__ == '__main__':
    # Demo09.demo1()
    # Demo09.demo2()
    # Demo09.demo3()
    # Demo09.demo4()
    # Demo09.demo5()
    # Demo09.demo6()
    # Demo09.demo7()
    # Demo09.demo8()
    Demo09.demo9()

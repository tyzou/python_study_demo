# 静态方法和类方法
class Triangle(object):
    def __init__(self,a,b,c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    def is_valid(a,b,c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a+b>c and b+c>a and a+c>b

    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    # 调用静态方法
    print(f"是否是三角形:{Triangle.is_valid(3, 4, 5)}")
    # 计算三角形周长和面积的方法添加一个`property`装饰器（Python 内置类型），
    # 这样三角形类的`perimeter`和`area`就变成了两个属性，
    # 不再通过调用方法的方式来访问，
    # 而是用对象访问属性的方式直接获得,不用再加括号
    print(f'周长: {t.perimeter}')
    print(f'面积: {t.area}')
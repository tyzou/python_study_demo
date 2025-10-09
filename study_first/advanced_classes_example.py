#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
超详细注释示例：@property、抽象基类（ABC）、静态方法、类方法
作者：kimi
日期：2025-09
"""

from abc import ABC, abstractmethod   ## abc 模块提供“抽象基类”基础设施
import math


# 1. 使用@property装饰器创建属性 -------------------------------------------------
class Circle:
    """
    圆形类，演示如何:
    1. 把方法伪装成属性（@property）
    2. 在赋值时做数据验证（@xxx.setter）
    3. 提供只读属性（area、circumference）
    """

    def __init__(self, radius: float):
        ## 单下划线是“程序员约定”的私有变量，外部不该直接访问
        self._radius = radius

    ## ====== 半径的 getter ======
    @property
    def radius(self) -> float:
        """返回半径（只读，除非再配 setter）"""
        return self._radius

    ## ====== 半径的 setter ======
    @radius.setter
    def radius(self, value: float) -> None:
        """
        给半径赋值时会先跑这段代码，可做校验、触发事件、写日志等
        如果赋值非法，直接抛异常，阻止修改
        """
        if value <= 0:
            raise ValueError("半径必须是正数")
        self._radius = value

    ## ====== 只读属性：面积 ======
    @property
    def area(self) -> float:
        """面积，动态计算，外部无法赋值（无 setter）"""
        return math.pi * self._radius ** 2

    ## ====== 只读属性：周长 ======
    @property
    def circumference(self) -> float:
        """周长，动态计算，外部无法赋值"""
        return 2 * math.pi * self._radius


# 2. 抽象基类（ABC） -------------------------------------------------------------
"""
ABC 是什么？
----------------
ABC = Abstract Base Class，即“抽象基类”。
它本身不能被实例化，只能被继承；并且强制子类必须实现指定的抽象方法。
作用：
1. 明确接口：告诉所有子类“你必须实现这些方法，否则别想实例化”。
2. 运行时检查：如果子类漏了实现，Python 在**实例化阶段**就会抛 TypeError，提前暴露错误。
3. 更好的多态：调用方只要拿到 Shape 类型，就能放心地调用 area()/perimeter()，无需关心具体子类。

与普通继承的区别：
-------------------
普通基类：子类**可以**重写，但**不强制**。
抽象基类：子类**必须**重写（实现）所有抽象方法，否则无法实例化。
"""


class Shape(ABC):
    """
    所有几何图形的“顶层设计图”。
    本身不能 new Shape()；任何子类必须实现 area() 与 perimeter()。
    """

    ## 抽象方法：只有签名，没有实现。子类必须 override。
    @abstractmethod
    def area(self) -> float:
        """计算面积"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """计算周长"""
        pass

    ## 类方法：属于类本身，而不是实例；可以被子类继承。
    @classmethod
    def describe(cls) -> str:
        """返回类的描述信息，cls 指向当前类（可能是 Shape 也可能是子类）"""
        return f"{cls.__name__} 是一个几何形状类"


class Rectangle(Shape):
    """
    矩形：具体实现 Shape 抽象基类
    必须实现 area() 与 perimeter()，否则无法实例化
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    ## 必须实现抽象方法，否则 Rectangle 也是“抽象”的，无法实例化
    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    ## 静态方法：与实例/类都无关，只是挂在类名下的普通函数
    @staticmethod
    def is_square(width: float, height: float) -> bool:
        """给定宽高，判断是不是正方形"""
        return width == height


# 3. 测试入口 --------------------------------------------------------------------
if __name__ == "__main__":
    print("========== 1. Circle 属性装饰器演示 ==========")
    circle = Circle(5)
    print(f"半径: {circle.radius}")
    print(f"面积: {circle.area:.2f}")
    print(f"周长: {circle.circumference:.2f}")

    ## 通过 setter 修改半径
    circle.radius = 10
    print(f"新半径: {circle.radius}")
    print(f"新面积: {circle.area:.2f}")

    ## 下面这句会抛 ValueError，因为半径必须 > 0
    # circle.radius = -3

    print("\n========== 2. ABC 抽象基类演示 ==========")
    rect = Rectangle(4, 6)
    print(f"矩形面积: {rect.area()}")
    print(f"矩形周长: {rect.perimeter()}")
    print(f"4×4 是正方形吗？{Rectangle.is_square(4, 4)}")

    ## 类方法被子类继承，cls 自动指向 Rectangle
    print(Shape.describe())      # Shape 是一个几何形状类
    print(Rectangle.describe())  # Rectangle 是一个几何形状类

    ## 下面这行如果取消注释会直接报错：TypeError: Can't instantiate abstract class Shape...
    # s = Shape()
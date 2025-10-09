# 定义一个类描述平面上的点，提供计算到另一个点距离的方法。
class Point:
    # 初始化方法
    def __init__(self,x=0,y=0):
        self.x,self.y = x,y

    # 计算与另一个点的距离
    def distance_to(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy) ** 0.5

    def __str__(self):
        return f"({self.x},{self.y})"

p1 = Point(3,5)
p2 = Point(6,9)
print(p1)
print(p2)
print(p1.distance_to(p2))
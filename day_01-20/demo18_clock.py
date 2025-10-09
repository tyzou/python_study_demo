import time

# 定义一个类描述数字时钟，提供走字和显示时间的功能。
class Clock:
    """ 数字时钟 """

    def __init__(self,hour=0,minute=0,second=0):
        """ 初始化方法
        :param hour: 时钟
        :param minute: 分钟
        :param second: 秒
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60:
            self.second =0
            self.minute +=1

        if self.minute == 60:
            self.hour += 1
            self.minute = 0

        if self.hour == 24:
            self.hour = 0

    def show(self):
        """ 显示时间 """
        return f"{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}"

clock = Clock(23,58,10)
while True:
    print(clock.show())
    time.sleep(1)
    clock.run()
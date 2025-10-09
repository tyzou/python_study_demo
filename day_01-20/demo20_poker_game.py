# 扑克游戏
# 扑克只有52张牌（没有大小王），
# 游戏需要将 52 张牌发到 4 个玩家的手上，
# 每个玩家手上有 13 张牌，按照黑桃、红心、草花、方块的顺序和点数从小到大排列，

from enum import Enum
import random

class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


class Card:
    """定义牌类。"""
    def __init__(self,suite,face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        """返回牌的字符串表示，格式为“花色符号+点数”。"""
        # 花色顺序：黑桃、红心、梅花、方块
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'  # 返回牌的花色和点数

class Poker:
    """扑克"""
    def __init__(self):
        self.cards = []
        for suite in Suite:
            for face in range(1, 14):
                self.cards.append(Card(suite, face))

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)  # 通过random模块的shuffle函数实现随机乱序

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)

if __name__ == '__main__':
    poker = Poker()
    print(f'洗牌前的牌：{poker.cards}')  # 洗牌前的牌
    poker.shuffle()
    print(f'洗牌后的牌：{poker.cards}')  # 洗牌后的牌
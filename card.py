#!/usr/bin/env python
# coding: UTF-8


class Card(object):
    """
    マークと数字でカードを生成する

    Attributes
    ----------
    value : str
        カードの数字
    suit : str
        カードのマーク
    """
    # 数値(インデックスの値を揃える為) ex. values[2] = "2" values[14] = "Ace"
    values = (
        [None, None, 2, 3, 4, 5, 6,
         7, 8, 9, 10, 11, 12, 13, 1]
    )
    # マーク
    suits = ["♠︎", "❤︎", "♦︎", "♣️"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    # repr → インスタンスを文字列で返してくれる特殊メソッド
    def __repr__(self):
        v = self.suits[self.suit] + str(self.values[self.value])
        return v

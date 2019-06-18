#!/usr/bin/env python
# coding: UTF-8


class Card(object):
    # 数値(インデックスの値を揃える為) ex. values[2] = "2" values[14] = "Ace"
    # values = (
    #     [None, None, "2", "3", "4", "5", "6",
    #      "7", "8", "9", "10", "11", "12", "13", "1"]
    # )
    values = (
        [None, None, 2, 3, 4, 5, 6,
         7, 8, 9, 10, 11, 12, 13, 1]
    )
    # マーク
    suits = ["♠︎", "❤︎", "♦︎", "♣️"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    # 引数付きのインスタンスを文字列で返してくれる関数
    def __str__(self):
        v = self.suits[self.suit] + str(self.values[self.value])
        return v

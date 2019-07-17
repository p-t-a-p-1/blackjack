#!/usr/bin/env python
# coding: UTF-8
import card
from random import shuffle


class Deck(object):
    """
    カード52枚を持ったデッキ

    Attributes
    ----------
    cards : dict
        持っているカード
    """
    def __init__(self):
        self.cards = []
        # 2から14（エース）✖︎ 4つのマーク 通りループさせる
        # カードについてはcard.pyのCardクラスより生成する
        for i in range(2, 15):
            # 数字のループ
            for j in range(4):
                # マークのループ
                # 生成されたカード(❤︎2など)をリストに入れる
                self.cards.append(card.Card(i, j))
        # 生成されたデッキをシャッフルする
        shuffle(self.cards)

    # ドロー : デッキから要素を1つ削除し、その要素を取り出す
    def draw(self):
        # デッキがない場合は何もしない
        # TODO カードがなくなった場合は補充（デッキ作成）
        if len(self.cards) == 0:
            return
        # デッキから取り出す
        return self.cards.pop()

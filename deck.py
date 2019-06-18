#!/usr/bin/env python
# coding: UTF-8
import card
from random import shuffle


class Deck(object):
    def __init__(self):
        self.cards = []
        # 2から14（エース）✖︎ 4つのマーク 通りループさせる
        # カードについてはcard.pyのCardクラスより生成する
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(card.Card(i, j))
        # 生成されたデッキをシャッフルする
        shuffle(self.cards)

    # ドロー : デッキから要素を1つ削除し、その要素を取り出す
    def rm_card(self):
        # デッキがない場合は何もしない
        if len(self.cards) == 0:
            return
        return self.cards.pop()

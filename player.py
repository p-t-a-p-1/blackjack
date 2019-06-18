#!/usr/bin/env python
# coding: UTF-8


class Person(object):
    """
    プレイヤーの情報を保持する

    Attributes
    ----------
    wins : int
        勝利数
    card : dict
        持っているカード
    """

    def __init__(self):
        self.wins = 0
        self.card = None


class Dealer(Person):
    def __init__(self):
        self.name = "Dealer"


class Player(Person):
    def __init__(self):
        self.name = "You"

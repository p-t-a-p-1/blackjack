#!/usr/bin/env python
# coding: UTF-8

import deck
import player
import re


class Game:
    def __init__(self):
        self.deck = deck.Deck()
        self.dealer = player.Dealer()
        self.player = player.Player()

    # カードから数値を算出する
    def get_card_val(card_str):
        card_val = re.sub(r'\D', '', str(card_str))
        card_val = int(card_val)
        # 11, 12, 13 は全て10扱い
        if card_val >= 10:
            card_val = 10
        return card_val

    def play_game(self):
        print("Game Start!!")
        # シャッフルされたカード 52枚
        cards = self.deck.cards
        while len(cards) >= 5:
            start_msg = " Q で終了,それ以外でPlay: "
            start_res = input(start_msg)
            if start_res == 'Q':
                break
            # playerとdealerに2枚ずつ配る ex ❤︎2 , ♠︎13 など
            p_card_1 = self.deck.rm_card()
            d_card_1 = self.deck.rm_card()
            p_card_2 = self.deck.rm_card()
            d_card_2 = self.deck.rm_card()
            # player の値の計算
            p_card_1_val = Game.get_card_val(p_card_1)
            p_card_2_val = Game.get_card_val(p_card_2)
            p_sum = p_card_1_val + p_card_2_val
            # dealer の値計算
            d_card_1_val = Game.get_card_val(d_card_1)
            d_card_2_val = Game.get_card_val(d_card_2)
            d_sum = d_card_1_val + d_card_2_val

            # 最初のフェーズ
            print("")
            print("------------")
            print("Your Card is [ {} , {} ]".format(p_card_1, p_card_2))
            print("total {}".format(p_sum))
            print("Dealer Card is [ {} , ** ]".format(d_card_1, d_card_2))
            # print("total {}".format(d_sum))
            print("------------")

            # hit（もう1枚引く） or stand（これで勝負する）
            hs_flg = True
            while hs_flg:
                hs_msg = "\nHit(1) or Stand(2) : "
                hs_res = input(hs_msg)
                print("")
                if hs_res == '1':
                    # hit
                    p_add_card = self.deck.rm_card()
                    p_add_card_val = Game.get_card_val(p_add_card)
                    p_sum += p_add_card_val
                    print("------------")
                    print("Your draw card is {}".format(p_add_card))
                    print("Player total {}".format(p_sum))
                    # print("Dealer total {}".format(d_sum))
                    print("------------")
                    if p_sum > 21:
                        # 21より大きくなった場合は負け
                        print("\nYour Burst!")
                        hs_flg = False
                        break
                        # TODO dealerの勝ちカウントを増やす
                    elif p_sum == 21:
                        # 21になった場合は自動的に勝負する
                        hs_flg = False
                elif hs_res == '2':
                    # stand
                    hs_flg = False
                else:
                    # それ以外のコマンド
                    print("だめです")

            # 結果発表
            print("")
            print("--- Dealer Turn Start ---")

            while d_sum < 17:
                # dealerのカードが17以上になるまで引き続ける
                d_add_card = self.deck.rm_card()
                d_add_card_val = Game.get_card_val(d_add_card)
                d_sum += d_add_card_val
                print("------------")
                print("Dealer draw card is {}".format(d_add_card))

                print("Dealer total {}".format(d_sum))
                print("------------")

                if d_sum > 21:
                    print("\nDealer Burst!\n")

            print("--- Dealer Turn End ---\n")

            print("*-*-*-*-*-*-*-*")
            print("Player total is {}".format(p_sum))
            print("Dealer total is {}".format(d_sum))
            print("*-*-*-*-*-*-*-*")

            print("")
            # 勝敗
            # Plyer と Dealer のカードの合計
            if 21 >= p_sum > d_sum:
                print("\nYou Win!!\n")
            elif p_sum <= 21 < d_sum:
                print("\nYou Win!! (Dealer Burst) \n")
            elif p_sum == d_sum:
                print("@Draw@")
            else:
                # バーストした時点で負け
                print("You Lose...")
            print("")


game = Game()
game.play_game()

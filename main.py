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
        game_count = 0
        draw_count = 0
        # 残り5枚になるまで継続
        while len(cards) >= 5:
            start_msg = " Q で終了,それ以外でPlay: "
            start_res = input(start_msg)

            # Qで終了させ、戦績を表示させる
            if start_res == 'Q':
                break

            # カード保持を初期化
            self.player.card = []
            self.dealer.card = []

            # playerとdealerに2枚ずつ配る ex ❤︎2 , ♠︎13 など
            self.player.card.append(self.deck.draw())
            self.dealer.card.append(self.deck.draw())
            self.player.card.append(self.deck.draw())
            self.dealer.card.append(self.deck.draw())

            # player の値計算
            p_card_1_val = Game.get_card_val(self.player.card[0])
            p_card_2_val = Game.get_card_val(self.player.card[1])
            p_sum = p_card_1_val + p_card_2_val
            # dealer の値計算
            d_card_1_val = Game.get_card_val(self.dealer.card[0])
            d_card_2_val = Game.get_card_val(self.dealer.card[1])
            d_sum = d_card_1_val + d_card_2_val

            d_str = "Dealer Card is [ {} , ** ]".format(self.dealer.card[0])

            # 最初のフェーズ
            print("")
            print("------------")
            print("Your Card is {} ".format(self.player.card))
            print("total {}".format(p_sum))
            print(d_str)
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
                    p_add_card = self.deck.draw()
                    self.player.card.append(p_add_card)
                    p_add_card_val = Game.get_card_val(p_add_card)
                    p_sum += p_add_card_val
                    print("------------")
                    print("Your card is {}".format(self.player.card))
                    print("Player total {}".format(p_sum))
                    print(d_str)
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
                d_add_card = self.deck.draw()
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
            if d_sum < p_sum <= 21:
                print("\nYou Win!!\n")
                self.player.wins += 1
            elif p_sum <= 21 < d_sum:
                print("\nYou Win!! (Dealer Burst) \n")
                self.player.wins += 1
            elif p_sum == d_sum and p_sum <= 21:
                print("@Draw@")
            else:
                # バーストした時点で負け
                print("You Lose...")
                self.dealer.wins += 1
            game_count += 1
            print("")

        # ドローになった回数を計算
        draw_count = game_count - self.player.wins - self.dealer.wins

        # 戦績表示
        print("")
        print("*-*-*-*-*-*-*-*")
        print("total:{}".format(game_count))
        print("win:{}".format(self.player.wins))
        print("draw:{}".format(draw_count))
        print("lose:{}".format(self.dealer.wins))
        print("*-*-*-*-*-*-*-*")
        print("")


game = Game()
game.play_game()

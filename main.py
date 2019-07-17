#!/usr/bin/env python
# coding: UTF-8

import deck
import player
# 正規表現のためのライブラリ
import re


# ゲーム
class Game:
    """
    ブラックジャックのGameクラス

    Attributes
    ----------
    deck : dict
        52枚のカードをシャッフルしたデッキ
    dealer : str
        親
    player : str
        子（プレイヤー）
    """
    def __init__(self):
        self.deck = deck.Deck()
        self.dealer = player.Dealer()
        self.player = player.Player()

    # カードから数値を算出する
    def get_card_val(card_str):
        """
        Parameters
        ----------
        card_str : str
            カード ex) ❤︎2
        """
        # 正規表現を使い、文字列から数字だけ取り出す　❤︎2 → 2
        card_val = re.sub(r'\D', '', str(card_str))
        # 取り出した数字をintに変換
        card_val = int(card_val)
        # 11, 12, 13 は全て10扱い
        if card_val >= 10:
            card_val = 10
        return card_val

    # 勝ち負けを判定する
    def check_wins(self, d_val, p_val):
        """
        Parameters
        ----------
        d_val : int
            親の合計値
        p_val : int
            子の合計値
        """
        if d_val < p_val <= 21:
            # dealer < player <= 21の時、playerの勝利
            print("\nYou Win!!\n")
            # playerの勝ち回数を増やす
            self.player.wins += 1
        elif p_val <= 21 < d_val:
            # player が21以下、dealerがバーストはplayerの勝利
            print("\nYou Win!! (Dealer Burst) \n")
            # playerの勝ち回数を増やす
            self.player.wins += 1
        elif p_val == d_val and p_val <= 21:
            # どちらもバーストせず、同じ数字の場合は引き分け
            print("@Draw@")
        else:
            # それ以外の場合は全部 player の負け
            # バーストした時点で負け
            print("You Lose...")
            self.dealer.wins += 1

    # メインゲーム関数
    def play_game(self):
        print("Game Start!!")
        # シャッフルされたカード 52枚
        cards = self.deck.cards
        # 総ゲーム数
        game_count = 0
        draw_count = 0

        # 残り5枚になるまで継続
        while len(cards) >= 5:
            # スタートメッセージ
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
            # 確認用のdealerの持ち札メッセージ
            d_msg = "Dealer Card is [ {} , ** ]".format(self.dealer.card[0])

            # 最初のフェーズ
            print("")
            print("------------")
            print("Your Card is {} ".format(self.player.card))
            print("total {}".format(p_sum))
            print(d_msg)
            # print("total {}".format(d_sum))
            print("------------")

            # hit（もう1枚引く） or stand（これ以上引かない）
            hit_flg = True
            while hit_flg is True:
                hs_msg = "\nHit(1) or Stand(2) : "
                hs_res = input(hs_msg)
                print("")
                if hs_res == '1':
                    # hit（もう1枚引く） 1を選択する限り引き続ける

                    # デッキからドロー ex ❤︎2 など
                    p_add_card = self.deck.draw()
                    # 保持カードリストに追加
                    self.player.card.append(p_add_card)

                    # 合計を計算する
                    p_add_card_val = Game.get_card_val(p_add_card)
                    p_sum += p_add_card_val

                    # 途中経過メッセージ
                    print("------------")
                    print("Your card is {}".format(self.player.card))
                    print("Player total {}".format(p_sum))
                    print(d_msg)
                    print("------------")

                    # 21判定
                    if p_sum > 21:
                        # 21より大きくなった場合はバースト表示、勝敗判定へ
                        print("\nYour Burst!")
                        hit_flg = False
                        break

                    elif p_sum == 21:
                        # player が21になった場合は自動的に勝負する
                        hit_flg = False

                elif hs_res == '2':
                    # stand（これ以上引かない）
                    hit_flg = False

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

                # dealer の合計を足す
                d_sum += d_add_card_val

                # dealer の合計を表示
                print("------------")
                print("Dealer draw card is {}".format(d_add_card))
                print("Dealer total {}".format(d_sum))
                print("------------")

                if d_sum > 21:
                    # dealer が21を超えたらバースト表示
                    print("\nDealer Burst!\n")
            print("--- Dealer Turn End ---\n")

            # 合計数を表示
            print("*-*-*-*-*-*-*-*")
            print("Player total is {}".format(p_sum))
            print("Dealer total is {}".format(d_sum))
            print("*-*-*-*-*-*-*-*")

            print("")
            # 勝敗判定
            # Dealer と Player のカードの合計から
            Game.check_wins(self, d_sum, p_sum)
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


# このファイルが実行された時、gameインスタンスを生成し、
# play_game関数を呼び出してゲームをスタートする
if __name__ == "__main__":
    game = Game()
    game.play_game()

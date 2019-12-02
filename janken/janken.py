import random


class Hand:

    def __init__(self, shape, stronger_than):
        self.shape = shape
        self.stronger_than = stronger_than

    def __repr__(self):
        return self.shape

    def is_stronger_than(self, enemy):
        return self.stronger_than == enemy.shape


ROCK = Hand("グー", "チョキ")
SCESSORS = Hand("チョキ", "パー")
PAPER = Hand("パー", "グー")


class Record:

    def __init__(self):
        self.win = 0
        self.lose = 0
        self.draw = 0

    def __str__(self):
        return f"{self.win}勝 {self.lose}敗 {self.draw}引き分け"


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = ROCK  # 最初はグー
        self.record = Record()

    def show_hand(self):
        print(f"{self.name}の手は{self.hand}")

    def show_record(self):
        print(f"戦績: {self.record}")

    def is_stronger_than(self, enemy):
        return self.hand.is_stronger_than(enemy.hand)

    def judge(self, enemy):
        if self.is_stronger_than(enemy):  # わての方があんたより強いねん
            print(f"{self.name}の勝ち！")
            self.record.win += 1
        elif enemy.is_stronger_than(self):  #  あんたの方がわてより強いだと！？
            print(f"{self.name}の負け＞＜")  # しゃーない、わての負けや
            self.record.lose += 1
        else:
            print("あいこ～")
            self.record.draw += 1


class Human(Player):
    HANDS = {0: ROCK, 1: SCESSORS, 2: PAPER}

    def select_hand(self):
        while True:
            try:
                hand = int(input(f"{self.name}の手は？ {self.HANDS} "))
                if hand in self.HANDS:
                    self.hand = self.HANDS[hand]
                    return
            except ValueError:
                pass
            print("無効な手です！0~2の数字で入力してください！")


class Computer(Player):
    HANDS = ROCK, SCESSORS, PAPER

    def select_hand(self):
        self.hand = random.choice(self.HANDS)


def main():
    you = Human("あなた")
    com = Computer("コンピューター")

    times = 0
    one_more_play = True
    while one_more_play:
        times += 1
        print(f"ジャンケン{times}回目")

        com.select_hand()
        you.select_hand()
        com.show_hand()
        you.judge(com)
        you.show_record()

        one_more_play = input("もう一度やる？ １:やる！ 0：もうええわ > ") == '1'

if __name__ == "__main__":
    main()
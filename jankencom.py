# -*- coding: utf-8 -*-
# !/usr/bin/env python

import random
from enum import Enum, unique


@unique
class Result(Enum):
    draw = 'DRAW'
    win = 'You Win!!'
    lose = 'You lose!!'


@unique
class Hands(Enum):
    グー = '1'
    チョキ = '2'
    パー = '3'

    @classmethod
    def get_random(cls):
        values = list(map(lambda c: c.value, cls))
        value = random.choice(values)
        return Hands(value)


def janken(user_input):

    user_hand: Hands = Hands(user_input)

    pc_hand: Hands = Hands.get_random()

    judge: Result

    if user_hand is pc_hand:
        judge = Result.draw
    else:
        if user_hand is Hands.グー:
            judge = Result.win if (pc_hand == Hands.チョキ) else Result.lose

        elif user_hand is Hands.チョキ:
            judge = Result.win if (pc_hand == Hands.パー) else Result.lose

        else:
            judge = Result.win if (pc_hand == Hands.グー) else Result.lose

    print(u"あなたが選んだのは %s" % user_hand.name)
    print(u"コンピュータが選んだのは %s" % pc_hand.name)
    print(u"結果は%s\n"%judge.value)

    return judge


user_win = 0

for i in range(3):
    print (u"じゃーんけーん")
    print (u"1=グー　2=チョキ　3=パー　を入力")
    user = input('>>>  ')

    try:
        result: Result = janken(user)
        if result == Result.win:
            user_win += 1
    except:
        print(u"1か２か３を入力してください。")

print(u"\n\nあなたの勝利回数: %s回"%user_win)


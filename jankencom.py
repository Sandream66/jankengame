# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import random

dic = {"1":"グー","2":"チョキ","3":"パー"}

print (u"じゃーんけーん")
print (u"1=グー　2=チョキ　3=パー　を入力")
user = input('>>>  ')

try:
    user_choice = dic[user]
    
    choice_list = ['1','2','3']
    pc = dic[random.choice(choice_list)]
    
    draw = 'DRAW'
    win = 'You Win!!'
    lose = 'You lose!!'
    
    if user_choice == pc:
        judge = draw
    else:
        if user_choice == "グー":
            if pc == "チョキ":
                judge = win
            else:
                judge = lose
                
        elif user_choice == "チョキ":
            if pc == "パー":
                judge = win
            else:
                judge = lose
                
        else:
            if pc == u"グー":
                judge = win
            else:
                judge = lose
    
    print(u"あなた選んだのは %s"%user_choice)
    print(u"コンピュータが選んだのは %s"%pc)
    print(u"結果は%s"%judge)
except:
    print(u"1か２か３を入力してください。")
import random

colors = ['Red', 'Yellow', 'Blue', 'Green']
specials = ['Skip', 'Reverse', 'Draw Two']
numbers = list(range(10)) + list(range(1, 10))
wilds = ['wild', 'Wild Draw Four']
values = numbers+specials
deck=[[color,value]for color in colors for value in values]+4*wilds
random.shuffle(deck)

while True:
    count = input("number of players:")
    if not count.isdecimal():
        print("Wrong numbers")
        continue
    player_count=int(count)
    if player_count<2 or player_count>10:
        print("Wrong numbers")
        continue
    break
from random import choice
for i in range(1,player_count+1):
    print(f'\nplayer {i}:')
    for _ in range(7):
        print(deck.pop())



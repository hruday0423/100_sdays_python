import random

from defer import return_value

number_list=[]
for i in range(1,101):
    number_list.append(i)
number= int(random.choice(number_list))
game_level = input('enter level: easy or hard  ')
game_on = True

if game_level=="easy":
    lives= 10
elif game_level=="hard":
    lives= 5
else:
    print('please enter a valid input')
while game_on:
    if lives>0:
        guess= int(input('guess the number between 1 and 100: '))
        if guess<number:
            print('number is low')
            lives-=1
            print(f'you haves {lives} lives remaining')
        elif guess> number:
            lives-=1
            print('number is high')
            print(f'you haves {lives} lives remaining')
        elif guess==number:
             print('perfect!! your guess is correct with {lives) remaining')
    else:
        print('you lost')
        game_on= False


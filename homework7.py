import random
computer_num=random.randint(1,100)
games_count=4
while games_count!=0:
    user_input = int(input('try to guess the number: '))
    if user_input == computer_num:
        print('Good job!!!')
    elif user_input > computer_num:
        print('yor number is bigger')
    elif user_input < computer_num:
        print('yor number is smaller')
        games_count-=1
    user_input = int(input('try to guess the number: '))
    if user_input == computer_num:
        print('Good job!!!')
    elif user_input > computer_num:
        print('yor number is bigger')
    elif user_input < computer_num:
        print('yor number is smaller')
        games_count -= 1
    user_input = int(input('try to guess the number: '))
    if user_input == computer_num:
        print('Good job!!!')
    elif user_input > computer_num:
        print('yor number is bigger')
    elif user_input < computer_num:
        print('yor number is smaller')
        games_count -= 1
        break



games_count=int(input('how many games wanna play:'))
print(f'Ok, ypu are about to play{games_count}games...')
print('Please enter for Rock:0, Paper:1, Scissors:2')

user_wins=0

while games_count !=0
    user_input=int(input('plese make your choice:'))
    comp_choice=random.randint(0,2)

    if user_input==0:
        if user_input==comp_choice and comp_choice==1:
            games_count-=1
            continue
        if comp_choice==2:
            user_wins+=1
            continue

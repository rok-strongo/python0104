user_input_1=int(input("input first num:"))
user_input_2=int(input("input second num:"))
user_input_3=int(input("input third num:"))
user_input_4=int(input("input fourth num:"))

if user_input_1%2!=0 and user_input_2%2!=0 and user_input_3%2!=0 and user_input_4%2!=0:
    print('not found')
else:
    while max(user_input_1,user_input_2,user_input_3,user_input_4)%2!= 0:
        if max(user_input_1,user_input_2,user_input_3,user_input_4) == user_input_1 and user_input_1 % 2 != 0:
            user_input_1 = 0
            continue
        if max(user_input_1,user_input_2,user_input_3,user_input_4) == user_input_2 and user_input_2 % 2 != 0:
            user_input_2 = 0
            continue
        if max(user_input_1,user_input_2,user_input_3,user_input_4) == user_input_3 and user_input_3 % 2 != 0:
            user_input_3 = 0
            continue
        if max(user_input_1,user_input_2,user_input_3,user_input_4) == user_input_4 and user_input_4 % 2 != 0:
            user_input_4 = 0
            continue
    else:
        print(max(user_input_1,user_input_2,user_input_3,user_input_4))
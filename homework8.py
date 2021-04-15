num_1=int(input('input four-digit number:'))
string_1=str(num_1)
string_2=sorted(string_1)

if list(string_1)==string_2:
    print('Right')
elif list(string_1)!=string_2:
    print('Wrong')




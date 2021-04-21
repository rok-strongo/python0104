user_input_1=int(input("input deposit amount:"))
user_input_2=int(input("input annual percent:"))
result=user_input_1+(user_input_1/100)*(user_input_2*5) # формула расчета суммы с процентами
print(f"total ammount:{result}")



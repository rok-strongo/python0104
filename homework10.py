test_str_1 = "  Hello world   this is   me   "
test_str_2 = "Hello world   this is   me again   "
test_str_3 = "      "
test_str_4 = "   Hello world   this is  not actually me   :)"

result_1=test_str_1.strip()
result_2=test_str_2.strip()
result_3=test_str_3.strip()
result_4=test_str_4.strip()

while "  " in result_1:
    result_1=result_1.replace("  "," ")
while "  " in result_2:
    result_2=result_2.replace("  "," ")
while "  " in result_3:
    result_3=result_3.replace("  "," ")
while "  " in result_4:
    result_4=result_4.replace("  "," ")

print(result_1)
print(result_2)
print(result_3)
print(result_4)

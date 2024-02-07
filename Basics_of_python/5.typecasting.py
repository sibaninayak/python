#it helps to convert a data type to another data type
a = 4
b = 5
c = 6
str_a = str(a)
str_b = str(b)
str_c = str(c)

finalString = str_a + str_b + str_c
finalInt = int(finalString)
print("final string is :" , finalInt , type(finalInt))
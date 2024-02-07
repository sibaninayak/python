#?1
# salary = int(input("enter your salary:"))
# year = int(input("enter how many year you worked:"))

# if year > 5:
#     bonus = 5 * salary
#     print("your net bonus amount is:" , bonus)
# else:
#     print("no bonus")

#?2
# length = int(input("enter length:"))
# breadth = int(input("enter breadth:"))

# if length == breadth:
#     print("it is a square")
# else:
#     print("it is not a square")

#?3
# int1 = int(input("enter first number:"))
# int2 = int(input("enter secend number:"))

# if int1>int2:
#     print(int1 ,"int1 is greater")
# else:
#     print(int2 , "int2 is greater")

#?4
# quantity = int(input("enter your cost price:"))

# if quantity*100 > 1000:
#     print("cost price is :" ,(quantity*100)-(10/100*quantity*100))
# else:
#     print("no discount.cost price is:" ,quantity*100)

#?5
# age = int(input("enter your age:"))
# sex = (input("enter your sex m/f :"))
# maritial_status = input("are you married:")


# if sex == "f":
#     print("she will work only in urban areas")
# elif sex == "m" and age > 20 and age < 40:
#     print("he may work in anywhere")
# elif sex == "m" and age > 40 and age < 60 :
#     print("he will work in urban areas only!")
# else:
#     print("Error")

#?6
# year = int(input("enter year:"))
# century_year = 2000,1900,2100
# # year1 = ye
# # year2 = century_year/400
# if (year % 4 == 0) :
#     print("it is a leap year")
# elif (century_year % 400 == 0):
#     print("it is a century year")
# else:
#     print("error")

#?7

# number = input("enter a four digit number:")
# if number(-1):
#     print(number*-1)
# else:
#     print("error")
    
#?8
held = int(input("number of class held:"))
attended = int(input("number of class attended"))
attendence = attended/held * 100

if attendence > 75:
    print("he/she can enter the xm")
else:
    print("not")

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
# held = int(input("number of class held:"))
# attended = int(input("number of class attended"))
# attendence = attended/held * 100

# if attendence > 75:
#     print("he/she can enter the xm")
# else:
#     print("not")

#?9 loop
# for i in range(1,100):
#     print(i)

# for i in range(100,1 , -1):
#     print(i)

#?10 multiply
# x = int(input("enter any number:"))

# for i in range(1,11):
#     # print(i*x)
#     print(f'{i} X {x} = {i * x}')

#?11 sum using while
# x = int(input("enter any number:"))

# sum = 0
# i = 1
# while i <= x:
#     sum += i
#     i += 1

# print(sum)

#?12 factorial 
# x = int(input("enter any number:"))

# factorial = 1
# i = 1
# # while i <= x:
# #     factorial *= i
# #     i += 1

# for i in range(1,x+1):
#     factorial*= i

# print(factorial)

#?13 printing odd nd even numbers

# num = 1
# while num <= 20:
#     print(num)
#     num = num +2

#?14 natural nd whole numbers
    
# i = 0
# while i<= 10:
#     print(i)
#     i +=1

#?15 squares using while loop
i = 1
print("numbers\t\tsquares")
while i<=10:
    print(i,"\t\t",i**2)
    i+=1





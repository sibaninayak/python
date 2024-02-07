#?1
# num1 = int(input("enter first number:"))
# num2 = int(input("enter secend number:"))
# num3 = int(input("enter third number:"))

# if num1 > num2:
#     if num1 > num3:
#         print(num1,"num1 is greater")
#     else:
#         print(num3,"num3 is greatest")
# else:
#     if num2> num3:
#         print(num2,"num2 is greter")
#     else:
#         print(num3,"num3 is greater")

#?2
number = int(input("enter a postive intiger:"))

if number % 15 == 0:
    print("it is divisible by 15")
else:
    if number % 3 == 0 or number % 5 == 0:
        print("this is divisible by 3 and 5")
    else:
        print("it is not divisible by 3 nor 5!")

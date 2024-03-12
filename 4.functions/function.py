def hello():
    print("hello kitty!")

hello()   #we have to call the function name in last to print the statement

#?sum of two numbers
def add(n1 ,n2=0) :  #add(parameter)
    sum = n1 + n2
    return sum
x = 7
y = 8
# print(add(x,y))  #add(argument)
#?positional argument
# print("the sum of two number is :", add(2,3)) 

#?keyword arguments(named arguments)
# print("the sum of two number is :", add(n1=2,n2=3)) 

#?default arguments
# print("the sum of two number is :", add(2)) 

#?ex
# def calcNum(x,y):
#     return x+y

# sum = calcNum(6,7)
# print(sum)

#?arbitary arguments
# def addallNumbers(*args):  #many number for addition
#     sum = 0
#     for i in args:
#         sum+=i
#     return sum
# output = addallNumbers(2,3,4,5,6,7,8,9,1)
# print(output)

#?key value arguments **kwargs
# def studentinfo(**kwargs):
#     for x,y in kwargs.items():
#         print(x,"is",y)

# studentinfo(name ="kitty", age = 21 , city = "southkorea")
# studentinfo(name ="lucky", age = 26 , city = "southafrica")

#?1 average of 3 numbers
# def avg(a,b,c):
#     if a == b :
#         print("a is greater")

#     sum = a+b+c
#     avg = sum/3
#     # print(avg)
#     return avg

# total = avg(90,89,95)
# print(total)

#?2 printing numbers in a list
# bts = ["rm","jin","suga","hobi","jimin","v","jk"]

# def length(bts):
#     # print(len(bts))
#     # return bts
#     for i in bts:
#         print(i , end=" ")

# length(bts)

#?3 factorial
# def fact(n):
#     factorial = 1
#     # for i in range(1,n+1):
#     #      factorial *=i

#     i = 1
#     while i <= n:
#         factorial *=i
#         i+=1

#     print( factorial)

# fact(int(input("enter any number:")))

#?4 usd to inr
# def convert(usd_val):
#     inr_val = usd_val*83
#     print(usd_val , "usd =" ,inr_val ,"inr")

# convert(50)

#?5 inr to usd
# def convert(inr_val):
#     usd_val = inr_val/83
#     print(inr_val , "inr =" , usd_val ,"usd")

# convert(int(input("enter inr val:")))


#?6 odd & even
# def odd_even(x):
    
#     if x%2 == 0:
#         # print("EVEN")
#         return "even"
#     else:
#         print("odd")

# num = int(input("enter any number:"))
# odd_even(num) 






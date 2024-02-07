# x = 0

# while x <= 50 :
#     print(x)
#     x +=5

#?2
# x = 5
# y = 0

# while x >= 0 :
#     if x == y:
#         break
#     else:
#         print(x,y)
    
#     x -= 1
#     y += 1

#?3
# name = ""

# while len(name) == 0:
#     name = input("enter your name:")

# print("hello "+name)

#?4
# while True:
#     name = input("enter your name:")
#     if name != "":
#         break


#?5
# number = "123-456-789"

# for i in number:
#     if i == "-":
#         continue
#     print(i , end="")

# for i in range(1 , 25):
#     if i == 17:
#         pass
#     else:
#         print(i)

#?6
# n = int(input("Enter the number : "))
# a = 1 
# while (a<=10):  
#   print(f"{n} X {a} = {n*a}") 
# # a * 1

#?7
# num = int(input("enter any number: "))
# prime = True

# for i in range(2,num):
#     if (num%i == 0):
#         prime = False
#         break 

# if prime:
#     print("this is a prime number")
# else:
#     print("this is not a prime number")

#?8
# num = int(input("enter any number: "))
# factorial = 1

# for i in range(1 , num+1):
#     factorial = factorial * i
    
# print(f"factorial of {num} is {factorial}")

#?9
# i = 1
# while i <= 100:
#     print(i)
#     i+=1

#?10
# i = 100
# while i >=1:
#     print(i)
#     i-=1 

#?11
# heroes = ["ironman","thor","spiderman","hulk","captain america","hawkaye"]

# indx = 0
# while indx < len(heroes):
#     print(heroes[indx])
#     indx +=1

#?12 searching number x in tuple
# nums = (2,4,6,8,24,36,56,68,45,90)

# i = 0 #index/initialize
# x = int(input("enter your number:"))
# while i < len(nums):
#     if nums[i] == x:
#         print("found x in" ,i )
#     # else:
#     #     print("not found")
#     i +=1

#?13 odd or even
i = 1
while i< 50:
    if i%2 != 0:
        i+=1
        continue
    print(i)
    i+=1

    
    










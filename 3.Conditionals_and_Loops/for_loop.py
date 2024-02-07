#range(start,stop)
#?in place of i we can use anything
# for i in range(1,11):
#     print(i ,"hello kittyyy!")

 #range(start,stop,step -> step means it will + from the nmbr)
# for i in range(1,11,2):
#     print(i ,"hello kittyyy!")

#?2
# list = [1,2,3,4,5,6,7]
# bts = ["rm" , "jin" , "suga" , "hope" , "jimin" , "v" , "jk"]

# for i in bts:
#     print(i)

#?3
# n = int(input("enter n :"))

# for i in range(n):
#     print("*" * 7)

#?4
# n = int(input("enter n :"))

# for i in range(n): #? i for rows 
#     for j in range(1,n+1):  #? j for column
#         print(j , end="")
#     print()

#?5
# n = (input("enter n:"))

# for i in range(1 , n+1):
#     for j in range(1 , i +1):
#         print(j , end="")
#     print()

#?6
# n = int(input("enter n:"))

# for i in range(1 , n+1):
#     print(" " * (n-i) , end="")
#     for j in range(1 , 2*i):
#         print(j , end="")
#     print()

#?7 
# num = int(input("enter any number:"))
# for i in range(1,11):
    # print(f"{num}X{i} = {num*i}")
    # print(str(num) + " X " + str(i) " = " + str(num * i))
     
#?8

l1 = ["sibani","sasmita","lucky","balram"]
for i in l1:
    if i.startswith("s"):
        print("hello "+ i)
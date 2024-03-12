#recursion means when a function calls itself repetedly
# def num(n):
#     if n==0:
#         return
#     print(n)
#     num(n-1)
# num(5)

#?1 factorial of 
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# num = int(input("enter any number:"))
# print(factorial(num))

#? first n natural numbers
# def natural(n):
#     if n == 0:
#         return 0
#     else:
#         return natural(n-1) + 1
    
# sum = natural(10)
# print(sum)

#? list print
# def print_x(list,idx=0):
#     if idx == len(list):
#         return
#     print(list[idx])
#     print_x(list,idx+1)

# names = ["sibani","lucky","kitty"]
# print_x(names)

#? print n to 1
# def print_nto1(n):
#     if n == 0:
#         return
    

#     print_nto1(n-1) 
#     print(n)

# print_nto1(7)

#? sum of no n
# def sum(n):
#     if n == 1:
#         return 1
    
#     ans = n + sum(n-1)
#     return ans

# print(sum(4))

#? power 
# def power(a,b):
#     if b == 0:
#         return 1
    
#     ans = a * power(a,b-1)
#     return ans

# a = int(input("enter a:"))
# b = int(input("enter b:"))

# print(power(a,b))

#?fibbonnacci
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("enter n:"))
for i in range(1, n+1):
    print(fibonacci(i)) 

print(fibonacci(4)) 


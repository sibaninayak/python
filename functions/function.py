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

#?arbitary arguments
# def addallNumbers(*args):  #many number for addition
#     sum = 0
#     for i in args:
#         sum+=i
#     return sum
# output = addallNumbers(2,3,4,5,6,7,8,9,1)
# print(output)

#key value arguments **kwargs
def studentinfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)

studentinfo(name ="kitty", age = 21 , city = "southkorea")
studentinfo(name ="lucky", age = 26 , city = "southafrica")

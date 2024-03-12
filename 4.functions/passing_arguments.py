
#?pass by arguments (immutable object : string ,tuple,intiger,float)
# def addOne(x):    #we pass copy it will not effect outer object
#     x = x+1
#     print("inner function :" , x)

# x = 5
# addOne(x)
# print("outer function:" , x)

#?pass by refrence (mutable object : list , dict)
def function(list):     #here refrence which will effect outer object
    # list.append(5)
    list = [5,6,7,8]
    print("inner",list)

list = [1,2,3,4]
function(list)
print("outer",list)

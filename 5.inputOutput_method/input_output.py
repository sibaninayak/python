
#?read
f = open("5.inputOutput_method./text.txt" , "a")
# data = f.read()
# print(data)
# print(type(data))
#?if we print read with readline then it will not print readline

#?readline
# line1 = f.readline()
# print(line1)
# line1 = f.readline()
# print(line1)

#?write
#?if we use 'w(overwrite)' then it will rewrite the sentence,if we use 'a(append)' then it will add/append at the last
# f.write("\nAfter that i will learn ReactJS")

#?by this we can create and write in that file(doesnt exist file by w and a)
f1 = open("5.inputOutput_method./sample.txt" , "w+")

#?r+ , w+ , a+
# f1.write("abc") #it will replace in first
# print(f1.read())
# f1.write("abc")

f.close()

#?with

# with open("5.inputOutput_method./text.txt" , "r") as f:
#     data = f.read()
#     print(data)

# with open("5.inputOutput_method./text.txt" , "a") as f:
#     data = f.write("\n after compleating react js i will learn node JS")

#?remove
# import os

# os.remove("5.inputOutput_method./text.txt")

#?example
word = "xlearning"
with open("5.inputOutput_method./practice.txt" , "r") as f:
    # f.write("\ni like programming in java")
    data = f.read()
    # if word in data:
    #     print("found")
    # else:
    #     print("not found")

# x = data.replace("java","python")

# print(x)

# with open("5.inputOutput_method./practice.txt" , "w") as f:
#     f.write(x)    
        
#?
# def check_data():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("5.inputOutput_method./practice.txt" , "r") as f:
#         while data:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#                 return
#             line_no+=1

#     return -1

# check_data()
    
#?checking even odd
i = 0
with open("5.inputOutput_method./practice.txt" , "r") as f:
    data = f.read()

        
    nums = data.split(",")
    for val in nums:
        if (int(val) %2 == 0):
            i+=1
print(i)




    
    
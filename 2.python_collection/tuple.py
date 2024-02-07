colors = ("purple","black","blue","white")
# print(colors)
# print(colors[2]) #indexing start from 0
# print(colors[-2]) #negetive indexing starts backwards from -1
# print(colors[1:3]) #sublist - we have to give range 3 for 2 items
# print(colors[-3:-1])

#?creating a tuple with one item
# fruits = ("apple" , ) #we have to give a , or it will take as a string
# fruit = tuple("apple")

# print(type(fruits))
# print(len(fruits))

#? reverse tuple
# input_tuple = (1,2,3,4,5,6)
# list = []

# for x in reversed(input_tuple ):
#     list.append(x)

# output_tuple = tuple(list)
# print(output_tuple)

student = ("sibani" , 21 , "female")

print(student)
print(student.count("sibani"))
print(student.index(21))

for i in student:
    print(i)

if "sibani" in student :
    print("sibani is here!")
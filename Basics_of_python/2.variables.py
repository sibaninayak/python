#string
name = "sibani"
print(type(name))

#integer
roll_no = 7
print(type(roll_no))

#floating numbers
percentage = 90.5
print(type(percentage))

#boolean
is_student = True
print(type(is_student))

#print(name,roll_no,percentage,is_student)

#we can also print these varibles in sentence
#?print("my name is" + name "my roll no is" + roll_no) 
#it will through a error because we can use + sign in if the data type is same if not then we can use a ,
print("my name is "  +  name +  " my roll no is" , roll_no) 
print('i secured ', percentage ,"% in board" , "and im a " , is_student )

#we can also update the variable
percentage = 88.9
#print(name,roll_no,percentage,is_student)
print("my current percentage is ", percentage - 4.6 )

#print with seperator
print(name,roll_no,percentage,is_student, sep="-")
a = 1
b = 2
c = 3
print(a,b,c,sep="->")


#multiple Assignment
name , age , attractive = "sibani" , 21 , True
print(name,age,attractive)

# kityy = 21
# sibani = 21
# lucky = 21
kityy=lucky=sibani=21

print(kityy,lucky,sibani)

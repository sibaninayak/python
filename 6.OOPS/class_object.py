# class student:    #?class
#     name = "kitty"

# s1 = student()   #?object
# # print(s1)
# # print(s1.name)

# #?
# class student:
#     clg_name = "RIT"  #?class attribute
#     name = "lucky"
#      #object attribute > class attribute
#      #?default constructor
#     # def __init__(self) -> None:
#     #     pass
#     #?parametarized constructor
#     def __init__(self,name,age):
#         self.name = name   #?object attribute
#         self.age = age
        
# s1 = student("kitty",21)
# print(s1.name)
# print(s1.age)
# s1.marks = 45  #?instance attribute
# print(s1.marks)
# print(s1.name , s1.age)

# s2 = student("sibani",21)  #attribute values ex-name age like data
# # print(s2.name)
# # print(s2.age)
# # print(s2.name , s2.age)
# print(student.clg_name)  #we can print direct for class attribute

#?
# class Student:
#     def __init__(self,name,age):
#         self.name = name   #?object attribute
#         self.age = age

#     def hello(self):
#         print("hello" , self.name)

#     def age(self):
#         return self.age
    
# s1 = Student("kitty" , 21)
# s1.hello()
# print(s1.age)

#?average of 3 students
# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         i = 0
#         for val in self.marks:
#             i += val
#         print("hi" , self.name , "your avg score is:" , i/3)
        
# s1 = student("kitty" , [86,90,89])
# s1.average()

# s1.name = "sibani"  #we can change direct attribute value also
# s1.average()

#?rectangle
# class Rectangle:
#     def __init__(self,height,width):
#         self.height = height
#         self.width = width

#     def area(self):
#         return self.height* self.width
    
#     def perimeter(self):
#         return (self.height + self.width) * 2
    
# h = int(input("enter height:"))
# w = int(input("enter width:"))
# rec = Rectangle(h,w)
# # rec.set_dimension(h,w)
# print(rec.area())
# print(rec.perimeter())

#?credit and debit
class Account:
    def __init__(self,bal,acc_no):
        self.bal = bal
        self.acc_no = acc_no

    def debit(self,amount):
        self.bal -= amount
        print("Rs" , amount,"was debited")
        print("your total balance is:" , self.total_amount())

    def credit(self,amount):
        self.bal += amount
        print("Rs" , amount,"credited")
        print("your total balance is:" , self.total_amount())

    def total_amount(self):
        return self.bal

# acc = Account(10000,"kitty")
# acc.debit(5000)
# acc.credit(1000)
# acc.credit(60000)
# print(acc.bal)




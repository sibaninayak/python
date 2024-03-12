
#?static method
class student:

    @staticmethod
    def hello():
        print("hello kitty")
    
#     def __init__(self,name,age):
#         self.name = name   #?object attribute
#         self.age = age
    
        
# s1 = student("kitty",21)
# print(s1.name)
# print(s1.age)
        
#?class method
class Person:
    name = "sibani nayak"

    # def Pname(self,name):
    #     # self.name = name
    #     # Person.name = "kitttyyy"
    #     self.__class__.name = name   #we cant access class name by these three methods

    @classmethod
    def Pname(cls , name):
        cls.name = name

# p1 = Person()
# p1.Pname("kitty")
# print(p1.name)

#?property decorator
class Student():
    def __init__(self,phy,math,eng):
        self.phy = phy
        self.math = math
        self.eng = eng
        # self.percentage = str((self.eng + self.phy + self.math) / 3) #this is one method to calculate

    #if we change marks
    # def calcPercentage(self):
    #     self.percentage = str((self.eng + self.phy + self.math) / 3)"%"

    #by this method we can call directly  
    @property
    def percentage(self):
        return str((self.eng + self.phy + self.math) / 3 ) + "%" 

s1 = Student(94,56,78)
s1.phy = 87
# print(s1.phy)
# s1.calcPercentage()
print(s1.percentage)

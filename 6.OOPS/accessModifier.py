
#?public modifier
#we can access data in public modifier
class Modifier:
    def __init__(self):
        self.publicModifier = None

    def publicModifier(self):
        pass

obj = Modifier()
# print(obj.publicModifier)

#?private modifier
#we cant access data here it will through attribute error
# class Modifier:
#     def __init__(self):
#         self.__PrivateModifier = None

#     def __PrivateModifier(self):
#         pass

# obj = Modifier()
# print(obj.__PrivateModifier)

class student:
    __name = "kitty"

    def __hello(self):  #we cant access data from method in private
        print("hello kitty")

    def hi(self):   
        self.__hello()   #but inside the function we can call the method it will print the data

s1 = student()
print(s1.hi())


#?protector modifier
#it will access from inside the class or sub class
# class Modifier:
#     def __init__(self):
#         self._protectModifier = None

#     def _protectModifier(self):
#         pass

# obj = Modifier()
# print(obj._protectModifier)

#?del
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# s1 = Student("sibani", 21)
# del s1.age
# print(s1.name)
# print(s1.age)




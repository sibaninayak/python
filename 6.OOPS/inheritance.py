
#?single inheritance(single parent class and single child class)
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class Newcar(Car):
    def __init__(self,name):
        self.name = name
  

car1 = Newcar("porsche")
# print(car1.stop())

#?multilevel inheritance(multiple child)

class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class Newcar(Car):
    def __init__(self,name):
        self.name = name

class Fortuner(Newcar):
    def __init__(self,color):
        self.color = color

car1 = Fortuner("red")
# print(car1.start())  

#?multiple inheritance(two multiple parents)
class A:
    varA = "wecome to class A"

class B:
    varB = "welcome to class B"

class C(A,B): 
    varC = "welcome to class C"

cl = C()  #we can inherit from c of class a nd b
# print(cl.varA)
# print(cl.varB)
# print(cl.varC)

#?super() method
class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class Newcar(Car):
    def __init__(self,name,type):
        self.name = name
        #to call a parent method here we use super
        super().__init__(type)
        super().start()

car1 = Newcar("fortuner" ,"engine")
# print(car1.type)

#?ex
class Vehical:
    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity

    def fare_charge(self):
        return self.seating_capacity*100

class Bus(Vehical):
    def __init__(self,seating_capacity):
        super().__init__(seating_capacity)

    def fare_charge(self):
        vehical_fare = super().fare_charge()
        matainence_fare = 0.1 * vehical_fare
        total_fare = matainence_fare + vehical_fare
        return total_fare
    
vehical1 = Vehical(50)
print("vaheical fare is:" , vehical1.fare_charge())

bus1 = Bus(50)
print("bus fare is:" , bus1.fare_charge())
    
        



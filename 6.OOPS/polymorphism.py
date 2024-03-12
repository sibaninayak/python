
#?complex method
#? __ dunder function
#?add
class Complex:
    def __init__(self,real,img):
        self.real =real
        self.img = img

    def show(self):
        print(self.real,("i +") ,self.img,("j") )

    #for adding
    def __add__(self,num):
        real = self.real + num.real
        img = self.img + num.img
        return Complex(real,img)

# num1 = Complex(3,4)
# num1.show()

# num2 = Complex(9,6)
# num2.show()

# num3 = num1 + num2
# num3.show()

#?subtract
class Complex:
    def __init__(self,real,img):
        self.real =real
        self.img = img

    def show(self):
        print(self.real,("i +") ,self.img,("j") )

    #for subtraction
    def __sub__(self,num):
        real = self.real - num.real
        img = self.img - num.img
        return Complex(real,img)

# num1 = Complex(10,9)
# num1.show()

# num2 = Complex(9,6)
# num2.show()

# num3 = num1 - num2
# num3.show()
    
#?multiply
class Complex:
    def __init__(self,real,img):
        self.real =real
        self.img = img

    def show(self):
        print(self.real,("i +") ,self.img,("j") )

    #for adding
    def __mul__(self,num):
        real = self.real * num.real
        img = self.img * num.img
        return Complex(real,img)

# num1 = Complex(3,4)
# num1.show()

# num2 = Complex(9,6)
# num2.show()

# num3 = num1 * num2
# num3.show()
    
#?division
class Complex:
    def __init__(self,real,img):
        self.real =real
        self.img = img

    def show(self):
        print(self.real,("i +") ,self.img,("j") )

    #for adding
    def __truediv__(self,num):
        real = self.real / num.real
        img = self.img / num.img
        return Complex(real,img)

# num1 = Complex(3,4)
# num1.show()

# num2 = Complex(9,6)
# num2.show()

# num3 = num1 / num2
# num3.show()

#?modulo
class Complex:
    def __init__(self,real,img):
        self.real =real
        self.img = img

    def show(self):
        print(self.real,("i +") ,self.img,("j") )

    #for adding
    def __mod__(self,num):
        real = self.real % num.real
        img = self.img % num.img
        return Complex(real,img)

# num1 = Complex(3,4)
# num1.show()

# num2 = Complex(9,6)
# num2.show()

# num3 = num1 % num2
# num3.show()
    
#?greater then
class Order():
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price
    
odr1 = Order("chips",10)
odr2 = Order("drink" , 20)

print(odr1 > odr2)
    
#?ex (circle)
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return (22/7) * self.radius ** 2
    
    def Perimeter(self):
        return 2 * (22/7) +self.radius

        
# r = Circle(21)
# print(r.Area())
# print(r.Perimeter())
    
#?employee
class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("role = " ,self.role)
        print("department = ",self.department)
        print("salary = ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("accountant","cse","70,000")


# e1 = Engineer("sibani","21")
# e1.showDetails()




a = int(input("anter a:"))
b = int(input("enter b:"))

try:
    result = a/b
except ZeroDivisionError:
    result = None
    print("cannot divide by zero")
finally:
    print("the result is:" , result)

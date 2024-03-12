def outer_function():
    x = int(input("enter x:"))

    def inner_function():
        y = int(input("enter y:"))
        result = x+y
        return result
    
    return inner_function()

output = outer_function()
print(output)
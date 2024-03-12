name = "kitty"   #global scope(available outside & inside the function)

def output():
    name = "sibani nayak"   #local scope(available only inside the function)
    print(name)

output()
print(name)
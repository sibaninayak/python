name = "sibani nayak"

if(name[0].islower()):
    name = name.capitalize()

first_name = name[:6].upper()
last_name = name[7:].lower()
last_char = name[-1]  #negetive indexing start from last

print(name)
print(first_name)
print(last_name)
print(last_char)


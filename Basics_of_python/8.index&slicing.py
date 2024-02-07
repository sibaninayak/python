#indexing[] & slicing()
#[start:stop:step]

#?index
name = "sibani nayak"
print(name[0])
print(name[0:5]) #the index number starts from 0 in python but here the last number is exclusive so it takes another number +1
print(name[6]) #space
print(name[6:12])
print(name[::]) #if we leave empty then python will take from 0 index to last index
print(name[0:12:2])#it will print first index to 2nd index number of each
print(name[::-1]) #negetive - reverse

#?slicing
website = "http://google.com"
slice = slice(7,-4)

print(website[slice])
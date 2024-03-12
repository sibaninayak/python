# str = 'sibani'
# str = """kitty"""
str = "my name is kitty.\nim a good girl!" #for next line we use \n
# print(str)

#?concatination
str1 = "sibani"
str2 = "nayak"
# print(str1 + str2)
# final_str = str1 + str2
# final_str = str1 + " " + str2 #for space we can use " "
# print(final_str)

#?length
# print(len(str1))
# print(len(str2))
# print(len(final_str)) #it also check the length of space

#? indexing
# ch = str1[0] #indexing start from 0
# print(ch)

#? string function
name = "      sibani!         "
# print(name)
# print(len(name))
# print(name.find("s"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.count("i"))
# print(name.isalpha())
# # print(name.replace("s","k"))
# print(name.strip())
# print(name)
# print(name*3)


#? format string
name = "sibani"
char = "good"

# print("my name is" + " " + name + " " + "im a" + " " + char + " " + "girl")
# print("my name is {} and im a {} girl" . format('sibani' , 'good'))
# print("my name is {1} and im a {0} girl" . format(name , char))  #positional argument
# print("my name is {name} and im a {char} girl" . format(name = "kitty" , char = "good")) #keyword argument

# text = "my name is {} and im a {} girl"
# print(text.format(name,char))

#?space padding
# print("my name is {} " . format(name))
# print("my name is {:10}.thank you " . format(name))  #for space 
# print("my name is {:>10}.thank you " . format(name))
# print("my name is {:<10}.thank you " . format(name))
# print("my name is {:^10}.thank you " . format(name))  #center

#?number
# num = 42.76890
num = 10000

# print("my number is {:.2f}".format(num))  #floating number
# print("my number is {:,}".format(num)) 
# print("my number is {:b}".format(num)) #boolean
# print("my number is {:o}".format(num))  #octal
# print("my number is {:X}".format(num))  #hexadecimal
# print("my number is {:E}".format(num)) #sceintific notation

#? Traversing a string
name = "sibani nayak"
# for i in name:
#     print(i)

#?list comperhension
# list = [char for char in name]
# for i in list:
#     print(i)

#?exxample
text = "the unexpected always happen"
print(text)
print(len(text))
print(text.find("pp"))
print(text[:11])
print(text.replace("always" , "never"))
text2 = "no matter what"
text3 = text +" "+ text2
print(text3)
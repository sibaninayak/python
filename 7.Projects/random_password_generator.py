import  random
import string

password_len = 12
char_values = string.ascii_letters + string.digits + string.punctuation

password = ""
# for i in range(password_len):
#     password += random.choice(char_values)

# print("your random password is:",password)

#?by using list comphersion
# res = [random.choice(char_values)for i in range(password_len)]
# print(res)
#?for concatenate the list
password ="".join([random.choice(char_values)for i in range(password_len)])
print("your random password is:",password)
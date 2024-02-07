bts = ["rm" , "jin" , "suga" , "hobi" , "jimin" , "v" , "jk"]
bts[3] = "jhope"  #mutable
# print(bts)
# print(bts[2]) #indexing start from 0
# print(bts[-2]) #negetive indexing starts backwards from -1
# print(bts[1:3]) #sublist - we have to give range 3 for 2 items
# print(bts[-3:-1])

# bts.append("kitty")
# bts.insert(2,"yoongi")
# bangtan = ["kitty" , "sibani"]
# bts.extend(bangtan)
# print(bts)
# bts.pop() #it will remove the last element , if we will give index number then it will pop that out
# bts.remove("suga")
# bts.sort() #ascending
bts.sort(reverse=True) #descending
bts.reverse()
# bts.clear()
# print(bts)

# bts[1:3] = ["jinsuga"] 
# print(bts)
# print(type(bts))
# print(len(bts))

# for i in bts:
#     print(i)

#?2d list
# rapper = ["namjoon","suga" , "jhope"]
# vocal = ["jimin" , "jin" ,"tae" , "jungkook"]

# bangtans = [rapper,vocal]
# print(bangtans[1])
# print(bangtans[0] [1])

#?list comprehension
# newBts = [Bts for Bts in bts if "j" in Bts]
# print(newBts)

# newBts = bts.copy()
# print(newBts)

#?nested list
# bts.insert(2,["yoongi" , "hope"])
# print(bts[2] [0])


#? swapping numbers
# n = int(input("enter size of list:"))
# list = []

# for i in range(n):
#     num = int(input())
#     list.append(num)

# indx1 = int(input("enter indx1 : "))
# indx2 = int(input("enter indx2 : "))
# print(list)

# temp = list[indx1]
# list[indx1] = list[indx2]
# list[indx2] = temp

# print(list)

#?q1
# movies = []
# mov1 = input("enter your first movie name:")
# mov2 = input("enter your secend movie name:")
# mov3 = input("enter your third movie name:")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

#?palindrome
l1 = [1,2,3]

copy_l1 = l1.copy()
copy_l1.reverse()

if copy_l1 == l1:
    print("palindrome")
else:
    print("not palindrome")

#?unorderd , unindexing
name = {"kitty" , "sibani" ,"lucky"}

# print(name)
# print(type(name))
# print(len(name))

#?accesing name from the set
# for i in name:
#     print(i)

#?checking item exist in set
# if "kitty" in name:
#     print("kitty is a set")

#?add element in set
# name.add("v")
# print(name)

#?adding sequence in a set
# list = ["jk" , "rm"]
# name.update(list)
# print(name)

#?removing element
# name.remove("sibani")
# name.discard("jimin") #it will not through an error if value is not present in the set
# print(name)

#?joining element in set
s1 = {"a","b","c"}
s2 = {"d","e" ,"a"}
# print(s1,s2)

# s3 = s1.union(s2)
# print(s3)

# s1.update(s2)
# print(s1)

#?keep only duplicate value of set
# s1.intersection_update(s2)
# print(s1)

#?keep all value expect duplicate value
# s1.symmetric_difference_update(s2)
# print(s1)

#?q1
ar1 =  [1,5,10,20,40,80]
ar2 = [6,7,20,80,100]
ar3 = [3,4,15,20,30,70,80,120]

s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

s1s2 = s1.intersection(s2)
final = s1s2.intersection(s3)

final_list = list(final)
print(final_list)




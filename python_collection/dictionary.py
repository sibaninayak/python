#it is a key value pair
numbers = {
    "v" : 78695,
    "jk" : 78397,
    "jimin" : 76598,
}

# print(numbers)
# print(type(numbers))
# print(len(numbers))

#?for accesing one value
# print(numbers["jimin"])
# print(numbers.get("jin"))
# print(numbers.items())

#?printing key value pair
# print(numbers.keys())
# print(numbers.values())

# ?updating
# numbers["v"] = 5468342
# numbers.update({"suga" :2756985})  #byupdate method we can add value and update existing value also
# numbers.update({"v":834702})
# print(numbers)


#? adding
# numbers["hobi"] = 7843
# print(numbers)

# more_numbers = {
#     "hobi":7859907
# }

# numbers.update(more_numbers)
# print(numbers)

#?removing element
# numbers.pop("hobi")
# numbers.popitem()  # it will remove the last item
# print(numbers)

#?clearing all elements
# numbers.clear()
# print(numbers)

#?printing elements in dict
# for i in numbers.items():  #this will print key value pair
#     # print(i) #it will print only key 
#     # print(numbers[i]) #it will print only values
#     print(i)  

# for x,y in numbers.items():
#     print(x,y)  #it will print diffrent

#?printing nested dict
# phones = {
#     "maknae":{
#         "v":687997,
#         "jk":65869,
#         "jimin":3644767
#     },
#     "hyung":{
#         "rm":67480,
#         "jin":7846,
#         "suga":37678,
#         "hope":64767
#     }
# }
# print(phones["hyung"]["rm"])
# print(phones["maknae"]["v"])


#? adding in dict
# dict = {
#     "a" :100,
#     "b":200,
#     "c":300
# }
# # print(dict.values())
# print("the sum of dict is:",sum(dict.values()))

#?null dict
# null_dict = {}
# null_dict["name"] = "sibani nayak"
# print(null_dict)

#?practice qustnss
python_dict = {
    "cat" : "a small animal",
    "table" : ("a piece of furniture" , "list of packs & figures")

 }

# print(python_dict)

#?2
sets = {
    "python","java","c++","python","javascript","java","python","c"
    }
print(sets)
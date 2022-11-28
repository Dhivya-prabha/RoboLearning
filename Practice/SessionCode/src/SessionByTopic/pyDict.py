from fileinput import input
myDict = {"Name": "Babu", "Age": 35, "Gender" : "Male"}
print(myDict)

this_dict = {"Name": "Babu", "Age": 35, "Gender" : "Male", "Food":{"Morning":"Fruits", "Afternoon":"Veggies","Night":"Water"}}

print(this_dict["Food"]["Morning"])

print(this_dict.get("Name"))
print(this_dict.values())
this_dict["Name"] = "Raja"
print(this_dict)


this_dict["color"] = "Red"
print(this_dict)




print(this_dict.popitem())
print(this_dict)



d3 = this_dict

print(this_dict.update({"Name": "Manoj"}))
print(d3)

d3 = this_dict.copy()

dictionary = {"Mani":16, "Rocky":19}
search_age = input("Enter Age:")
for name, age in dictionary.items():
    if age == int(search_age):
        print(name)


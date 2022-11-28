from fileinput import input
d ={}
print(type(d))

Mydict = {"Name" :"Babu", "Age ": 35,"Gender ":"Male"}
Mydict["color"] = "red"
Mydict.update({"car":"Nexon"})
#del Mydict

print(Mydict)
this_dict = {"Name" :"Babu", "First Name" :"Babu", "Age ": 35,"Gender ":"Male", "Food":{"Morning": "Fruits", "Afternoon": "Veggies", "Night": "Water"}}
print("Values", this_dict.values())

n1 = input("Enter the key:")
this_dict = 

if "Age " in this_dict:
    print(this_dict["Age "])
else:
    
    print('No') 
    
    
for x in this_dict.keys():
    print(x)     
    
for x in this_dict.values():
    print(x)   
    
    
    
for x,y in this_dict.items():
    print(x," : ", y)  
    

#change the value
this_dict["Age "] = 30
print(this_dict)


#Add a value
Mydict["Place "] = "Coimbatore"
print(Mydict)

#Remove an item
Mydict.pop("Place ")
print(Mydict)


#Delete an item
#Mydict.clear()
#print(Mydict)


#Delete an item
#del Mydict
#print(Mydict)

print(len(Mydict))


dn = dict(Mydict)
print(dn)

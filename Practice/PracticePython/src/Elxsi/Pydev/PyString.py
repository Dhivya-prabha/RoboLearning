from asyncio.locks import Condition
txt = "I like Yellow. Yellow is perfect"
x = txt.replace("Yellow", "Red", 1)
print(x)

product = "Hp LapTop | 100000 | New"
name = product[:product.index("|"):]
print(name)
price = name = product[product.index("|")+1:product.rindex("|")]
print(price)
Condition = product[product.rindex("|")+1:]
print("Condition", Condition)

str = "Python"
print(str[0:4])
print(str[-4:-1])

print(str[:4])
print(str[3:])
print("Slicing with step",str[::3])

#Python string is immutable
for x in "banana":
  print(x)
  
txt = "The light heart lives long"
print("heart" in txt)
  

name = "Dhivya Prabha"
#Reverse Indexing

print('name in place: ',name[-12])

#Forward Index

print('name in place: ',name[12])

#Slicing
print(name[0:5])

print(name[-12:-7])

#If the starting index is missing, it will take 0
print(name[:-7])

#If the ending index is missing, it will take string length
print(name[-10:])


#string length
print(len(name))

#String Replace
print(name.replace('a', 'A', 2))

place = ' Coimbatore  '

print(place,'...')

#Remove white space
print(place.strip())


print(place.upper())
print(place.lower())

print(place.split('a'))























#Tuple is immutable
#Not possible to add, remove or change an element in tuple

MyTuple = ("apple", "banana", "cherry", "apple", "cherry")

print(MyTuple[1])

myList = list(MyTuple)
myList[1] = "kiwi"
newTuple = tuple(myList)
print(newTuple)

data = (10, 20, 30, 10 , 40, 10)
print(data.count(10))
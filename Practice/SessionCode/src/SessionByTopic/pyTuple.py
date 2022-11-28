MyTuple =("Apple", "Banana", "Cherry", "Apple", "Cherry")
print(MyTuple)
myList = list(MyTuple)
myList[1] = "Kiwi"
print(myList)
print(MyTuple.count("Apple"))

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1+tuple2
print(tuple3)

fruits = ("Apple", "Banana", "Cherry")
myFruits = fruits * 3
print(myFruits)
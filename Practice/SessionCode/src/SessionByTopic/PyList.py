from _operator import index
from setuptools._vendor.more_itertools.more import product_index
name = ["apple", "Orange", "Banana", "apple", 12]
print(len(name))

#for x in name:
   # print(x)
    
new = [2, 3, 4, 5, 6]
new[0] = 1
print(new)
print("index is ", new.index(6))
new[1:4] =[3, 5, 6]
print(new ,"1:4")

new.append(8)
print(new)

#new.extend([9, 10, 11])
x = (new+([9, 10, 11]))
print(x)

new.remove(3)

list1 = [[2,3], [3,4],[4,5]]
print(list1[0][0])
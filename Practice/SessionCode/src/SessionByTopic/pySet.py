from _ast import Set
from calendar import setfirstweekday
from _ctypes import Union
setData = {1, 2, 3, 4, 5, 3}
print(setData)

setData.add(6)
setData.update({7, 8})
print(setData)

newSet = {9, 10, 11, 12}
setData.update(newSet)
print(setData)

#setData.remove(8)
setData.discard(9)
print(setData)

UnionSet = {11, 12, 13, 14, 15}
#s1 = setData.union(UnionSet)
s1 = setData.intersection(UnionSet)
print(s1)

print(UnionSet.issuperset(s1))

a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}

d1 = a.symmetric_difference(b)
print(d1)

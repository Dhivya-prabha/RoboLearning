

SetData = {1, 2, 3, 4, 5, 8}
print(SetData)

newSet = {10, 11, 12, 13}
new = [2, 3, 4, 5, 6]


unionSet = {5, 6, 7, 8, 9, 10, 15}
s1 = SetData.union(unionSet)
print("Intersection", s1)


s1.remove(5)
print("remove", s1)


SetData.discard(7)
print(SetData)

#Clear the set
SetData.clear()
print(SetData)

#Delete the set
del SetData
#print(SetData)


a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}

c = a.union(b)
print(c)

d = a.intersection(b)
print(d)

print(a.issubset(c))
print(c.issubset(b))

print(c.issuperset(a))

print(a.isdisjoint(b))


print(a.difference(b))
print(b.difference(a))


print(a.symmetric_difference(b))


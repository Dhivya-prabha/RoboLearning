

num = [12, 23, 34, 45, 56, 67, 78]

def myFun(*arg):
    for x in arg:
        print (x , end='')   
myFun('Hello ', 'Welcome ', 'to ', 'Elxsi ')

print(num)
name = ["apple", "banana", "cherry", "orange", "cherry"]

for x in name:
    print(x)
    
    
if "apple" in name:
    print('The item yes')
else:
    
    print('No')   
    
#Forward Indexing
print(num[4])    
    
#Backward Indexing

print(num[-4])    
    
num[4] = 57   
    
print(num[4])     
    
    
#List Slicing

print('After slicing' ,name[1:-2])   
    
print(name[1:])    
print(name[:6])  

numbers = num[:]

print('Numbers:  ', numbers)

#To clear the list

numbers [:] = []

print('After empty Numbers:  ', numbers)


#to empty the list

num[1:3] = []

print('after empty', num)

list = [[2,3],[4,5],[5,6],[7,8],[8,9]]

print(list[0][0])  
   
print(len(list)) 


#to add 2 lists

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

c = a+b

print(c)

#add element in to a list
c.append(12)
print('Append :', c )

c.insert(2, 22)

print('Insert: ', c)

c.remove(22)
print('Remove: ', c)


del c[3]

print('Delete: ', c)


#clear a list
numbers.clear()
print(numbers)

#Delete a list
del numbers

#print(numbers)
new = [2, 4, 6, 8]
new[0] = 1 
print(new)    

# change 2nd to 4th items
new[1:4] = [3, 5, 7]  
print(new)

mylist = ["Red", [8, 4, 6], ['a']]
print(mylist)
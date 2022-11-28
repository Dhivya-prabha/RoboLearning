str1 = 'Hello Python'  
print(str1)  

str2 = "Hello Python"  
print(str2)  

str3 = '''Hello Python'''   
print(str3) 



x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

if y != 0:
    print(x/y)
    
#If else

num = int(9)

if num == 0:
  print("Zero")
else:
  print("Non Zero")
  
  
#Nested If else
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
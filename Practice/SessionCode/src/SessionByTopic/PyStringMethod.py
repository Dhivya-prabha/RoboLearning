from nt import stat
txt = "I like Yellow. Yellow is perfect"

x = txt.replace("Yellow", "Red")
print(x)

x = txt.replace("Yellow", "Red", 1)
print(x)

str = " I like Yellow.  "
print(str.strip())

str1 = ("Tata, Elxsi")
print(str1.split(","))

print(str.index("Y"))

product = "Dell | 100000 | Available"

name = product[:product.index("|")]
print(name)
price = product[product.index("|")+1:product.rindex("|")]
print(price)
status = product[product.rindex("|")+1:]
print(status)



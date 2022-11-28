def add(a, b=7):    
    print(a+b)
    
    def mul(a, b):
        print(a*b)
    mul(3,2)
add(2)

def fruits(food):
    for x in food:
        print(x)
food = ["Apple", "Banana", "cherry"] 

fruits(food)

def add1(*arg):
    for x in arg:
        print(x , end="")
        
add1("Hello", "Welcome", "to", "Elxsi")


print()
def animals(animal1, animal2, animal3):
    return("The cutest animal is "+animal2)

print("Name is ", __name__)

if __name__ ==  '__main__':
    print(animals(animal1 = "Puppy", animal2 = "Kitten", animal3 = "Lamb"))
    
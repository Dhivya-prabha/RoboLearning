from SessionByTopic.pyTuple import fruits
def add(a, b=7):   
    print(a+b)
    
    def mul(a, b):
        print(a*b)
    mul(3, 2)
add(4)

def fruits(food):
    for x in food:
        print(x)
        
food = ["Apple", "banana", "cherry"]
fruits(food)


def add1(*arg):
    for x in arg:
        print(x ,end='')
add1("Hello ", "Welcome ", "To ", "Elxsi")


print()
def animals(animal1, animal2, animal3):
    return("The cutest animal is "+animal2)
    
print(animals(animal1="Puppy", animal2= "Kitten", animal3 = "lamb"))

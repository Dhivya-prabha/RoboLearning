'''
Created on 04-Apr-2022

@author: 29179
'''


class FirstModule:
    name = ""  
    age = 0  
    def __init__(self, personName, personAge):  
        self.name = personName   
        self.age = personAge  
        
    def printPgm(self):
        
        print("Name:{1} Year:{0}".format(self.age, self.name))
        print("Name:{n} Year:{a}".format(n = self.name, a = self.age))
        print("Name:{} Year:{}".format(self.name, self.age))
        print(f"Name: {self.name }  Age:  { str(self.age)}")
        print("Name: ", self.name, "Year: ", self.age)
        print("Name: " + self.name, "My Year: "+str(self.age))
        print('Welcome to "Python Learning"')
        print("Welcome to'Python Learning'")
        print("Welcome")
        print('welcome')
        b = input('Enter you salary:')
        d = input('Enter you bonus:')
        print(int(b)+int(d))
        
P1 = FirstModule("Dhivya", 32)
P1.printPgm()
        
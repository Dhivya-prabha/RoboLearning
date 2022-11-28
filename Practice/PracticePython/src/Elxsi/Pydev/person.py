from Elxsi.Pydev import PyConstru
from Elxsi.Pydev.PyConstru import Employee
from Elxsi.Pydev.PyClass import Student

class person(Employee, Student):
    pass

per1 = person("Mani", 100)  
per1.display()

per1.name = "Raja"
per1.age = 15
per1.details(2015) 
class Employee:  
    def __init__(self, name, empid):  
        self.empid = empid  
        self.name = name  
  
    def display(self):  
        print(f"Employee Id: {self.empid} Name: {self.name}" )  
  
  
emp1 = Employee("John", 101)  
emp2 = Employee("David", 102) 

emp1.display() 
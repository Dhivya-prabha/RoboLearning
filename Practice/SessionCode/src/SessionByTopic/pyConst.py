class Employee:
    
    def __init__(self, empId, name):
        self.empId = empId 
        self.name = name
        
    def display(self):
        print(f"Employee Id is {self.empId} and Name {self.name}")
        
        
emp1 = Employee("Mani", 101)
emp2 = Employee("Balu", 101)

emp2.display()
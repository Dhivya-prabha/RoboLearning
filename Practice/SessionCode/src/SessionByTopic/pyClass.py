class student():
    
    gender = "Male"
    
    def details(self, year):
        print(f"Name of the student is {self.name} and age is {self.age} year is {year}")
    
    
person1 = student()
person2 = student()

person1.name = "Raja"
person1.age = 15

person2.name = "Mani"
person2.age = 13

person2.details(2011)
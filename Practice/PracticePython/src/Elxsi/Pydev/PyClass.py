

class Student(object):
    gender = "Male"
    
    def details(self, year):
        print(f"Name of the student is {self.name} year {year} and age is {self.age}")
        
person1 = Student()
person2 = Student()

person1.name = "Raja"
person1.age = 15
person1.hobbies = ("Books", "Songs", "Sports", "Cook")
print(person1.name)
print(person1.hobbies)  
print(person1.gender)  

person2.name = "Bala"
person2.age = 12
print(person2.name)

person2.details(2013)

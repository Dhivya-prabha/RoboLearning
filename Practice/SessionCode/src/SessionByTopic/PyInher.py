from SessionByTopic.pyConst import Employee
from SessionByTopic.pyClass import student

class person(Employee, student):
        pass
per1 = person("Rocky", 100)
per1.display()

per1.name = "Heran"
per1.age = 21
per1.details(2000)
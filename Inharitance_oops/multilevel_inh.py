class person:
    country="india"
    def takeBreath(self):
        print("I am breathing")
class Employee(person):
    compny="Honda"
    def getSalary(self):
        print("Salary is 100k")
    def takeBreath(self):
        print("I ama an employee so i am luckily breathing")
class Programmer(Employee):
    company="Fiverr"
    def getSalary(self):
        print("No salary for programmer")
    def takeBreath(self):
        print("I am a programmer so i am breathing fine")
p=person()
p.takeBreath()
pr=Programmer()
print(pr.compny)
e=Employee()
e.takeBreath()

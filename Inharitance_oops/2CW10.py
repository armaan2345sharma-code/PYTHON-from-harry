#Types of inhartance
#1. Single inheritance
class Employee:
    company="Google"
    def getInfo(self):
        print("This is an Employee class")
class Programmer(Employee):#This is inheritance
    language="Python"
     # company="YouTube"
    def getLanguage(self):
        print("the language is",self.language)
    def getInfo(self):
        print("This is a Programmer class")#this will override the employee attribute
e=Employee()
e.getInfo()
p=Programmer()
p.getInfo()
p.getLanguage()
print (p.company)
#Multiple inharitance
class ni:
    company="Visa"
class fi:
    company="Fiveer"
class Programmer(ni,fi):
    name="Rohit"
    
l=Programmer()
print(l.name)
print (l.company)
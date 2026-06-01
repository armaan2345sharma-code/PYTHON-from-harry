class employee:
    company="Cammel"
    salary=1000#here salary is a class attrbute 
    location="Delhi"
    def changesalary (self, sal):
        self.salary=sal#here salary is an instance attribute 
    @classmethod
    def changecompany(cls, cmp):#here company is a class attribute and cls is used to access the class attributes 
        cls.company=cmp
        e=employee()
        print(e.company)
e=employee ()
print(e.salary)
e.changesalary(2000)
print(e.salary) 
print(employee.company)
employee.changecompany("Honda")


class employee:
    company="Reliance "
    salary=50000
    salarybonous=10000
    #this is setter method by using property decorator
    @property#property dicorator
    def totalsalary(self):
        return self.salary+self.salarybonous
    @totalsalary.setter
    def totalsalary(self, value):
        self.salary = value - self.salarybonous
e=employee()
print (e.totalsalary)
e.totalsalary=80000
print(e.totalsalary)
print(e.salary)

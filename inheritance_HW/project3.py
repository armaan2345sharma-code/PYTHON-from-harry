class Employee:
    def salary(self,k):
        self.sal=k
    def increment(self):
        self.incr=0.5*self.sal
    @property
    def total(self):
        return self.sal+self.incr
e=Employee()
e.salary(10000)
e.increment()
print("your new pay is ;",e.total)
 
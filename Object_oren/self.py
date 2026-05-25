class Employee:
    company ="Google"
    def getsalary():#get Salary has no self parameter
        print ("Salary is 100k")
harry =Employee ()
#harry.getsalary()=
Employee.getsalary(harry)#now we are trying to give harry as a argument so it throws error
#this is function of self that automatically takes the 1st argument 


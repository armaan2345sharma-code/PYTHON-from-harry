class employee:
    company="Google"#attribute of employee
    company1="Microsoft"
mohit=employee()#instance of employee class 
harry=employee ()
harry.salary=450000#instance attribute of harry
lomror=employee ()
lomror.salary=500000#instance attribute of lomror
print(harry.company)
print(lomror.company,lomror.salary)
employee.company="Youtube"
print(harry.company,harry.salary)
print(lomror.company,lomror.salary)
print(mohit.company1)
#intance attribute will override class attributes 




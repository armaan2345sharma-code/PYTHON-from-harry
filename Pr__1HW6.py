#PROJECT 1
#greatest of 4 number enterd by user
a=int(input("Give first number"))
b=int(input("Give second number"))
c=int(input("Give third number"))
d=int(input("Give fourth number"))
if(a>b):
    f1=a
else:
    f1=b
if(c>d):
    f2=c
else:
    f2=d
if(f1>f2):
    print("greatest number is",f1)
else:
     print("greatest number is",f2)

#FUNCTIONS
#the functions start with def
def Percentage(marks):
    return((marks[0]+marks[1]+marks[2]) / 3)
    
marks1 = [24,56,67]
percentage1=Percentage(marks1)
marks2=[99,89,85]
percentage2=Percentage(marks2)
print(percentage1)
print(percentage2) 

#greetin good day
def greet(name):
    print("Good day",name)
greet("HARRY")

#default parameter
def gret(name="Stranger"):
    print("Good day",name)
gret()
#Recursion function which call itself

#MKING A PROGRAM FOR CALCULATING FACTORIAL
def factorial_iter(n):
    product=1
    for k in range(n):
        product=product*(k+1)
    return product
    
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursive(n-1) 
f=factorial_iter(5)
k=factorial_recursive(5)
print(k)
print(f)
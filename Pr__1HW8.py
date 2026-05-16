#Getting greatest of 3 numbers using a function

def greatest(num1,num2,num3):
    if num1>num2:
        inter1=num1
    else:
        inter1=num2
    if inter1>num3:
        inter2=inter1
    else:
        inter2=num3
    return inter2
m=greatest(45,89,90)
print("greatest is ",m)          
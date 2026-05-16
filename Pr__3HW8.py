#A recursive function to print sum of n natural numbers
def sum_recursive(n):
    if n==1:
        return 1
    return n+sum_recursive(n-1)
k=sum_recursive(7)
print("Sum of n natural number",k)
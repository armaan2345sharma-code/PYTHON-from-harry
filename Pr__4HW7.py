i=int(input("Enter your number : "))
prime=True
for num in range(2,i):
    if i%num==0:
        prime=False
        break
if prime:
        print("prime")
else:
        print("not prime")
        
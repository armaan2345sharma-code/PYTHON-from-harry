
#While loop
i=0
while i<10:
    print("Yes" + str(i))
    i=i+1
print("done")

#For loop
fruits=['Banana','Watermelon','Mango']
for items in fruits:
    print(items)
#Range function  for itemis in ramge (start,end ,stepsize)
for itemis in range (1,8,2):
    print(itemis)
#else in for loop
for ixems in range (1,10):
    print(ixems)
else:
    print("we are over with values")
#Break
#this will tell why else is different then normal print
for n in range (0,10):
    print(n)
    if n==7:
        break
else:
   print("Program is done")
#Here else is not executed as loop is not completely completed


#Continue
print("CONTINUE")

for o in range(0,10):
    if o == 4:
        continue
    print(o)
 
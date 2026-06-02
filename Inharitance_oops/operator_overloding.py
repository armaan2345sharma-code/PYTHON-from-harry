class number :
    def __init__(self, num):
        self.num = num

    def __add__(self,num2):
        print("lets add")
        return number(self.num + num2.num)

n1=number(10)
n2=number(20)
sum= n1+n2
print(sum)

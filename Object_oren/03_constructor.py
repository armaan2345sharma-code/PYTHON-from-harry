class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("This is constructor")
    def display (self):
        print("Name:",self.name)
        print("Age:",self.age)

harry=employee("Harry",25)
#This run automatically when we create object of class employee 
#This intialize the class and run the code without even writing print statements 
harry.display()
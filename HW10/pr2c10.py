#Calculator
class calculation:
    def square(self,num):
        return num*num
    def cube (self,num):
        return num*num*num
    @staticmethod
    def print_thanks():
        print("Thanks for using this calculator ")
    def square_root(self,num):
        return num**0.5
num=int(input("Enter a number: "))
cal=calculation ()
calculation.print_thanks()
print("Square of num is:",cal.square(num))
print("Cube of num is:",cal.cube(num))
print("Square root of num is:",cal.square_root(num))

class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{self.x}i+{self.y}j"
k=vector(1,9)
print(k)
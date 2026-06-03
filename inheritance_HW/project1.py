class c2dvec:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def __str__(self):
        return f"i={self.i} j={self.j}"
class c3dvec(c2dvec):
    def __init__(self,i,j,k):
        super().__init__(i,j)#this will the constructor of the parents
        self.kcap=k
    def __str__(self):
        return f"i={self.i} j={self.j} k={self.kcap}"
v1=c2dvec(1,2)
v2=c3dvec(3,4,5)
print(v1)
print(v2)

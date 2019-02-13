# instructions
# create a vector class
# that should...
# add vectors
# scale vector
# norm or len
# dot product
# override __str__ and __repr__
from functools import reduce 
class Vector:
    def __init__(self, *args):
        self.args = args
        

    def __str__(self):
        return str(self.args)

    def add(self,vect):
        return Vector(*[x + y for x, y in zip(self.args, vect.args)])

    def scale(self, dim1):
        return Vector(*[x * dim1 for x in self.args])

    def norm(self):
        temp = reduce(lambda final, x: final + x**2,self.args)
        return temp ** 0.5

    def product(self,dim1):
        return sum((x * y for x, y in zip(self.args, dim1.args)))




    
        

        

# read in the vectors.txt file
# create a  list of vectors
# scale the first and last vector by 3
# add them all together and find
# that new vector
# find the norm of the final vector
# also find the dot product between the 2nd and 3rd vector
from vector import Vector
a = []
with open("vectors.txt") as f:
    for line in f:
        # lineitems = line.strip().split(',')
        # #print(lineitems)
        # lineitemsint = [int(i) for i in lineitems]
        # #print(lineitemsint)
        # v1= Vector(lineitemsint)
        v = Vector(*tuple(map(int,line.strip().split(','))))
        a.append(v)
       
for i in range(len(a)):
    print(a[i])

print(a[0].add(a[1]))
print(a[0].scale(3))
print(a[2].norm())
print(a[0].product(a[2]))

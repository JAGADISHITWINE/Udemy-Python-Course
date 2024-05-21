## Set & Creating Sets
numbers = set([1,2,3,4,5,6,7,8,9])
print(numbers)
numbers = {1,3,2,4,5,4,2}
print(numbers)

## Empty Set
numbers = set()
print(type(numbers))

## Set Operations
seta = {1,2,3,4,5}
setb = {4,5,6,7,8}
print(seta | setb) # union operation
print(seta & setb) # intersection  operation
print(seta - setb) # difference  operation
print(seta ^ setb) # symmetric difference  operation

## Add & Remove Set Methods
seta = {1,2,3,4,5}
seta.add(6)
print(seta)
seta.remove(1)
print(seta)

seta = {1,2,3,4,5}
a = seta.pop()
print(a)
seta.clear()
print(seta)

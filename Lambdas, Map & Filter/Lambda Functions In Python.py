result = (lambda x:x**2)(7)
print(result)

result = (lambda x,y:x+y)(2,3)
print(result)

## Map In Python
numbers = [1,2,3,4,5,6]

def square(x):
    return x*x

new_list = list(map(square,numbers))
print(new_list)
    
## Using Map In Different Ways
names = ['john','rob','mike']
cap_names = list(map(str.capitalize,names))
print(cap_names)

## Filter In Python
numbers = [1,2,3,4,5,6,7,8,9,10]
       
odd_num = list(filter(lambda x : x%2 == 1,numbers))
print(odd_num)

## Generators In Python
def function():
    counter = 0
    while counter<=10:
        yield counter
        counter+=1

print(list(function()))

def even_generator(x):
    for i in range(x):
        if i%2==0:
            yield i
        
print(list(even_generator(12)))
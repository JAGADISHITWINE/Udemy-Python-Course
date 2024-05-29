## Passing Arguments to Functions
def speed(distance,time):
    speed = distance/time
    print(speed)
    
speed(100, 2)

##  Keyword Arguments
def speed(distance,time):
    speed = distance/time
    print(speed)
    
speed(distance=100, time=2)

## Default Parameters
def area(radius,pi = 3.14):
    print(pi*radius*radius)
    
area(10,3.15)

## Making function return a value
def area(radius,pi):
    return(pi*radius*radius)
    
print(area(10,3.15))

## Calling a function in other function
def area(radius,pi):
   result =  pi*radius*radius
   return result

def cost(circle_area,cost_per_sqm):
   total_cost = circle_area * cost_per_sqm
   return total_cost

print(cost(area(10,3.15),2))

##  Making A Function Return Multiple Values
def circle(r):
    area = 3.14 * r * r
    circumference = 2 * 3.14 * r * r
    return area, circumference

a, c = circle(5)
print(f'Area of the circle is {a}, circumference of the circle is {c}')

## Passing List To A Function
scores = [1,2,3,4,5]
numbers = 0

def add(numbers):
    for number in numbers:
        number += number
    return number

sum = add(scores)
print(sum)

## Returning List
def remove_duplicates(numbers):
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list

ids = [1,2,3,4,5,2,1,7,8,9]
print(remove_duplicates(ids))

## Check If A String Is A Palindrome
def ispalindrome(word):
    return word == word[::-1]

word = 'racecar'
ans = ispalindrome(word)

if ans:
    print('yes')
else:
    print('no')


## Variable Length Positional Arguments
def add(*args):
    sum = 0
    for number in args:
        sum = sum + number
    return sum
    
print(add(1,2,3,4,5,6,7,8,9))

## Variable Length keyword Arguments
def product(**kwargs):
    for key,value in kwargs.items():
        print(key+":"+value)

product(name='iphone',price='700')

## Decorators
def chocolate():
    print("Chocolate")
    
def decorator(func):
    def wrapper():
        print("Wrapper upside")
        func()
        print("Wrapper downside")
    return wrapper

chocolate = decorator(chocolate)
chocolate()
        
##  Another Way Of Using Decorator
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Wrapper upside")
        func(*args, **kwargs)
        print("Wrapper downside")
    return wrapper

@decorator
def chocolate():
    print("Chocolate")

@decorator
def cake(name):
    print("Cake "+name)
    
chocolate()
cake('apple')

def summer_discount_decorator(func):
    def wrapper(price):
        # take the value inside the total and return
        func(price)
        return func(price/2)
    return wrapper
 
@summer_discount_decorator
def total(price):
    # Let's assume there was some code here which calculated the total amount
    return price
 
print(total(20))
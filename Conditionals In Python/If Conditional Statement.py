## If Conditional Statement
age = int(input("Enter your age: "))

if age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')
print('#'*20)
    
## Elif Statement
marks = int(input('Enter the marks: '))
if marks>=90:
    print('Grade A')
elif marks>=70:
    print('Grade B')
elif marks>=60:
    print('Grade C')
else:
    print('Grade D')
print('#'*20)
    
## Range Function
numbers = list(range(1,11))
print(numbers)
print('#'*20)

## For Loop
for numbers in range(1,11):
    print(numbers)
print('#'*20)
    
fruits = ['Apple','Mango','Banana','Orange']
for fruit in fruits:
    print(fruit)
print('#'*20)    

## Looping Through A Dictionary    
people = {"John":32,"Rob":40,"Tim":20}
for x in people:
    print(x,people[x])
print('#'*20)

## While Loop
counter  = 0
while counter<=10:
    print(counter)
    counter = counter +1
print('#'*20)
    
## Break Statement
counter  = 0
while counter<=10:
    print(counter)
    if counter == 5:
        break
    counter = counter +1
print('#'*20)

## Continue Statement
counter = 0
while counter<=10:
    counter = counter +1
    if counter == 5:
        continue
    print(counter)
print('#'*20)


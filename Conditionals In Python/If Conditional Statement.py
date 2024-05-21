## If Conditional Statement
age = int(input("Enter your age: "))

if age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')
    
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
    
## Range Function
numbers = list(range(1,11))
print(numbers)

## For Loop
for numbers in range(1,11):
    print(numbers)
    
fruits = ['Apple','Mango','Banana','Orange']
for fruit in fruits:
    print(fruit)

## Looping Through A Dictionary    
people = {"John":32,"Rob":40,"Tim":20}
for x in people:
    print(x,people[x])

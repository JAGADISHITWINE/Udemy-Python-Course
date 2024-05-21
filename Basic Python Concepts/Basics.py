## Accepting User Input
Name = input("Enter your name: ")
print(Name)

## Concatenation Of Strings
Message = 'Hello ' + 'World'
print(Message)

## Data Types In Python
print(type(8))
print(type('8'))
print(type(8.0))
print(type(True))
print(type(8+8j))

## Variable Declaration & Assignment
price = 100
print(price)

## Naming Conventions To Follow While Creating Variables
radius=10
RADIUS=10
RADIUS=10
rad_ius=10
_radius=10
radius1=10

## Operators In Python
a=10
b=20
print(a==b)
b=10
print(a==b)
print(a!=b)
b=20
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

## Logical Operators
a=10
b=10
print(a==b)
b = 20
print(a==10 and b==20)
b=30
print(a==10 and b==20)
print(a==10 or b==20)

## Accepting Input & Adding Numbers
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
summed_num = num1 + num2
print(summed_num)

## Creating Username & Email Using Concatenation
firstname = input('Enter firstname: ')
lastname = input('Enter lastname: ')
username = firstname + lastname
print("Username is: ",username)

email = username + '@gmail.com'
print("Email is: ",email)

## Comparing User Strings

saved_password = "admin@1234"
user_password = input("Enter password ")
if saved_password == user_password:
    print("The entered pasword is correct")
else:
    print("The entered pasword is Incorrect")
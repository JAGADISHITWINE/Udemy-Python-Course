## Lists In Python
#            0      1      2
people = ['John', 'Rob', 'Mike']
print(people) 

## Storing Different Data Types In A List
items = ['Computer', 10, 4.5 ,True, 3+5j]
print(items)
print(type(items[4]))

## Negative Indexing
#-ve        -6       -5       -4       -3          -2          -1
fruits = ['apple', 'mango', 'peach', 'orange', 'watermelon', 'grapes']
#+ve         0        1        2        3           4           5
print(fruits[-1])

## List Slicing
#slicing-6       -5       -4       -3        -2            -1
#-ve        -6       -5       -4       -3          -2          -1
fruits = ['apple', 'mango', 'peach', 'orange', 'watermelon', 'grapes']
#+ve         0        1        2        3           4           5
#slicing 0        1        2        3         4             5         6
print(fruits[0:6])
print(fruits[-6:-4])

## In & Not In Operators
fruits = ['apple', 'mango', 'peach', 'orange', 'watermelon', 'grapes']
print('apple' in fruits)
print('tomato' in fruits)
print('pineapple' not in fruits)
print('apple' not in fruits)


## List Functions
fruits = ['apple', 'mango', 'peach', 'orange', 'watermelon', 'grapes']
print(len(fruits)) #find length of list
fruits.insert(1,'pineapple') #insert items to list
print(fruits)
fruits.append('tomato') #append items to list
print(fruits)
fruits.append(['cherry','strawberry']) #append items to list
print(fruits)
fruits.extend(['guava','muskmelon']) #extend items to list
print(fruits)
fruits.remove('guava') #remove items from list
print(fruits)

scores = [1,2,3,4,5,6,7,8,9]
print(max(scores))
print(min(scores))

## Addition & Multiplication Operation On Lists
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)
print(a*2)

## Nesting Lists
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [1, 2, [3, 4, 5, [10, 20, 30]], 6, 7, 8, [9, 10]]
print(b[2][0])
print(b[2][3][1])

## Mutability Of Lists
a = [1, 2, 3]
a[1] = 100
print(a)

## Tuples
fruits = ('apple', 'mango', 'peach', 'orange', 'watermelon', 'grapes')
print(fruits)
print(type(fruits))

## Searching Items In A List
products = ['phone', 'tablet', 'laptop', 'journal']
item = input("Enter product to search: ")
print(item in products)

## Adding & Removing Items
products = ['phone', 'tablet', 'laptop', 'journal']

#displaying products
print(f'Current list of items: {products}')

#asking user to remove a product
item = input("Enter a product to remove: ")
products.remove(item)

#displaying the entire list after removing item
print(f'List of items after removing: {products}')

#asking user to add a product
add_item = input("Enter a product to add: ")
products.append(add_item)

#displaying the entire list after adding item
print(f'List of items after adding: {products}')

## Adding List Item At A Position
products = ['phone', 'tablet', 'laptop', 'journal']

#displaying products
print(f'Current list of items: {products}')

#asking user to add a product
add_item = input("Enter a product to add: ")

add_after = input(f'After which product do you want to place {add_item} ')
index = products.index(add_after)
products.insert(index+1,add_item)

#displaying products
print(f'Current list of items: {products}')
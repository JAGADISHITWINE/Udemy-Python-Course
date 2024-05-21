## Dictionaries
people = {"John":32,"Rob":40,"Tim":20}
print(people['Tim'])

people_id = {32:'John',40:'Rob',20:'Tim'}
print(people_id[32])

people = {"John":32,"Rob":40,"Tim":20}
people['Rob'] = 45
print(people)

## Creating a Dictionaries using dict()
people = dict(
    john=32,
    mike=23,
    rob=58
)
people['tim'] = 30
del people['mike']
print(people)

## Get Method
people = {
    "John":32,
    "Rob":40,
    "Tim":20
    }

print(people["Rob"])
print(people.get("Rob"))

## Update & Pop Method
prices = {
    "iphone":500,
    "ipad":400
    }

new_prices = {
    "iphone":600,
    "imac":1500
}
prices.update(new_prices)
print(prices)
prices.pop('ipad')
print(prices)

## Items & Keys Method
prices={'iphone': 600, 'ipad': 400, 'imac': 1500}
print(prices.keys(),
      prices.values(),
      prices.items())

## Adding Products To A Dictionary
products = {'phone':100, 'tablet':200, 'laptop':400, 'journal':40}

#displaying products
print(f'Current list of items: {products}')

#asking user to add a product
product = input("Enter a product to check the price : ")
print(f'Price of the {product} is {products[product]}')

new_product = input("Enter a product you want to add: ")
new_product_price = int(input(f'Enter the price for {new_product}: '))
products[new_product] = new_product_price
print(f'Updated list of products {products}')

## Deleting Products from A Dictionary
products = {'phone':100, 'tablet':200, 'laptop':400, 'journal':40}

#displaying products
print(f'Current list of items: {products}')
deleted_product = input("Enter a product to be deleted: ")
del(products[deleted_product])
print(f'Updated list of products {products}')

## Editing Products from a Dictionary
products = {'phone':100, 'tablet':200, 'laptop':400, 'journal':40}

#displaying products
print(f'Current list of items: {products}')
price_change_product = input("Enter product for which you want to change the price : ")
price_change = int(input(f"Enter the new price for {price_change_product} : "))
products[price_change_product] = price_change
print(f'Updated list of products {products}')



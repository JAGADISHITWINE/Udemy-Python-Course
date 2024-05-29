## Adding Items To Cart Using For Loop
cart_1 = []
num_of_items = int(input("Enter the number of items you want to add to the cart "))
for x in range(num_of_items):
    item = input("Enter an Item into the cart ")
    cart_1.append(item)
print(cart_1)

## Adding Items To Cart Using While Loop
cart_2 = []

while True:
    choice = input("Do you want to add items to the cart ?")
    if choice == 'yes':
        item = input("Enter an Item into the cart: ")
        cart_2.append(item)
        print(f'Current cart contents are {cart_2}')
    else:
        break

## Creating A List Of Products
Products = [{'name':'Smartphone','price': 500,'description':'A handled device'}, 
           {'name':'Tablet','price': 1000,'description':'A portable computer'},
           {'name':'Headphones','price': 50,'description':'A pair of earphones'},
           {'name':'Smartwatch','price': 300,'description':'A wearable device used for fitness tracking'},
           {'name':'Bluetooth speakers','price': 100,'description':'A wireless portable speaker'}]

cart_3 = []
while True:
    choice = input("Do you want to add items to the cart ?")
    if choice == 'yes':
        print('Here is a list of products and their prices')
        for index,product in enumerate(Products):
            print(f"{index}:{product['name']}: {product['description']} :$ {product['price']} ")
        product_id = int(input("Enter the id of the product you want to buy: "))
        # check if product is already present in the cart
        if Products[product_id] in cart_3:
            Products[product_id]['quantity'] += 1
        else:
            Products[product_id]['quantity'] = 1
            cart_3.append(Products[product_id])
        total = 0
        print('Here are the contents in your cart:')
        for product in cart_3:
            print(f"{product['name']} : {product['price']} : QTY: {product['quantity']}")
            total += product['price'] * product['quantity']
    else:
        break

if cart_3 != []:
    print(f'Thank You, your final cart contents are')
    for product in cart_3:
        print(f"{product['name']} : {product['price']} : QTY: {product['quantity']}") 
    print(f"Cart total is: ${total}")
else:
    print(f'No products are added to cart')
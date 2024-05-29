# def product_data():
#     product_name = input("Enter name of the product ")
#     product_price = int(input("Enter price of thr product "))
#     print(product_name,product_price)
    
# product_data()

class Product:
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def get_data(self):
        self.name = input("Enter name of the product ")
        self.price = int(input("Enter price of thr product "))
    
    def put_data(self):
        print(self.name)
        print(self.price)
        
p1 = Product("","")
p1.get_data()
p1.put_data()
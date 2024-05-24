# Inheritance - meaning('Getting Something from Somebody)

class Product:
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def get_data(self):
        self.name = input("Enter name of the product ")
        self.price = int(input("Enter price of thr product "))
    
    def put_data(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")
        
class DigitalProduct(Product):
    def __init__(self, name, price, link):
        super().__init__(name, price)
        self.link = link
    
    def get_link(self):
        self.link = input("Enter the product link ")
        
    def put_link(self):
        print(f"Product Link: {self.link}")

ebook = DigitalProduct("",0,"")
ebook.get_data()
ebook.get_link()
ebook.put_data()
ebook.put_link()


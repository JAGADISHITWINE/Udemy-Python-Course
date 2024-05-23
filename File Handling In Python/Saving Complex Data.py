def save_user_data():
    name = input('Enter name ')
    email = input('Enter email ')
    contact = input('Enter contact ')
    
    user_data = f"Name:{name}\nEmail:{email}\nContact:{contact}\n"
    with open('C:/python/Udemy-Course/File Handling In Python/user_data.txt','a') as file:
        file.write(user_data)
    
def read_user_data():
    with open('C:/python/Udemy-Course/File Handling In Python/user_data.txt','r') as file:
        print(file.read())
        
# save_user_data()
read_user_data()
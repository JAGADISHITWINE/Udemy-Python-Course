import json

def save_user_data():
    user_list = []
    while True:
        name = input("Enter name (or 'quit' to exit the program): ")
        if name == 'quit':
            break
        email = input('Enter email ')
        contact = input('Enter contact ')
        
        # creating user dictionary
        user_data = {
            "name":name,
            "email":email,
            "contact":contact
        }
        
        user_list.append(user_data)
        
        with open('C:/python/Udemy-Course/File Handling In Python/user_data.json','w') as file:
            json.dump(user_list,file)
        
        print("User data saved successfully")

save_user_data()
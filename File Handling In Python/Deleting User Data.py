import json
import os

def delete_user_data(name):
    if not os.path.exists('C:/python/Udemy-Course/File Handling In Python/user_data.json'):
        print('No user data found')
        return

    with open('C:/python/Udemy-Course/File Handling In Python/user_data.json') as file:
        user_list = json.load(file)
        user_found = False
        for user_data in user_list:
            if user_data['name'].lower() == name.lower():
                user_list.remove(user_data)
                user_found = True
                break
        if not user_found:
            print("User not found")
        with open('C:/python/Udemy-Course/File Handling In Python/user_data.json','w') as file:
            json.dump(user_list,file)
        print("User data deleted successfully")
        
delete_name = input("Enter name which you want to delete: ")
delete_user_data(delete_name)
import json
import os

def edit_user_data(name):
    if not os.path.exists('C:/python/Udemy-Course/File Handling In Python/user_data.json'):
        print('No user data found')
        return

    with open('C:/python/Udemy-Course/File Handling In Python/user_data.json') as file:
        user_list = json.load(file)
        user_found = False
        for user_data in user_list:
            if user_data['name'].lower() == name.lower():
                email = input("Enter updated email: ")
                contact = input("Enter updated contact: ")
                
                user_data['email'] = email
                user_data['contact'] = contact
                user_found = True
                break
        if not user_found:
            print("User not found")
        with open('C:/python/Udemy-Course/File Handling In Python/user_data.json','w') as file:
            json.dump(user_list,file)
        print("User data updated successfully")

edit_name = input("Enter name which you want to edit data for:")
edit_user_data(edit_name)
import json
import os

def read_user_data():
    if not os.path.exists('C:/python/Udemy-Course/File Handling In Python/user_data.json'):
        print('No user data found')
        return
    
    with open('C:/python/Udemy-Course/File Handling In Python/user_data.json') as file:
        user_list = json.load(file)
        for user_data in user_list:
            print('Name:',user_data['name'])
            print('Email:',user_data['email'])
            print('Contact:',user_data['contact'])
            print("\n")
                 
read_user_data()

from tkinter import *
import bcrypt

def validate(password):
    hash = b'$2b$12$3/Re7C/sFMv4od5zxcyoeuslqUOAQurtA1LMP2XTvyUuzDuQd6LZm'
    entered_password = bytes(password,encoding='utf-8')
    if bcrypt.checkpw(entered_password,hash):
        print('Login successful')
    else:
        print('Invalid password')
    
window = Tk()
window.title("Password Validator")
window.geometry('300x300')
password_entry = Entry(window)
password_entry.pack()

button = Button(text='Validate',command = lambda:validate(password_entry.get()))
button.pack()
window.mainloop()
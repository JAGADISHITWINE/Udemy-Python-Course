from tkinter import *

def add():
    num1 = int(number1.get())
    num2 = int(number2.get())
    result = str(num1 + num2)
    answer.config(text='Answer is: '+ result)

root = Tk()
root.geometry("300x300")

number1 = Entry(root)
number2 = Entry(root)
number1.pack()
number2.pack()

button =  Button(root,text = 'ADD',command = add)
button.pack()

answer = Label(root)
answer.pack()
root.mainloop()

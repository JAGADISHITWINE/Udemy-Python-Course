from tkinter import *

root = Tk()
root.geometry('300x300')

def selected():
    label.config(text = 'Choice of fuel is: '+ fuel.get())
    

fuel = StringVar(value='None')

radio1 = Radiobutton(root, text='Petrol', variable=fuel, value='Petrol', command=selected)
radio1.pack()

radio2 = Radiobutton(root, text='Diesel', variable=fuel, value='Diesel', command=selected)
radio2.pack()

radio3 = Radiobutton(root, text='Electric', variable=fuel, value='Electric', command=selected)
radio3.pack()

label = Label(root)
label.pack()
root.mainloop()
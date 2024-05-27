from tkinter import *
def display():
    data = entry.get()
    print(data)


root = Tk()
root.geometry("300x300")
entry = Entry(root)
entry.pack() 

button = Button(root,text='CLick here',command = display)
button.pack()
root.mainloop()

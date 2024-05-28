from tkinter import *

root=Tk()

frame1 = Frame(root,highlightthickness=1,highlightbackground='black', padx=2, pady=2)
frame1.pack()

frame2 = Frame(root,highlightthickness=1,highlightbackground='black', padx=2, pady=2)
frame2.pack(side=BOTTOM)

button1 = Button(frame1, text='Button 1')
button1.pack()

button2 = Button(frame2, text='Button 2')
button2.pack()

root.geometry('300x300')


root.mainloop()
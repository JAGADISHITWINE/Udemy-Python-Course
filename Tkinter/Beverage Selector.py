from tkinter import *

root = Tk()
root.geometry('300x300')

def selected():
    sugar = sugar_var.get()
    ice = ice_var.get()
    cream = cream_var.get()
    
    if sugar:
        sugar="Sugar"
    else:
        sugar="No Sugar"
    if ice:
        ice=" Ice"
    else:
        ice=" No Ice"
    if cream:
        cream=" Cream"
    else:
        cream=" No Cream"
    
    label.config(text='Options selected are: ' + '\n' + sugar + '\n' + ice + '\n' + cream)

sugar_var=BooleanVar()
ice_var=BooleanVar()
cream_var=BooleanVar()

sugar_checkbox = Checkbutton(root,text='Sugar',variable=sugar_var,command=selected)
sugar_checkbox.pack()

ice_checkbox = Checkbutton(root,text='Ice',variable=ice_var,command=selected)
ice_checkbox.pack()

cream_checkbox = Checkbutton(root,text='Cream',variable=cream_var,command=selected)
cream_checkbox.pack()

label=Label(root)
label.pack()

root.mainloop()
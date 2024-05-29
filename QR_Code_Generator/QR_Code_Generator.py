import os
from tkinter import *
import pyqrcode
from PIL import Image, ImageTk
import png  # Ensure this library is installed with `pip install pypng`

directory = os.path.join(os.getcwd(), 'QR_Code_Generator')

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    filename = link_name + '.png'
    
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    filepath = os.path.join(directory, filename)
    url = pyqrcode.create(link)
    url.png(filepath, scale=5)
    image = ImageTk.PhotoImage(Image.open(filepath))
    
    image_label.config(image=image)
    image_label.image = image  # Keep a reference to avoid garbage collection

window = Tk()
window.title('QR Code Generator')

# Ensure the icon path is correct
icon_path = os.path.join(directory, 'QrCode.png')
if os.path.exists(icon_path):
    img = PhotoImage(file=icon_path)
    window.iconphoto(False, img)

canvas = Canvas(window, width=400, height=500)  # Increased height to accommodate the image
canvas.pack()

app_label = Label(window, text='QR Code Generator', fg='lightblue', font=('Arial', 25))
canvas.create_window(200, 50, window=app_label)

name_label = Label(window, text='Link Name')
link_label = Label(window, text='Link')
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(window)
link_entry = Entry(window)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

button = Button(window, text='Generate QR Code', command=generate)
canvas.create_window(200, 230, window=button)

# Create an initial placeholder for the QR code image
image_label = Label(window)
canvas.create_window(200, 350, window=image_label)  # Adjusted y-coordinate to 350

window.mainloop()

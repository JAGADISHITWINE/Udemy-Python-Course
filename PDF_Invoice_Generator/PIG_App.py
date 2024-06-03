from tkinter import *
from fpdf import FPDF
from datetime import datetime
import random

# Create main window
window = Tk()
icon_path = "C:/python/Udemy-Course/PDF_Invoice_Generator/hospital.png"
img = PhotoImage(file=icon_path)
window.iconphoto(False, img)
window.title('PIG')
window.geometry('500x500')  # Set the window size

# Global variables
invoice_items = []

# Function to add selected medicine to the invoice
def add_medicine():
    selected_medicine = medicine_list_box.get(ANCHOR)
    quantity = int(quantity_entry.get())
    price = medicines[selected_medicine]
    item_total = quantity * price

    # Check if the selected medicine is already in the invoice items
    for index, item in enumerate(invoice_items):
        if item[0] == selected_medicine:
            # Update quantity and total price
            new_quantity = item[1] + quantity
            new_total = new_quantity * price
            invoice_items[index] = (selected_medicine, new_quantity, new_total)
            break
    else:
        # Add new entry if the medicine is not already in the list
        invoice_items.append((selected_medicine, quantity, item_total))

    total_amount_entry.config(state=NORMAL)
    total_amount_entry.delete(0, END)
    total_amount_entry.insert(END, str(calculate_total()))
    total_amount_entry.config(state='readonly')
    update_invoice_text()

# Function to calculate the total amount
def calculate_total():
    total = 0.0
    for item in invoice_items:
        total += item[2]
    return total

# Function to update the invoice text area
def update_invoice_text():
    invoice_text.config(state=NORMAL)
    invoice_text.delete(1.0, END)
    for item in invoice_items:
        invoice_text.insert(END, f'Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n')
    invoice_text.config(state='disabled')

# Function to generate a unique receipt number
def generate_receipt_number():
    return f"REC-{random.randint(1000, 9999)}"

# Function to generate the invoice PDF
def generate_invoice():
    customer_name = customer_entry.get()
    receipt_number = generate_receipt_number()
    purchase_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pdf = FPDF()
    pdf.add_page()

    # Header
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, 'SANKALPA VETERINARY HOSPITAL', new_x='LMARGIN', new_y= 'NEXT', align = 'C')
    pdf.set_font('Helvetica', '', 12)
    pdf.cell(0, 10, 'Opp ShanthiNagar Bus-Stop, Bangalore, India - 560027', new_x='LMARGIN', new_y= 'NEXT', align = 'C')
    pdf.cell(0, 10, 'Ph.No: +91 9980556022, 080-2242586', new_x='LMARGIN', new_y= 'NEXT', align = 'C')
    pdf.image(icon_path, x=5, y=3, w=30)  # Add the company logo

    # Invoice title and details
    pdf.set_font('Helvetica', 'BU', 18)
    pdf.cell(0, 10, 'Bill', new_x='LMARGIN', new_y= 'NEXT', align = 'C')
    pdf.set_font('Helvetica', size=12)
    pdf.cell(0, 10, f'Receipt Number: {receipt_number}',new_x='LMARGIN', new_y= 'NEXT', align = 'L')
    pdf.cell(0, 10, f'Customer: {customer_name}', new_x='LMARGIN', new_y= 'NEXT', align = 'L')
    pdf.cell(0, 10, f'Purchase Date & Time: {purchase_date_time}', new_x='LMARGIN', new_y= 'NEXT', align = 'L')
    pdf.ln(10)

    # Invoice items
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(60, 10, 'Medicine', 1)
    pdf.cell(20, 10, 'Quantity', 1)
    pdf.cell(40, 10, 'Total', 1)
    pdf.ln(10)
    pdf.set_font('Helvetica', size=12)
    for item in invoice_items:
        pdf.cell(60, 10, item[0], 1)
        pdf.cell(20, 10, str(item[1]), 1)
        pdf.cell(40, 10, str(item[2]), 1)
        pdf.ln(10)

    # Total amount
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(60, 10, '', 0)
    pdf.cell(20, 10, 'Total:', 1)
    pdf.cell(40, 10, str(calculate_total()), 1)
    pdf.ln(20)

    # Signature
    pdf.cell(0, 10, 'Signature: ____________________', new_x='LMARGIN', new_y= 'NEXT', align = 'R')

    pdf.output("Bill.pdf")

# Dictionary of medicines with their prices
medicines = {

}

# Create and place widgets using grid layout
medicine_label = Label(window, text='Medicine:')
medicine_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

medicine_list_box = Listbox(window, selectmode=SINGLE)
for medicine in medicines:
    medicine_list_box.insert(END, medicine)
medicine_list_box.grid(row=0, column=1, padx=10, pady=10, sticky=W)

quantity_label = Label(window, text='Quantity:')
quantity_label.grid(row=1, column=0, padx=10, pady=10, sticky=E)

quantity_entry = Entry(window)
quantity_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

add_button = Button(window, text='Add Medicine', command=add_medicine)
add_button.grid(row=2, column=1, padx=10, pady=10, sticky=W)

total_amount_label = Label(window, text='Total Amount:')
total_amount_label.grid(row=3, column=0, padx=10, pady=10, sticky=E)

total_amount_entry = Entry(window, state='readonly')
total_amount_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

customer_label = Label(window, text='Customer Name:')
customer_label.grid(row=4, column=0, padx=10, pady=10, sticky=E)

customer_entry = Entry(window)
customer_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

generate_button = Button(window, text='Generate Invoice', command=generate_invoice)
generate_button.grid(row=6, column=1, padx=10, pady=10, sticky=W)

invoice_text = Text(window, height=10, width=50, state='disabled')
invoice_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
window.mainloop()

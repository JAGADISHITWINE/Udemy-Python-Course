from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image('profile_logo.png', 10, 8, 33)
        self.set_font('helvetica', 'B', size=16)
        self.cell(80)
        self.cell(40, 10, text='Hello world',border=1,align='C')
        self.ln(40)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', size=16)
        self.cell(0,10,f'Page {self.page_no()}/{{nb}}',align='C')
        
        

# Create an instance of the PDF class (not FPDF)
pdf = PDF()

# Add a page to the PDF document
pdf.add_page()

for i in range(1,41):
    pdf.cell(0,10,f"Priniting line numbers {i}",new_x = 'LMARGIN',new_y = "NEXT")

pdf.set_font('helvetica', 'B', size=12)

# Output the PDF to a file
pdf.output('helloworld.pdf')
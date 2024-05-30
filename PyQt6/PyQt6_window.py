
from PyQt6.QtWidgets import QWidget,QApplication,QLabel
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('First PyQT Window')
        self.setGeometry(0,0,400,300)
        
        label = QLabel(self)
        label.setText("Hello World!")
        label.move(180,110)
        
app=QApplication(sys.argv)
window=Window()
window.show()

sys.exit(app.exec())
#Construir un programa que muestre una ventana a traves de la cuál se pueda leer su número
#de cédula y su nombre completo



from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QFormLayout, QLabel)
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #dimension

        self.setGeometry(400, 100, 600, 300)

        #Nombre ventana

        self.setWindowTitle("Ingreso de Cédula y Nombre Completo")
        
        #Widgets

        self.boton = QPushButton("Mostrar Datos")
        self.boton.clicked.connect(self.boton_click)
        
        #Pedimos nombre y cédula

        self.nombre_edit = QLineEdit()
        self.cedula_edit = QLineEdit()
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        
        #Espacios para colocar el nombre y la cédula

        layout = QFormLayout()
        layout.addRow("Nombre Completo:", self.nombre_edit)
        layout.addRow("Número de Cédula:", self.cedula_edit)
        layout.addWidget(self.boton)
        layout.addWidget(self.label)
        
        

        central_widget = QWidget()
        central_widget.setLayout(layout)
        
        

        self.setCentralWidget(central_widget)
    
    def boton_click(self):

        #Mostramos lo puesto en los espacios de célula y nombre

        nombre = self.nombre_edit.text()
        cedula = self.cedula_edit.text()
        
        
        texto = f"Nombre: {nombre}\nCédula: {cedula}"
        self.label.setText(texto)


app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
sys.exit(app.exec_())

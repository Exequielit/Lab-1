#Construir un programa que muestre una ventana que lea una clave secreta sin mostrar 
#los carácteres que la componen




from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QFormLayout, QLabel)
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Dimensiones

        self.setGeometry(400, 100, 600, 400)

        #Nombre de la Ventana
        self.setWindowTitle("Ingreso de Clave Secreta")
        
        # Botón para mostrar la clave con los carácteres reales
        self.boton = QPushButton("Mostrar Clave")
        self.boton.clicked.connect(self.boton_click)
        
        #Ocultamos los carácteres de la clave con la función .Password
        self.clave_edit = QLineEdit()
        self.clave_edit.setEchoMode(QLineEdit.Password)
        
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        
        # Aqui pedimos la clave

        layout = QFormLayout()
        layout.addRow("Clave Secreta:", self.clave_edit)
        layout.addWidget(self.boton)
        layout.addWidget(self.label)
        

        central_widget = QWidget()
        central_widget.setLayout(layout)
        
      
        self.setCentralWidget(central_widget)
    
    def boton_click(self):
        #En esta parte obtenemos la clave secreta si la queremos saber
        clave = self.clave_edit.text()
        
        # se muestra
        self.label.setText(f"Clave ingresada: {clave}")


app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
sys.exit(app.exec_())

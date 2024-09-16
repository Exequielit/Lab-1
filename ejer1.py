
#Construir un programa que muestre una ventana en la cuál aparezca su nombre completo en base a este 
#código ya hecho y su edad centrado


from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QFormLayout, QLabel, QVBoxLayout)
from PyQt5.QtCore import Qt
import sys

#Ventana principal donde montaremos todo

class MainWindow(QMainWindow):

    #Función principal

    def __init__(self):
        super().__init__()
        
        #Dimensiones 

        self.setGeometry(400, 100, 600, 400)
        self.setWindowTitle("Ventana para mostrar Nombre y Edad Centrado")
        
        #Crear widgets

        self.boton = QPushButton("Mostrar Nombre y Edad")
        self.boton.clicked.connect(self.boton_click)
        
        self.nombre_edit = QLineEdit()  
        self.edad_edit = QLineEdit()    
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter) 
        
        #Layaout que pide los nombres y la edad
        layout = QFormLayout()
        layout.addRow("Nombre Completo:", self.nombre_edit)
        layout.addRow("Edad:", self.edad_edit)
        layout.addWidget(self.boton)
        layout.addWidget(self.label)
        
        #Widget central para la ventana
        central_widget = QWidget()
        central_widget.setLayout(layout)
        
        #Widget central de la ventana
        self.setCentralWidget(central_widget)
    
    def boton_click(self):
        nombre = self.nombre_edit.text()
        edad = self.edad_edit.text()
        
        #Aquí se mostraran el nombre y la edad juntos centrados
        texto = f"Nombre: {nombre}\nEdad: {edad} años"
        self.label.setText(texto)


app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
sys.exit(app.exec_())

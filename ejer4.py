#Construir un programa que muestre una ventana a traves de la cuál se pueden leer tres 
#datos básicos de tres mascotas diferentes




from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QFormLayout, QLabel)
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 100, 600, 400)
        self.setWindowTitle("Datos de Tres Mascotas")

        #Widgets para los datos de la mascota 1
        self.nombre1_edit = QLineEdit()
        self.raza1_edit = QLineEdit()
        self.edad1_edit = QLineEdit()

        #Widgets para los datos de la mascota 2
        self.nombre2_edit = QLineEdit()
        self.raza2_edit = QLineEdit()
        self.edad2_edit = QLineEdit()

        #Widgets para los datos de la mascota 34
        self.nombre3_edit = QLineEdit()
        self.raza3_edit = QLineEdit()
        self.edad3_edit = QLineEdit()

        #Boton para enviar y mostrar los datos
        self.boton = QPushButton("Mostrar Datos de Mascotas")
        self.boton.clicked.connect(self.boton_click)

        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        #Apartado donde configuramos el layaout para mostrar los datos de las mascotas
        layout = QFormLayout()
        layout.addRow("Nombre Mascota 1:", self.nombre1_edit)
        layout.addRow("Raza Mascota 1:", self.raza1_edit)
        layout.addRow("Edad Mascota 1:", self.edad1_edit)

        layout.addRow("Nombre Mascota 2:", self.nombre2_edit)
        layout.addRow("Raza Mascota 2:", self.raza2_edit)
        layout.addRow("Edad Mascota 2:", self.edad2_edit)

        layout.addRow("Nombre Mascota 3:", self.nombre3_edit)
        layout.addRow("Raza Mascota 3:", self.raza3_edit)
        layout.addRow("Edad Mascota 3:", self.edad3_edit)

        layout.addWidget(self.boton)
        layout.addWidget(self.label)

        
        central_widget = QWidget()
        central_widget.setLayout(layout)

        
        self.setCentralWidget(central_widget)


#Función principal que muestra la informacion con las variables elegidas


    def boton_click(self):
        nombre1 = self.nombre1_edit.text()
        raza1 = self.raza1_edit.text()
        edad1 = self.edad1_edit.text()

        nombre2 = self.nombre2_edit.text()
        raza2 = self.raza2_edit.text()
        edad2 = self.edad2_edit.text()

        nombre3 = self.nombre3_edit.text()
        raza3 = self.raza3_edit.text()
        edad3 = self.edad3_edit.text()

        #Luego mostramos los datos almacenados
        texto = (f"Mascota 1: Nombre: {nombre1}, Raza: {raza1}, Edad: {edad1} años\n"
                 f"Mascota 2: Nombre: {nombre2}, Raza: {raza2}, Edad: {edad2} años\n"
                 f"Mascota 3: Nombre: {nombre3}, Raza: {raza3}, Edad: {edad3} años")
        self.label.setText(texto)


app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
sys.exit(app.exec_())

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

#Clase base de Qt (PySide)
#Se encarga de procesar los eventos (event loop)
app = QApplication()
#Crear el objeto ventana
# ventana = QPushButton("Botón PySide")
ventana = QMainWindow()
#Cambiar título
ventana.setWindowTitle("Hola Mundo con Pyside")
#Modificar dimensiones
ventana.resize(600, 400)
#Mostrar el objeto ventana
ventana.show()
#Se ejecuta la aplicación
sys.exit(app.exec())
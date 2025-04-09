#Signals y Slots
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signals & Slots")
        self.setFixedSize(400, 200)
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        #Conectar entry con label
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        disposicion = QVBoxLayout()
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)
        contenedor = QWidget()
        contenedor.setLayout(disposicion)
        self.setCentralWidget(contenedor)

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
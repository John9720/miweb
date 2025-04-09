import sys
from random import randint
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox, QPushButton, QDialog, \
    QDialogButtonBox, QVBoxLayout, QMessageBox, QWidget, QLineEdit


class VentanaNueva(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nueva Ventana")
        layout = QVBoxLayout()
        self.etiqueta = QLabel(f"Nueva Ventana: {randint(0,100)}")
        layout.addWidget(self.etiqueta)
        self.setLayout(layout)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nueva_ventana = VentanaNueva()
        self.setWindowTitle("Ventanas")
        self.boton = QPushButton("Mostrar/Ocultar nueva ventana")
        self.boton.clicked.connect(self.mostrar_nueva_ventana)
        self.entrada_texto = QLineEdit()
        self.entrada_texto.textChanged.connect(self.nueva_ventana.etiqueta.setText)
        layout = QVBoxLayout()
        layout.addWidget(self.boton)
        layout.addWidget(self.entrada_texto)
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)


    def mostrar_nueva_ventana(self, estado):
        if self.nueva_ventana.isVisible():
            self.nueva_ventana.hide()
        else:
            self.nueva_ventana.show()
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
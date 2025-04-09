import sys
from random import randint
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox, QPushButton, QDialog, \
    QDialogButtonBox, QVBoxLayout, QMessageBox, QWidget, QLineEdit, QMenu


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú Contextual")
        self.show()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.mostrar_menu_contexto)

    def mostrar_menu_contexto(self, posicion):
        menu_contextual = QMenu(self)
        boton_nuevo = QAction(QIcon("942290.png"), "Nuevo", self)
        boton_guardar = QAction(QIcon("967231.jpg"), "Guardar", self)
        boton_salir = QAction("Salir", self)
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)
        boton_salir.triggered.connect(self.click_boton_salir)
        menu_contextual.addAction(boton_nuevo)
        menu_contextual.addAction(boton_guardar)
        menu_contextual.addAction(boton_salir)
        menu_contextual.exec(self.mapToGlobal(posicion))

    def click_boton_nuevo(self, s):
        print("Opción Nuevo")

    def click_boton_guardar(self, ):
        print("Opción Guardar")

    def click_boton_salir(self, s):
        print("Opción Salir")

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
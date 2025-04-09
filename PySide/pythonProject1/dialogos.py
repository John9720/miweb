import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox, QPushButton, QDialog, \
    QDialogButtonBox, QVBoxLayout, QMessageBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barra de Herramientas")
        boton = QPushButton("Mostrar dálogo")
        boton.clicked.connect(self.click_boton)
        self.setCentralWidget(boton)

    def click_boton(self, s):
        print(f"Click sobre botón: {s}")
        dialogo = QMessageBox.critical(self, "Problema crítico", "Ventana con problema crítico", buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore, defaultButton=QMessageBox.Discard)

        if dialogo == QMessageBox.Discard:
            print("Regresó el valor Discard")
        elif dialogo == QMessageBox.NoToAll:
            print("Regresó valor NoToAll")
        else:
            print("Se presionó Ignore")

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
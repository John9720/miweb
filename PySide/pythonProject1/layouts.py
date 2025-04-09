from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, \
    QPushButton, QTabWidget
import sys

class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        self.setPalette(paletaColores)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabulador en PySide")
        tabulador = QTabWidget()
        tabulador.setTabPosition(QTabWidget.North)
        tabulador.setMovable(True)
        tabulador.addTab(Color("red"), "Rojo")
        tabulador.addTab(Color("yellow"), "Amarillo")
        tabulador.addTab(Color("green"), "Verde")

        self.setCentralWidget(tabulador)


if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
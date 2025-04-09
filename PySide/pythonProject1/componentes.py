from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox, QComboBox, QListWidget, QLineEdit, QSpinBox, \
    QDoubleSpinBox, QSlider, QDial
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Componentes")
        componente = QDial()
        componente.setRange(-5,50)
        componente.valueChanged.connect(self.cambio_valor)
        componente.sliderMoved.connect(self.slider_cambio_posicion)
        componente.sliderPressed.connect(self.slider_presionado)
        componente.sliderReleased.connect(self.slider_liberado)
        self.setCentralWidget(componente)

    def cambio_valor(self, nuevo_valor):
        print(f"Nuevo valor: {nuevo_valor}")

    def slider_cambio_posicion(self, nueva_posicion):
        print(f"Nueva posicion: {nueva_posicion}")

    def slider_presionado(self):
        print("Dial presionado")

    def slider_liberado(self):
        print("Dial liberado")


if __name__ == "__main__":
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())
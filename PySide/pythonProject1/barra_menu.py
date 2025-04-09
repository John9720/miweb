import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barra de Herramientas")
        etiqueta = QLabel("Hola")
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)

        barra = QToolBar("Mi barra de herramientas")
        barra.setIconSize(QSize(16,16))
        barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.addToolBar(barra)

        boton_nuevo = QAction(QIcon("967231.jpg"), "Nuevo", self)
        barra.addAction(boton_nuevo)
        self.setStatusBar(QStatusBar(self))
        boton_nuevo.setStatusTip(("Nuevo archivo"))
        boton_nuevo.triggered.connect(self.click_boton_nuevo)

        #boton_nuevo.setCheckable(True)

        boton_guardar = QAction(QIcon("942290.png"), "Guardar", self)
        barra.addAction(boton_guardar)
        boton_guardar.setStatusTip(("Guardar archivo"))
        boton_guardar.triggered.connect(self.click_boton_guardar)

        barra.addSeparator()

        barra.addWidget(QCheckBox())
        barra.addWidget(QLabel("Salir"))

        menu = self.menuBar()
        menu_archivo = menu.addMenu("Archivo")
        menu_archivo.addAction(boton_nuevo)
        menu_archivo.addAction(boton_guardar)
        menu_archivo.addSeparator()
        boton_salir = QAction(QIcon("Legend.jpg"), "Salir", self)
        menu_archivo.addAction(boton_salir)

        boton_acerca_de = QAction(QIcon("Legend.jpg"), "Acerca de", self)
        menu_ayuda = menu.addMenu("Ayuda")
        menu_ayuda.addAction(boton_acerca_de)
        boton_acerca_de.triggered.connect(self.click_boton_acerca_de)

        menu_archivo.addMenu(menu_ayuda)

        boton_nuevo.setShortcut(Qt.CTRL | Qt.Key_N)
        boton_guardar.setShortcut(Qt.CTRL | Qt.Key_G)
        boton_acerca_de.setShortcut(Qt.CTRL | Qt.Key_1)
    def click_boton_nuevo(self, s):
        print(f"Nuevo: {s}")

    def click_boton_guardar(self, s):
        print(f"Guardando: {s}")

    def click_boton_acerca_de(self, s):
        print(f"Acerca de: {s}")

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
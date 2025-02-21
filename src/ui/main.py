from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenid@")
        self.setFixedSize(QSize(480, 320))

        boton = QPushButton("Ingresar")
        boton.setCheckable(True)
        boton.clicked.connect(self.ingresar_alternado)
        
        self.setCentralWidget(boton)
        
        self.boton = boton
        
    def ingresar_alternado(self, valor):
        if valor:
            self.boton.setText("Activo")
        else:
            self.boton.setText("Desactivado")
        print("Ingreso", valor)    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
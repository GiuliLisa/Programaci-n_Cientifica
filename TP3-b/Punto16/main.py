#Reinaldo Giulianna
#2025
#Programación Científica

#16. Utilizando el framework de Qt designer implementará un botón para imprimir en pantalla “Hola soy <nombre>”. 

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from ventana_ui import Ui_Dialog  #Se importa la clase generada por pyuic5

class MiDialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #Se conecta el botón a la función que muestra el mensaje
        self.ui.btnSaludar.clicked.connect(self.saludar)

    def saludar(self):
        nombre = self.ui.lineNombre.text()
        if not nombre:
            nombre = "<nombre>"
        QMessageBox.information(self, "Saludo", f"Hola soy {nombre}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = MiDialogo()
    dialogo.show()
    sys.exit(app.exec_())

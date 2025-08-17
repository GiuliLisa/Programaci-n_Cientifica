import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from password import Ui_Dialog
import random
import string

class Contraseñas(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.longitud = 12
        self.caracteres = string.ascii_letters + string.digits + string.punctuation
        
        self.ui.btnGenerar.clicked.connect(self.generar_password)

    def generar_password(self):
        contraseña = ''.join(random.choice(self.caracteres) for _ in range(self.longitud))
        self.ui.lineC.setText(contraseña)
        QMessageBox.information(self, "Generada", "Contraseña generada correctamente.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Contraseñas()
    ventana.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from ventana_ui import Ui_Dialog  # Asegurate de que el nombre coincida con tu clase

class Agenda(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.proveedores = []
        self.indice_actual = 0

        # Conectar botones
        self.ui.btnGuardar.clicked.connect(self.guardar_proveedor)
        self.ui.btnSiguiente.clicked.connect(self.mostrar_siguiente)
        self.ui.btnAnterior.clicked.connect(self.mostrar_anterior)

        # Cargar los proveedores del archivo
        self.cargar_proveedores()

    def cargar_proveedores(self):
        try:
            with open("proveedores.txt", "r", encoding="utf-8") as f:
                lineas = f.readlines()
                self.proveedores = [line.strip().split(" - ") for line in lineas if " - " in line]
        except FileNotFoundError:
            self.proveedores = []

        self.indice_actual = 0
        self.mostrar_actual()

    def guardar_proveedor(self):
        nombre = self.ui.lineNombre.text().strip()
        contacto = self.ui.lineContacto.text().strip()

        if not nombre or not contacto:
            QMessageBox.warning(self, "Error", "Completá ambos campos para guardar.")
            return

        with open("proveedores.txt", "a", encoding="utf-8") as f:
            f.write(f"{nombre} - {contacto}\n")

        QMessageBox.information(self, "Guardado", "Proveedor guardado correctamente.")

        self.ui.lineNombre.clear()
        self.ui.lineContacto.clear()
        self.cargar_proveedores()

    def mostrar_actual(self):
        if self.proveedores:
            nombre, contacto = self.proveedores[self.indice_actual]
            self.ui.lineNombre2.setText(nombre)
            self.ui.lineContacto2.setText(contacto)
        else:
            self.ui.lineNombre2.setText("")
            self.ui.lineContacto2.setText("")

    def mostrar_siguiente(self):
        if self.indice_actual < len(self.proveedores) - 1:
            self.indice_actual += 1
            self.mostrar_actual()

    def mostrar_anterior(self):
        if self.indice_actual > 0:
            self.indice_actual -= 1
            self.mostrar_actual()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Agenda()
    ventana.show()
    sys.exit(app.exec_())




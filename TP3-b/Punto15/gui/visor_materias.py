from PyQt5.QtWidgets import (
    QWidget, QPushButton, QHBoxLayout, QGroupBox, QGridLayout,
    QLabel, QLineEdit, QVBoxLayout
)

class Aplicacion_Gui(QWidget):
    def __init__(self, logica):
        super().__init__()

        self.logica = logica  # Lógica recibida

        self.title = 'Mi aplicación'
        self.left = 80
        self.top = 80
        self.width = 400
        self.height = 420

        self.inicializar_GUI()
        self.actualizar_materia()

    def inicializar_GUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.distr_vertical = QVBoxLayout()

        # Caja de materias
        self.caja_materias = QGroupBox("Materia")
        distr_caja_materias = QGridLayout()
        self.caja_materias.setLayout(distr_caja_materias)

        self.etiqueta_nombre = QLabel('Nombre')
        self.txt_nombre = QLineEdit()

        self.etiqueta_semestre = QLabel('Semestre')
        self.txt_semestre = QLineEdit()

        self.etiqueta_profesor = QLabel('Profesor')
        self.txt_profesor = QLineEdit()

        self.etiqueta_nota = QLabel('Nota')
        self.txt_nota = QLineEdit()

        # Etiquetas
        distr_caja_materias.addWidget(self.etiqueta_nombre, 0, 0)
        distr_caja_materias.addWidget(self.etiqueta_semestre, 1, 0)
        distr_caja_materias.addWidget(self.etiqueta_profesor, 2, 0)
        distr_caja_materias.addWidget(self.etiqueta_nota, 3, 0)

        # Campos de texto
        distr_caja_materias.addWidget(self.txt_nombre, 0, 1)
        distr_caja_materias.addWidget(self.txt_semestre, 1, 1)
        distr_caja_materias.addWidget(self.txt_profesor, 2, 1)
        distr_caja_materias.addWidget(self.txt_nota, 3, 1)

        # Caja de botones
        self.caja_botones = QGroupBox()
        distr_caja_botones = QHBoxLayout()
        self.caja_botones.setLayout(distr_caja_botones)

        self.boton_retroceder = QPushButton("<<")
        self.boton_retroceder.clicked.connect(self.retroceder_materia)
        self.boton_avanzar = QPushButton(">>")
        self.boton_avanzar.clicked.connect(self.avanzar_materia)

        # Cambiar el color del botón:
        self.boton_avanzar.setStyleSheet("background-color: lightgreen; color: black;")
        self.boton_retroceder.setStyleSheet("background-color: lightcoral; color: white;")


        distr_caja_botones.addWidget(self.boton_retroceder)
        distr_caja_botones.addWidget(self.boton_avanzar)

        # Agregar todo al layout principal
        self.distr_vertical.addWidget(self.caja_materias)
        self.distr_vertical.addWidget(self.caja_botones)

        self.setLayout(self.distr_vertical)
        self.show()

    def actualizar_materia(self):
        actual = self.logica.dar_materia_actual()
        self.txt_nombre.setText(actual["Nombre"])
        self.txt_semestre.setText(actual["Semestre"])
        self.txt_profesor.setText(actual["Profesor"])
        self.txt_nota.setText(str(actual["Nota"]))

    def avanzar_materia(self):
          self.logica.avanzar()
          self.actualizar_materia()
    
    def retroceder_materia(self):
          self.logica.retroceder()
          self.actualizar_materia()
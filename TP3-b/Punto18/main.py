import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtMultimedia import QSound
from temporizador_ui import Ui_Dialog

class Temporizador(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnEmpezar.clicked.connect(self.iniciar_temporizador)

        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1 segundo
        self.timer.timeout.connect(self.actualizar_tiempo)

        self.tiempo_restante = QTime(0, 0, 0)

    def iniciar_temporizador(self):
        tiempo = self.ui.timeEdit.time()
        if tiempo == QTime(0, 0, 0):
            QMessageBox.warning(self, "Error", "Ingresá un tiempo válido.")
            return

        self.tiempo_restante = tiempo
        self.actualizar_lcd()
        self.timer.start()

    def actualizar_tiempo(self):
        if self.tiempo_restante == QTime(0, 0, 0):
            self.timer.stop()
            # Mostrar 00:00:00 o alguna alerta en el LCD (QLCDNumber no tiene texto, solo números)
            self.ui.lcdTiempo.display("000000")  # Se muestra como seis dígitos
            QSound.play("alarma.wav")
            return

        self.tiempo_restante = self.tiempo_restante.addSecs(-1)
        self.actualizar_lcd()

    def actualizar_lcd(self):
        # QLCDNumber muestra solo números, sin ":", así que convertimos hh:mm:ss en un string numérico
        texto = self.tiempo_restante.toString("hhmmss")
        self.ui.lcdTiempo.display(texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Temporizador()
    ventana.show()
    sys.exit(app.exec_())

#Reinaldo Giulianna
#2025
#Programación Científica

# 18. En una panadería se necesita un temporizador para controlar los tiempos de 
# cocción en un horno industrial. Dado que se hornean varios productos 
# simultáneamente, el operario debe poder ingresar el tiempo en minutos y 
# visualizar una cuenta regresiva en pantalla. Al llegar a cero, el temporizador 
# debe emitir un aviso claro. Se debe proponer una estrategia de aviso; se 
# presentan algunosejemplos como un cambio de color en pantalla, parpadeo 
# del temporizador o la emisión de un sonido. 

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtMultimedia import QSound
from temporizador_ui import Ui_Dialog

ruta_wav = os.path.join(os.path.dirname(__file__), "alarma.wav")

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

        #Ruta absoluta al archivo de sonido (misma carpeta que este .py)
        self.ruta_alarma = os.path.join(os.path.dirname(__file__), "alarma.wav")
        
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
            #Mostrar 00:00:00 o alguna alerta en el LCD (QLCDNumber no tiene texto, solo números)
            self.ui.lcdTiempo.display("000000")  #Se muestra como seis dígitos
            
            #Reproducir sonido de la alarma
            if os.path.isfile(self.ruta_alarma):
                QSound.play(self.ruta_alarma)
            else:
                QMessageBox.warning(self, "Error", f"No se encontró {self.ruta_alarma}")
            return

        self.tiempo_restante = self.tiempo_restante.addSecs(-1)
        self.actualizar_lcd()

    def actualizar_lcd(self):
        #QLCDNumber muestra solo números, sin ":", así que se convierte hh:mm:ss en un string numérico
        texto = self.tiempo_restante.toString("hhmmss")
        self.ui.lcdTiempo.display(texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Temporizador()
    ventana.show()
    sys.exit(app.exec_())
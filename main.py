import os
import pickle
import sys
import time

from PyQt6.QtCore import pyqtSignal

from Custom_Widgets.Widgets import QMainWindow
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication
from PyQt6.uic.uiparser import QtCore
from PySide6.QtCore import *
from PySide6.QtWidgets import QComboBox, QMenu
from PyQt6.QtCore import QThread

import Envio
from Conexion import Conexion
from Envio import *

import iconos
from ui_mercurio_prominente import *



class HiloConexion(QObject):
    signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()

    def run(self):
        signal = 1
        if Conexion._conexion is None:
            print('Estableciendo conexion...')
            Conexion.conexion()
            Envio.envio()




class VentanaPrincipal(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Boton Menu control de eventos
        self.boton_menu.setCheckable(True)
#        self.boton_menu.clicked.connect(self.evento_checar)
        self.boton_menu.clicked.connect(self.mover_menu)

        #Boton Prueba Diaria control de eventos
        self.boton1.setCheckable(True)
        self.boton1.clicked.connect(self.evento_checar_diaria)
        self.boton1.clicked.connect(self.mover_prueba_diaria)

        #Boton prueba general
        prueba = False

        self.boton_gral.setCheckable(True)
        self.boton_gral.clicked.connect(self.mover_widet7)
        self.conexion_label.setText('Conexion establecida')
        self.envio_msj.setText(f'Mensaje enviado con exito a:{Envio.destino}')
        self.sesion_cerrada_label.setText(f'Sesion cerrada')


        #HILO DE CONEXION Y ENVIO
        self.thread = QThread()
        self.worker = HiloConexion()

        self.worker.moveToThread(self.thread)

        self.boton_gral.clicked.connect(self.worker.run)
        #self.worker.finished.connect(self.thread.quit)
#       self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

        #Pagina 1 visualizacion de procesos


    def evento_checar(self,checar):
         self.botonchecado = checar
         print(f'Boton checado',self.botonchecado)

    def evento_checar_diaria(self,checar_diaria):
        self.boton_diaria_checado = checar_diaria
        print(f'Boton diaria checado',self.boton_diaria_checado)


    def mover_menu(self):
        self.width = self.menu_lateral.width()

        if self.width == 0:
            #ExpandMenu
            self.newWidth=147
        else:
            self.newWidth=0


        #Vincular la animacion de contraccion del menu general con los botones de prueba
        self.newHeight = 0
        self.animacion = QPropertyAnimation(self.botones_pruebas, b"maximumHeight")
        self.animacion.setDuration(700)
        self.animacion.setStartValue(self.newHeight)
        self.animacion.setEndValue(self.width)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()

        #Vincular animacion de boton menu con menu lateral
        self.animacion = QPropertyAnimation(self.menu_lateral, b"maximumWidth")
        # Animate minumWidth
        self.animacion.setDuration(500)
        self.animacion.setStartValue(self.width)
        self.animacion.setEndValue(self.newWidth)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()



    def mover_prueba_diaria(self):
        self.height = self.botones_pruebas.height()

        if self.height == 0:
            # ExpandirMenu
            self.newHeight = 75

        else:
            self.newHeight = 0


        #Animacion botones de prueba diaria (prueba general, particular)
        self.animacion = QPropertyAnimation(self.botones_pruebas, b"maximumHeight")
        # Animate minumWidth
        self.animacion.setDuration(500)
        self.animacion.setStartValue(self.height)
        self.animacion.setEndValue(self.newHeight)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()


    def mover_widet7(self):
        self.width_widget7 = self.widget_7.width()
        if self.width_widget7 == 0:
            self.newWidth_wiget7 = 500

        else:
            self.newWidth_wiget7 = 0

        self.animacion = QPropertyAnimation(self.widget_7, b"minimumWidth")
        self.animacion.setDuration(500)
        self.animacion.setStartValue(self.width_widget7)
        self.animacion.setEndValue(self.newWidth_wiget7)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()



        self.boton1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))

        # PAGINA 2
        self.boton2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))

        # PAGINA 3
        self.boton3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))

        # PAGINA 4
        self.boton4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))




        # PAGINA 1






if __name__ == '__main__':

    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

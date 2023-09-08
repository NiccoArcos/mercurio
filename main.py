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

import Conexion
from Envio import *

import iconos
from ui_mercurio_prominente import *



class VentanaPrincipal(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Boton Menu control de eventos
        self.boton_menu.setCheckable(True)
        self.boton_menu.clicked.connect(self.evento_checar)
        self.boton_menu.clicked.connect(self.mover_menu)

        #Boton Prueba Diaria control de eventos
        self.boton1.setCheckable(True)
        self.boton1.clicked.connect(self.evento_checar_diaria)
        self.boton1.clicked.connect(self.mover_prueba_diaria)

        #Boton prueba general
        prueba = False

        self.boton_gral.clicked.connect(lambda :self.mover_widet7(self.conexion()))
        #self.boton_gral.released.connect(self.conexion)
        self.boton_gral.setCheckable(True)
        self.boton_gral.clicked.connect(self.evento_checar)





        #self.boton_gral.clicked.connect(self.mover_barra_progreso)




        #Pagina 1 visualizacion de procesos


    def conexion(self):


        username = 'nicolas.arccos94@gmail.com'
        password = 'lrvwutkoxzctbosb'
        context = ssl.create_default_context()
        _conexion = None

        destino = 'nicolas.arccos94@gmail.com'
        mensaje = 'puchito <3'

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(username, password)
            print(f'Conexion establecida con exito')

            self.envio_msj.setText(f'Conexion establecida con exito a:{destino}')

            server.sendmail(username, destino, mensaje)

            self.conexion_label.setText(f'Mensaje enviado con exito.')

            print(f'Mensaje enviado a:{destino} con exito')
            server.close()

            self.sesion_cerrada_label.setText('Sesion cerrada con exito')
            print(f'Sesion cerrada con exito.')
            print(f'Accion finalizada con exito')


    # Barra de progreso
    def progress(self):
        self.progressBar.minimum = 1
        self.progressBar.maximum = 100
        for i in range (1,101):
            self.progressBar.setValue(i)


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


        #Contraccion barra de progreso
        self.newHeight = 0
        self.animacion = QPropertyAnimation(self.progressBar, b'maximumWidth')
        self.animacion.setDuration(700)
        self.animacion.setStartValue(self.newHeight)
        self.animacion.setEndValue(self.width)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()

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


      #Contraer barra de progreso al contraer los botones de prueba diaria
        self.newWidth = 0
        self.animacion = QPropertyAnimation(self.progressBar, b'maximumWidth')
        self.animacion.setDuration(700)
        self.animacion.setStartValue(self.newWidth)
        self.animacion.setEndValue(self.height)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()



        #Animacion botones de prueba diaria (prueba general, particular)
        self.animacion = QPropertyAnimation(self.botones_pruebas, b"maximumHeight")
        # Animate minumWidth
        self.animacion.setDuration(500)
        self.animacion.setStartValue(self.height)
        self.animacion.setEndValue(self.newHeight)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()

    def mover_widet7(self,conexion):

        self.width_widget7 = self.widget_7.width()
        if self.width_widget7 == 0:
            self.newWidth_wiget7= 1000

        else:
            self.newWidth_wiget7 = 0


        self.animacion = QPropertyAnimation(self.widget_7, b"maximumWidth")
        self.animacion.setDuration(500)
        self.animacion.setStartValue(self.width_widget7)
        self.animacion.setEndValue(self.newWidth_wiget7)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()




    def mover_barra_progreso(self):
        self.width = self.progressBar.width()
        if self.width == 0:
            self.newWidth = 16777215
        else:
            self.newWidth = 0

        self.animacion = QPropertyAnimation(self.progressBar, b"maximumWidth")
        self.animacion.setDuration(5)
        self.animacion.setStartValue(self.width)
        self.animacion.setEndValue(self.newWidth)
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

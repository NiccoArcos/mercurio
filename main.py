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
            Conexion.conexion()
            Envio.envio()



class VentanaPrincipal(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.bandera_local = False
        self.bandera_externa = False
        self.bandera_nube = False
        #Boton Menu control de eventos
        self.boton_menu.setCheckable(True)
#        self.boton_menu.clicked.connect(self.evento_checar)
#
        self.boton_menu.clicked.connect(self.mover_menu)

        #Boton Prueba Diaria control de eventos
        self.boton1.setCheckable(True)
        self.boton1.clicked.connect(self.evento_checar_diaria)
        self.boton1.clicked.connect(self.mover_cabecera_custom_1)
        #Boton prueba general

        self.btn_gral_2.setCheckable(True)
        self.btn_gral_2.clicked.connect(self.evento_checar_btn_gral_2)
        self.btn_gral_2.clicked.connect(self.mover_columnas_custom_1)
        # Boton prueba personalizada
        self.btn_particular_prt_2.setCheckable(True)
        self.btn_particular_prt_2.clicked.connect(self.evento_checar_btn_particular_2)




        #combo origen externo

        self.combo_origen_ext.currentIndexChanged.connect(self.evento_checar_indice_origen_ext)
        self.ruta_origen_ext.clicked.connect(self.mover_info_prueba_ext)

        # combo origen local

        self.combo_origen_loc.currentIndexChanged.connect(self.evento_checar_indice_origen_loc)
        self.ruta_origen_loc.clicked.connect(self.mover_info_prueba_loc)

        #combo origen nube
        self.combo_origen_nub.currentIndexChanged.connect(self.evento_checar_indice_origen_nub)
        self.ruta_origen_nub.clicked.connect(self.mover_info_prueba_nub)




        #HILO DE CONEXION Y ENVIO
        self.thread = QThread()
        self.worker = HiloConexion()
        self.worker.moveToThread(self.thread)
        #self.boton_gral.clicked.connect(self.worker.run)
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

    def evento_checar_btn_gral_2(self,checar_general_2):
        self.boton_general_2 = checar_general_2
        print(f'Boton General checado',self.boton_general_2)

    def evento_checar_btn_particular_2(self,checar_btn_particular_2):
        self.boton_particular_2 = checar_btn_particular_2
        print(f'Boton particular checado',self.boton_particular_2)



    def evento_checar_indice_origen_ext(self,nuevo_indice):
        if self.combo_origen_ext.currentIndex() == 1:
            self.combo_origen_nub.setDisabled(True)
            self.combo_origen_loc.setDisabled(True)

        else:
            self.combo_origen_loc.setDisabled(False)
            self.combo_origen_nub.setDisabled(False)
        print(f'Nuevo indice seleccionado:{nuevo_indice}')

    def evento_checar_indice_origen_loc(self,nuevo_indice):
        indices = 1,2,3,4,5,6,7
        for indice in indices:
            self.combo_origen_ext.setDisabled(True)
            self.combo_origen_nub.setDisabled(True)
            if nuevo_indice == 0:
                self.combo_origen_ext.setDisabled(False)
                self.combo_origen_nub.setDisabled(False)
        print(f'Nuevo indice seleccionado:{nuevo_indice}')



    def evento_checar_indice_origen_nub(self,nuevo_indice):
        indices = 1,2
        for indice in indices:
            self.combo_origen_loc.setDisabled(True)
            self.combo_origen_ext.setDisabled(True)
            if nuevo_indice == 0:
                self.combo_origen_loc.setDisabled(False)
                self.combo_origen_ext.setDisabled(False)



    def mover_info_prueba_nub(self):
        self.width_nub = self.page_2_2.width()
        if (self.combo_origen_nub.currentIndex() == 1 or self.combo_origen_nub.currentIndex() == 2):
            if self.width_nub == 0:
                self.newWidth_nub = 1000
            else:
                self.newWidth_nub = 0
        self.animacion = QPropertyAnimation(self.page_2_2, b"maximumWidth")
        self.animacion.setDuration(900)
        self.animacion.setStartValue(self.width_nub)
        self.animacion.setEndValue(self.newWidth_nub)
        self.animacion.setEasingCurve(QEasingCurve.InCubic)
        self.animacion.start()


    def mover_info_prueba_loc(self, nuevo_indice):

        self.width_loc = self.page_2_3.width()
        if (self.combo_origen_loc.currentIndex() == 1 or self.combo_origen_loc.currentIndex() == 2
                or self.combo_origen_loc.currentIndex() == 3 or self.combo_origen_loc.currentIndex() == 4
                or self.combo_origen_loc.currentIndex() == 5):

            if self.width_loc == 0:
                self.newWidth_loc = 1000
            else:
                self.newWidth_loc = 0

        self.animacion = QPropertyAnimation(self.page_2_3, b"maximumWidth")
        self.animacion.setDuration(900)
        self.animacion.setStartValue(self.width_loc)
        self.animacion.setEndValue(self.newWidth_loc)
        self.animacion.setEasingCurve(QEasingCurve.InCubic)
        self.animacion.start()



    def mover_info_prueba_ext(self, nuevo_indice):
        self.width_ext = self.page_2_1.width()
        if (self.combo_origen_ext.currentIndex() == 1 and self.width_ext == 0):
            self.newWidth_ext = 1000
        else:
            self.newWidth_ext = 0


        self.animacion = QPropertyAnimation(self.page_2_1, b"maximumWidth")
        self.animacion.setDuration(900)
        self.animacion.setStartValue(self.width_ext)
        self.animacion.setEndValue(self.newWidth_ext)
        self.animacion.setEasingCurve(QEasingCurve.InCubic)
        self.animacion.start()





    def mover_menu(self):
        self.width = self.menu_lateral.width()

        if self.width == 0:
            #ExpandMenu
            self.newWidth=900
        else:
            self.newWidth=0


    # Vincular animacion de boton menu con menu lateral
        self.animacion = QPropertyAnimation(self.menu_lateral, b"maximumWidth")
    # Animate minumWidth
        self.animacion.setDuration(900)
        self.animacion.setStartValue(self.width)
        self.animacion.setEndValue(self.newWidth)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()



    def mover_cabecera_custom_1(self):
        self.width = self.frame_btns_cabecera_custom_1.width()
        if self.width == 0:
            self.newWidth = 1000

        else:
            self.newWidth = 0

        self.newHeight = 0
        self.height = 0
        self.animacion = QPropertyAnimation(self.columnas_custom_1, b"maximumHeight")
        self.animacion.setDuration(900)
        self.animacion.setStartValue(self.height)
        self.animacion.setEndValue(self.newHeight)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()

        self.animacion = QPropertyAnimation(self.frame_btns_cabecera_custom_1, b"maximumWidth")
        self.animacion.setDuration(900)
        self.animacion.setStartValue(self.width)
        self.animacion.setEndValue(self.newWidth)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()





    def mover_columnas_custom_1(self):
        self.height = self.columnas_custom_1.height()
        if self.height == 0:
            self.newHeight = 1000
        else:
            self.newHeight = 0
        self.animacion = QPropertyAnimation(self.columnas_custom_1, b"maximumHeight")
        self.animacion.setDuration(900)
        self.animacion.setStartValue(self.height)
        self.animacion.setEndValue(self.newHeight)
        self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
        self.animacion.start()




        # PAGINA 1
        self.boton1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina1))

        self.btn_gral_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina1))

        #PAGINA 1.2
        self.btn_particular_prt_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina2))

        #PAGINA 4
        self.boton4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina4))

        #PAGINAS DE RUTAS DE ENVIO
        self.ruta_origen_ext.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_2_1))
        self.ruta_origen_loc.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_2_3))
        self.ruta_origen_nub.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_2_2))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

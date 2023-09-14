from time import sleep

import self
from PySide6.QtCore import QThread

from Conexion import *
from Conexion import Conexion
from ui_mercurio_prominente import *



import logging as log
import smtplib
import ssl
import sys
from Conexion import *


class Envio(Conexion,Ui_MainWindow):


    destino = 'nicolas.arccos94@gmail.com'
    mensaje = 'test'

    @classmethod
    def envio(cls):
        mensaje = Conexion.conexion().sendmail(cls.username,cls.destino,cls.mensaje)
        print(f'Mensaje enviado a:{cls.destino} con éxito')

        Conexion.conexion().close()
        print(f'Sesion cerrada con éxito.')
        print(f'Accion finalizada con exito')











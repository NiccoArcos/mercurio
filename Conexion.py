import logging as log
import smtplib
import ssl
import sys

from PySide6.QtCore import QThread


class Conexion(QThread):
    username = 'nicolas.arccos94@gmail.com'
    password = "debe vincular una app password"
    context = ssl.create_default_context()
    _conexion = None

    @classmethod
    def conexion(cls):
        # Crear la conexión
        if cls._conexion is None:

            try:
                cls._conexion = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=cls.context)
                cls._conexion.login(cls.username, cls.password)

                print(f'Conexion establecida con exito')
                print(cls._conexion)
                return cls._conexion

            except Exception as e:
                print(f'Ocurrio un problema del tipo:{e} al intentar establecer la conexion'
                      f'al servidor de Exchange')
                sys.exit()

        else:
            return cls._conexion



    @property
    def conexione(cls):
        return cls._conexion

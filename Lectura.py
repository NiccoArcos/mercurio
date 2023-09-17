import ssl

from Conexion import Conexion
import imaplib
import email
from email.header import decode_header
import webbrowser
import os


class Lectura(Conexion):
    username = 'nicolas.arccos94@gmail.com'
    password = 'mhmzvocbhqlsadzl'

    @classmethod
    def lectura(cls):

        imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        imap.login(cls.username, cls.password)
        status, mensajes = imap.select("inbox")
        print(mensajes)

        N = 3




a = Lectura.lectura()
print(a)
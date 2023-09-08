# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazXwMyWO.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import imagenes
import iconos

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 717)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-image: url(:/imagenes/bg4-1.png);\n"
"}\n"
"\n"
"#cabecera{\n"
"	background-color: #025a7d;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#widget_7{\n"
"	border: solid #8f8f91;\n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"\n"
"}	\n"
"\n"
"#enviado_con_exito{\n"
"	background-color:#025a7d;\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"#menu_lateral{\n"
"	background-color: #025a7d;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#botones_pruebas{\n"
"	background-color: #025a7d;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    border: solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    min-width: 80px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cabecera = QFrame(self.centralwidget)
        self.cabecera.setObjectName(u"cabecera")
        self.cabecera.setMinimumSize(QSize(0, 50))
        self.cabecera.setMaximumSize(QSize(16777215, 50))
        self.cabecera.setFrameShape(QFrame.StyledPanel)
        self.cabecera.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.cabecera)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.cabecera)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.boton_menu = QPushButton(self.frame)
        self.boton_menu.setObjectName(u"boton_menu")
        icon = QIcon()
        icon.addFile(u":/iconos/Iconos/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_menu.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.boton_menu)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(self.cabecera)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.cabecera, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_lateral = QFrame(self.frame_4)
        self.menu_lateral.setObjectName(u"menu_lateral")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menu_lateral.sizePolicy().hasHeightForWidth())
        self.menu_lateral.setSizePolicy(sizePolicy2)
        self.menu_lateral.setMinimumSize(QSize(0, 400))
        self.menu_lateral.setMaximumSize(QSize(0, 16777215))
        self.menu_lateral.setFrameShape(QFrame.StyledPanel)
        self.menu_lateral.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_lateral)
        self.gridLayout.setObjectName(u"gridLayout")
        self.boton5 = QPushButton(self.menu_lateral)
        self.boton5.setObjectName(u"boton5")
        font = QFont()
        font.setPointSize(12)
        self.boton5.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/iconos/Iconos/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton5.setIcon(icon1)

        self.gridLayout.addWidget(self.boton5, 4, 0, 1, 1)

        self.boton4 = QPushButton(self.menu_lateral)
        self.boton4.setObjectName(u"boton4")
        self.boton4.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/iconos/Iconos/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton4.setIcon(icon2)

        self.gridLayout.addWidget(self.boton4, 3, 0, 1, 1)

        self.boton3 = QPushButton(self.menu_lateral)
        self.boton3.setObjectName(u"boton3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.boton3.sizePolicy().hasHeightForWidth())
        self.boton3.setSizePolicy(sizePolicy3)
        self.boton3.setMinimumSize(QSize(80, 0))
        self.boton3.setMaximumSize(QSize(16777215, 16777215))
        self.boton3.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/iconos/Iconos/server.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton3.setIcon(icon3)

        self.gridLayout.addWidget(self.boton3, 2, 0, 1, 1)

        self.boton1 = QPushButton(self.menu_lateral)
        self.boton1.setObjectName(u"boton1")
        self.boton1.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/iconos/Iconos/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton1.setIcon(icon4)

        self.gridLayout.addWidget(self.boton1, 0, 0, 1, 1)

        self.boton2 = QPushButton(self.menu_lateral)
        self.boton2.setObjectName(u"boton2")
        self.boton2.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/iconos/Iconos/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton2.setIcon(icon5)

        self.gridLayout.addWidget(self.boton2, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.menu_lateral, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(30, 0))
        self.frame_6.setMaximumSize(QSize(95, 75))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.botones_pruebas = QFrame(self.frame_6)
        self.botones_pruebas.setObjectName(u"botones_pruebas")
        self.botones_pruebas.setMinimumSize(QSize(0, 0))
        self.botones_pruebas.setMaximumSize(QSize(1677800, 0))
        self.botones_pruebas.setFrameShape(QFrame.StyledPanel)
        self.botones_pruebas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.botones_pruebas)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.boton_gral = QPushButton(self.botones_pruebas)
        self.boton_gral.setObjectName(u"boton_gral")
        icon6 = QIcon()
        icon6.addFile(u":/iconos/Iconos/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_gral.setIcon(icon6)

        self.verticalLayout_10.addWidget(self.boton_gral)

        self.boton_particular = QPushButton(self.botones_pruebas)
        self.boton_particular.setObjectName(u"boton_particular")
        icon7 = QIcon()
        icon7.addFile(u":/iconos/Iconos/crosshair.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_particular.setIcon(icon7)

        self.verticalLayout_10.addWidget(self.boton_particular)


        self.verticalLayout_4.addWidget(self.botones_pruebas, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.widget_7 = QWidget(self.page)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy2.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy2)
        self.widget_7.setMinimumSize(QSize(0, 350))
        self.widget_7.setMaximumSize(QSize(0, 300))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 200)
        self.widget_2 = QWidget(self.widget_7)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/iconos/Iconos/check.svg"))

        self.verticalLayout_5.addWidget(self.label)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/iconos/Iconos/check.svg"))

        self.verticalLayout_5.addWidget(self.label_2)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/iconos/Iconos/check.svg"))

        self.verticalLayout_5.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.widget_2, 0, Qt.AlignLeft)

        self.widget = QWidget(self.widget_7)
        self.widget.setObjectName(u"widget")
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.envio_msj = QLabel(self.widget)
        self.envio_msj.setObjectName(u"envio_msj")
        font1 = QFont()
        font1.setFamilies([u"Garamond"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.envio_msj.setFont(font1)

        self.verticalLayout_6.addWidget(self.envio_msj)

        self.conexion_label = QLabel(self.widget)
        self.conexion_label.setObjectName(u"conexion_label")
        self.conexion_label.setFont(font1)

        self.verticalLayout_6.addWidget(self.conexion_label)

        self.sesion_cerrada_label = QLabel(self.widget)
        self.sesion_cerrada_label.setObjectName(u"sesion_cerrada_label")
        self.sesion_cerrada_label.setFont(font1)

        self.verticalLayout_6.addWidget(self.sesion_cerrada_label)


        self.horizontalLayout_5.addWidget(self.widget)


        self.verticalLayout_3.addWidget(self.widget_7, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.page)
        self.widget_7.raise_()
        self.frame_6.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(45)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_7 = QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.page_4)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(40)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boton_menu.setText("")
        self.boton5.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.boton4.setText(QCoreApplication.translate("MainWindow", u"Estadisticas Test", None))
        self.boton3.setText(QCoreApplication.translate("MainWindow", u"Disponibilidad", None))
        self.boton1.setText(QCoreApplication.translate("MainWindow", u"Prueba Diaria", None))
        self.boton2.setText(QCoreApplication.translate("MainWindow", u"Actividad Hosts", None))
        self.boton_gral.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.boton_particular.setText(QCoreApplication.translate("MainWindow", u"Particular", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_6.setText("")
        self.envio_msj.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.conexion_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.sesion_cerrada_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PAGINA 2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PAGINA 3 ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PAGINA 4", None))
    # retranslateUi


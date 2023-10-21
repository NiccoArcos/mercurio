# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazpDoJHa.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

import imagenes
import iconos

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1048, 674)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(9)
        font.setItalic(False)
        MainWindow.setFont(font)
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
"	\n"
"#menu_lateral{\n"
"	background-color: #025a7d;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#botones_pruebas{\n"
"	background-color: #025a7d;\n"
"	border-radius: 8px;\n"
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
"}\n"
"QPushButton:hover{\n"
"	border:1px solid  #025a7d; \n"
"	background-color: #fcc253;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#frame_btns_cabecera_custom_1{background-color: #025a7d;\n"
"	border-radius: 6px\n"
"}\n"
"\n"
"#frame_btns_ejec_1{background-color: #025a7d;\n"
"	border-radius: 6px\n"
"}\n"
"\n"
"\n"
"#frame_nub{\n"
"	border: solid #8f8f91;\n"
"    border-rad"
                        "ius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"#clm_nub_gral{background-color: #025a7d;\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"\n"
"\n"
"#frame_lcl{\n"
"	border: solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    min-width: 80px;\n"
"}\n"
"#clm_lcl_gral{\n"
"	background-color: #025a7d;\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"#frame_ori{border: solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    min-width: 80px;\n"
"\n"
"}\n"
"\n"
"#clm_ori_gral{\n"
"	background-color: #025a7d;\n"
"	border-radius: 20px\n"
"}\n"
"	\n"
"#btns_ejecutar_prueba{\n"
"	background-color: #025a7d;\n"
"	b"
                        "order-radius: 8px\n"
"}\n"
"\n"
"#frame_ejec{\n"
"	background-color: #025a7d;\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"#frame_btns_cabecera_custom_2{background-color: #025a7d;\n"
"	border-radius: 6px\n"
"}\n"
"\n"
"#clm_ori_perso{background-color: #025a7d;\n"
"	border-radius: 20px\n"
"}\n"
"#frame_ori_perso_5{border: solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"#frame_ori_lcl_4{border: solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"#frame_ori_nub_4{border: solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    mi"
                        "n-width: 80px;\n"
"}\n"
"\n"
"#clm_dest_perso{background-color: #025a7d;\n"
"	border-radius: 20px\n"
"}\n"
"\n"
"#frame_perso_dest_lcl{\n"
"border: solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"#frame_perso_dest_nub{\n"
"border: solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"#frame_perso_dest_ext{\n"
"border: solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"#frame_btns_ejec_perso{background-color: #025a7d;\n"
"	border-radius: 6px\n"
"}\n"
"\n"
"#frame_btns_ejec_4{background-c"
                        "olor: #025a7d;\n"
"	border-radius: 6px\n"
"}\n"
"\n"
"#frame_12{background-color: #fff;\n"
"	border-radius: 20px\n"
"}\n"
"")
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
        self.boton_menu.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.boton_menu)


        self.horizontalLayout_2.addWidget(self.frame)


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
        self.menu_lateral.setMinimumSize(QSize(0, 450))
        self.menu_lateral.setMaximumSize(QSize(150, 16777215))
        self.menu_lateral.setFrameShape(QFrame.StyledPanel)
        self.menu_lateral.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_lateral)
        self.gridLayout.setObjectName(u"gridLayout")
        self.boton1 = QPushButton(self.menu_lateral)
        self.boton1.setObjectName(u"boton1")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.boton1.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/iconos/Iconos/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton1.setIcon(icon1)

        self.gridLayout.addWidget(self.boton1, 0, 0, 1, 1)

        self.boton2 = QPushButton(self.menu_lateral)
        self.boton2.setObjectName(u"boton2")
        self.boton2.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/iconos/Iconos/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton2.setIcon(icon2)

        self.gridLayout.addWidget(self.boton2, 1, 0, 1, 1)

        self.boton3 = QPushButton(self.menu_lateral)
        self.boton3.setObjectName(u"boton3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.boton3.sizePolicy().hasHeightForWidth())
        self.boton3.setSizePolicy(sizePolicy3)
        self.boton3.setMinimumSize(QSize(80, 0))
        self.boton3.setMaximumSize(QSize(16777215, 16777215))
        self.boton3.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/iconos/Iconos/server.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton3.setIcon(icon3)

        self.gridLayout.addWidget(self.boton3, 2, 0, 1, 1)

        self.boton4 = QPushButton(self.menu_lateral)
        self.boton4.setObjectName(u"boton4")
        self.boton4.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/iconos/Iconos/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton4.setIcon(icon4)

        self.gridLayout.addWidget(self.boton4, 3, 0, 1, 1)

        self.boton5 = QPushButton(self.menu_lateral)
        self.boton5.setObjectName(u"boton5")
        self.boton5.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/iconos/Iconos/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boton5.setIcon(icon5)

        self.gridLayout.addWidget(self.boton5, 4, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.menu_lateral, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 500))
        self.stackedWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.pagina1 = QWidget()
        self.pagina1.setObjectName(u"pagina1")
        self.pagina1.setMinimumSize(QSize(0, 557))
        self.pagina1.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_20 = QVBoxLayout(self.pagina1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_3 = QFrame(self.pagina1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cabecera_custom_1 = QFrame(self.frame_3)
        self.cabecera_custom_1.setObjectName(u"cabecera_custom_1")
        self.cabecera_custom_1.setMaximumSize(QSize(16777215, 16777215))
        self.cabecera_custom_1.setFrameShape(QFrame.StyledPanel)
        self.cabecera_custom_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.cabecera_custom_1)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_btns_cabecera_custom_1 = QFrame(self.cabecera_custom_1)
        self.frame_btns_cabecera_custom_1.setObjectName(u"frame_btns_cabecera_custom_1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_btns_cabecera_custom_1.sizePolicy().hasHeightForWidth())
        self.frame_btns_cabecera_custom_1.setSizePolicy(sizePolicy5)
        self.frame_btns_cabecera_custom_1.setMinimumSize(QSize(0, 0))
        self.frame_btns_cabecera_custom_1.setMaximumSize(QSize(1000, 16777215))
        self.frame_btns_cabecera_custom_1.setFrameShape(QFrame.StyledPanel)
        self.frame_btns_cabecera_custom_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_btns_cabecera_custom_1)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.btn_gral_2 = QPushButton(self.frame_btns_cabecera_custom_1)
        self.btn_gral_2.setObjectName(u"btn_gral_2")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.btn_gral_2.setFont(font2)
        icon6 = QIcon()
        icon6.addFile(u":/iconos/Iconos/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gral_2.setIcon(icon6)

        self.horizontalLayout_35.addWidget(self.btn_gral_2)

        self.btn_particular_prt_2 = QPushButton(self.frame_btns_cabecera_custom_1)
        self.btn_particular_prt_2.setObjectName(u"btn_particular_prt_2")
        self.btn_particular_prt_2.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u":/iconos/Iconos/target.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_particular_prt_2.setIcon(icon7)

        self.horizontalLayout_35.addWidget(self.btn_particular_prt_2)


        self.verticalLayout_29.addWidget(self.frame_btns_cabecera_custom_1)


        self.verticalLayout_4.addWidget(self.cabecera_custom_1, 0, Qt.AlignTop)

        self.columnas_custom_1 = QFrame(self.frame_3)
        self.columnas_custom_1.setObjectName(u"columnas_custom_1")
        sizePolicy1.setHeightForWidth(self.columnas_custom_1.sizePolicy().hasHeightForWidth())
        self.columnas_custom_1.setSizePolicy(sizePolicy1)
        self.columnas_custom_1.setMinimumSize(QSize(0, 0))
        self.columnas_custom_1.setMaximumSize(QSize(16777215, 0))
        self.columnas_custom_1.setFrameShape(QFrame.StyledPanel)
        self.columnas_custom_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.columnas_custom_1)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_btns_ejec_1 = QFrame(self.columnas_custom_1)
        self.frame_btns_ejec_1.setObjectName(u"frame_btns_ejec_1")
        self.frame_btns_ejec_1.setFrameShape(QFrame.StyledPanel)
        self.frame_btns_ejec_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_btns_ejec_1)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.pushButton_27 = QPushButton(self.frame_btns_ejec_1)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setFont(font2)
        icon8 = QIcon()
        icon8.addFile(u":/iconos/Iconos/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_27.setIcon(icon8)

        self.horizontalLayout_39.addWidget(self.pushButton_27)

        self.pushButton_28 = QPushButton(self.frame_btns_ejec_1)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setFont(font2)
        icon9 = QIcon()
        icon9.addFile(u":/iconos/Iconos/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_28.setIcon(icon9)

        self.horizontalLayout_39.addWidget(self.pushButton_28)

        self.pushButton_29 = QPushButton(self.frame_btns_ejec_1)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setFont(font2)
        icon10 = QIcon()
        icon10.addFile(u":/iconos/Iconos/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_29.setIcon(icon10)

        self.horizontalLayout_39.addWidget(self.pushButton_29)


        self.gridLayout_2.addWidget(self.frame_btns_ejec_1, 1, 0, 1, 3, Qt.AlignBottom)

        self.clm_lcl_gral = QFrame(self.columnas_custom_1)
        self.clm_lcl_gral.setObjectName(u"clm_lcl_gral")
        sizePolicy1.setHeightForWidth(self.clm_lcl_gral.sizePolicy().hasHeightForWidth())
        self.clm_lcl_gral.setSizePolicy(sizePolicy1)
        self.clm_lcl_gral.setFrameShape(QFrame.StyledPanel)
        self.clm_lcl_gral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.clm_lcl_gral)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_lcl = QFrame(self.clm_lcl_gral)
        self.frame_lcl.setObjectName(u"frame_lcl")
        self.horizontalLayout_37 = QHBoxLayout(self.frame_lcl)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_82 = QLabel(self.frame_lcl)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setPixmap(QPixmap(u":/iconos/Iconos/server.svg"))

        self.horizontalLayout_37.addWidget(self.label_82, 0, Qt.AlignRight)

        self.label_83 = QLabel(self.frame_lcl)
        self.label_83.setObjectName(u"label_83")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setItalic(True)
        self.label_83.setFont(font3)

        self.horizontalLayout_37.addWidget(self.label_83)

        self.label_84 = QLabel(self.frame_lcl)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setPixmap(QPixmap(u":/iconos/Iconos/server.svg"))

        self.horizontalLayout_37.addWidget(self.label_84)


        self.verticalLayout_6.addWidget(self.frame_lcl)

        self.label_85 = QLabel(self.clm_lcl_gral)
        self.label_85.setObjectName(u"label_85")
        sizePolicy.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy)
        self.label_85.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(14)
        self.label_85.setFont(font4)
        self.label_85.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_85.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_85, 0, Qt.AlignHCenter)

        self.label = QLabel(self.clm_lcl_gral)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.clm_lcl_gral)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.clm_lcl_gral)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(self.clm_lcl_gral)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(self.clm_lcl_gral)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.label_7 = QLabel(self.clm_lcl_gral)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_7, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.clm_lcl_gral, 0, 1, 1, 1)

        self.clm_ori_gral = QFrame(self.columnas_custom_1)
        self.clm_ori_gral.setObjectName(u"clm_ori_gral")
        sizePolicy1.setHeightForWidth(self.clm_ori_gral.sizePolicy().hasHeightForWidth())
        self.clm_ori_gral.setSizePolicy(sizePolicy1)
        self.clm_ori_gral.setFrameShape(QFrame.StyledPanel)
        self.clm_ori_gral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.clm_ori_gral)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_ori = QFrame(self.clm_ori_gral)
        self.frame_ori.setObjectName(u"frame_ori")
        font5 = QFont()
        font5.setPointSize(9)
        self.frame_ori.setFont(font5)
        self.frame_ori.setFrameShape(QFrame.StyledPanel)
        self.frame_ori.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_ori)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.frame_ori)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/iconos/Iconos/map-pin.svg"))

        self.horizontalLayout_6.addWidget(self.label_10, 0, Qt.AlignRight)

        self.label_79 = QLabel(self.frame_ori)
        self.label_79.setObjectName(u"label_79")
        font6 = QFont()
        font6.setPointSize(13)
        font6.setBold(True)
        font6.setItalic(True)
        font6.setUnderline(False)
        self.label_79.setFont(font6)
        self.label_79.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_79, 0, Qt.AlignTop)

        self.label_80 = QLabel(self.frame_ori)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setPixmap(QPixmap(u":/iconos/Iconos/map-pin.svg"))

        self.horizontalLayout_6.addWidget(self.label_80)


        self.verticalLayout_9.addWidget(self.frame_ori, 0, Qt.AlignBottom)

        self.frame_10 = QFrame(self.clm_ori_gral)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_10)


        self.gridLayout_2.addWidget(self.clm_ori_gral, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.columnas_custom_1)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy6 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy6)
        self.progressBar.setMaximumSize(QSize(0, 16777215))
        self.progressBar.setValue(24)

        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 3)

        self.clm_nub_gral = QFrame(self.columnas_custom_1)
        self.clm_nub_gral.setObjectName(u"clm_nub_gral")
        sizePolicy1.setHeightForWidth(self.clm_nub_gral.sizePolicy().hasHeightForWidth())
        self.clm_nub_gral.setSizePolicy(sizePolicy1)
        self.clm_nub_gral.setFrameShape(QFrame.StyledPanel)
        self.clm_nub_gral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.clm_nub_gral)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_nub = QFrame(self.clm_nub_gral)
        self.frame_nub.setObjectName(u"frame_nub")
        self.frame_nub.setFrameShape(QFrame.StyledPanel)
        self.frame_nub.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_nub)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_86 = QLabel(self.frame_nub)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setPixmap(QPixmap(u":/iconos/Iconos/cloud.svg"))

        self.horizontalLayout_38.addWidget(self.label_86, 0, Qt.AlignRight)

        self.label_87 = QLabel(self.frame_nub)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font3)

        self.horizontalLayout_38.addWidget(self.label_87)

        self.label_88 = QLabel(self.frame_nub)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setPixmap(QPixmap(u":/iconos/Iconos/cloud.svg"))

        self.horizontalLayout_38.addWidget(self.label_88)


        self.verticalLayout_17.addWidget(self.frame_nub)

        self.frame_14 = QFrame(self.clm_nub_gral)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_14)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_18.addWidget(self.label_16)

        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_18.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_18.addWidget(self.label_15, 0, Qt.AlignHCenter)

        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_18.addWidget(self.label_13)


        self.verticalLayout_17.addWidget(self.frame_14)


        self.gridLayout_2.addWidget(self.clm_nub_gral, 0, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.columnas_custom_1)


        self.verticalLayout_20.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.pagina1)
        self.pagina5 = QWidget()
        self.pagina5.setObjectName(u"pagina5")
        self.horizontalLayout_5 = QHBoxLayout(self.pagina5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_6 = QFrame(self.pagina5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.pagina5)
        self.pagina4 = QWidget()
        self.pagina4.setObjectName(u"pagina4")
        self.verticalLayout_3 = QVBoxLayout(self.pagina4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_9 = QFrame(self.pagina4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.pagina4)
        self.pagina2 = QWidget()
        self.pagina2.setObjectName(u"pagina2")
        self.pagina2.setMinimumSize(QSize(0, 557))
        self.verticalLayout_8 = QVBoxLayout(self.pagina2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_7 = QFrame(self.pagina2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.cabecera_custom_5 = QFrame(self.frame_7)
        self.cabecera_custom_5.setObjectName(u"cabecera_custom_5")
        self.cabecera_custom_5.setMaximumSize(QSize(16777215, 16777215))
        self.cabecera_custom_5.setFrameShape(QFrame.StyledPanel)
        self.cabecera_custom_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.cabecera_custom_5)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_btns_cabecera_custom_2 = QFrame(self.cabecera_custom_5)
        self.frame_btns_cabecera_custom_2.setObjectName(u"frame_btns_cabecera_custom_2")
        self.frame_btns_cabecera_custom_2.setFrameShape(QFrame.StyledPanel)
        self.frame_btns_cabecera_custom_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_btns_cabecera_custom_2)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.btn_gral_3 = QPushButton(self.frame_btns_cabecera_custom_2)
        self.btn_gral_3.setObjectName(u"btn_gral_3")
        self.btn_gral_3.setFont(font2)
        self.btn_gral_3.setIcon(icon6)

        self.horizontalLayout_40.addWidget(self.btn_gral_3)

        self.btn_particular_prt_3 = QPushButton(self.frame_btns_cabecera_custom_2)
        self.btn_particular_prt_3.setObjectName(u"btn_particular_prt_3")
        self.btn_particular_prt_3.setFont(font2)
        self.btn_particular_prt_3.setIcon(icon7)

        self.horizontalLayout_40.addWidget(self.btn_particular_prt_3)


        self.verticalLayout_33.addWidget(self.frame_btns_cabecera_custom_2)


        self.verticalLayout_5.addWidget(self.cabecera_custom_5)

        self.columnas_custom_5 = QFrame(self.frame_7)
        self.columnas_custom_5.setObjectName(u"columnas_custom_5")
        sizePolicy2.setHeightForWidth(self.columnas_custom_5.sizePolicy().hasHeightForWidth())
        self.columnas_custom_5.setSizePolicy(sizePolicy2)
        self.columnas_custom_5.setMaximumSize(QSize(16777215, 1000))
        self.columnas_custom_5.setFrameShape(QFrame.StyledPanel)
        self.columnas_custom_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.columnas_custom_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.clm_ori_perso = QFrame(self.columnas_custom_5)
        self.clm_ori_perso.setObjectName(u"clm_ori_perso")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.clm_ori_perso.sizePolicy().hasHeightForWidth())
        self.clm_ori_perso.setSizePolicy(sizePolicy7)
        self.clm_ori_perso.setMaximumSize(QSize(266, 424))
        self.clm_ori_perso.setFrameShape(QFrame.StyledPanel)
        self.clm_ori_perso.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.clm_ori_perso)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.clm_ori_perso)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_11)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_ori_perso_5 = QFrame(self.frame_11)
        self.frame_ori_perso_5.setObjectName(u"frame_ori_perso_5")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_ori_perso_5.sizePolicy().hasHeightForWidth())
        self.frame_ori_perso_5.setSizePolicy(sizePolicy8)
        self.frame_ori_perso_5.setFrameShape(QFrame.StyledPanel)
        self.frame_ori_perso_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_ori_perso_5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_43 = QLabel(self.frame_ori_perso_5)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setPixmap(QPixmap(u":/iconos/Iconos/map-pin.svg"))

        self.horizontalLayout_21.addWidget(self.label_43, 0, Qt.AlignRight)

        self.label_100 = QLabel(self.frame_ori_perso_5)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setFont(font3)

        self.horizontalLayout_21.addWidget(self.label_100)

        self.label_101 = QLabel(self.frame_ori_perso_5)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setPixmap(QPixmap(u":/iconos/Iconos/map-pin.svg"))

        self.horizontalLayout_21.addWidget(self.label_101)


        self.verticalLayout_23.addWidget(self.frame_ori_perso_5)

        self.combo_origen_ext = QComboBox(self.frame_11)
        self.combo_origen_ext.addItem("")
        self.combo_origen_ext.addItem("")
        self.combo_origen_ext.setObjectName(u"combo_origen_ext")

        self.verticalLayout_23.addWidget(self.combo_origen_ext)

        self.ruta_origen_ext = QPushButton(self.frame_11)
        self.ruta_origen_ext.setObjectName(u"ruta_origen_ext")
        font7 = QFont()
        font7.setBold(True)
        self.ruta_origen_ext.setFont(font7)
        self.ruta_origen_ext.setIcon(icon9)

        self.verticalLayout_23.addWidget(self.ruta_origen_ext)


        self.verticalLayout_10.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.frame_16 = QFrame(self.clm_ori_perso)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy9)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_ori_lcl_4 = QFrame(self.frame_16)
        self.frame_ori_lcl_4.setObjectName(u"frame_ori_lcl_4")
        sizePolicy8.setHeightForWidth(self.frame_ori_lcl_4.sizePolicy().hasHeightForWidth())
        self.frame_ori_lcl_4.setSizePolicy(sizePolicy8)
        self.frame_ori_lcl_4.setFrameShape(QFrame.StyledPanel)
        self.frame_ori_lcl_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_ori_lcl_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_21 = QLabel(self.frame_ori_lcl_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setPixmap(QPixmap(u":/iconos/Iconos/server.svg"))

        self.horizontalLayout_13.addWidget(self.label_21, 0, Qt.AlignRight)

        self.label_41 = QLabel(self.frame_ori_lcl_4)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_41)

        self.label_42 = QLabel(self.frame_ori_lcl_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setPixmap(QPixmap(u":/iconos/Iconos/server.svg"))

        self.horizontalLayout_13.addWidget(self.label_42)


        self.verticalLayout_19.addWidget(self.frame_ori_lcl_4)

        self.combo_origen_loc = QComboBox(self.frame_16)
        self.combo_origen_loc.addItem("")
        self.combo_origen_loc.addItem("")
        self.combo_origen_loc.addItem("")
        self.combo_origen_loc.addItem("")
        self.combo_origen_loc.addItem("")
        self.combo_origen_loc.addItem("")
        self.combo_origen_loc.addItem("")
        self.combo_origen_loc.addItem("")
        self.combo_origen_loc.setObjectName(u"combo_origen_loc")
        sizePolicy8.setHeightForWidth(self.combo_origen_loc.sizePolicy().hasHeightForWidth())
        self.combo_origen_loc.setSizePolicy(sizePolicy8)

        self.verticalLayout_19.addWidget(self.combo_origen_loc)

        self.ruta_origen_loc = QPushButton(self.frame_16)
        self.ruta_origen_loc.setObjectName(u"ruta_origen_loc")
        self.ruta_origen_loc.setFont(font7)
        self.ruta_origen_loc.setIcon(icon9)

        self.verticalLayout_19.addWidget(self.ruta_origen_loc)


        self.verticalLayout_10.addWidget(self.frame_16, 0, Qt.AlignTop)

        self.frame_25 = QFrame(self.clm_ori_perso)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_25)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_ori_nub_4 = QFrame(self.frame_25)
        self.frame_ori_nub_4.setObjectName(u"frame_ori_nub_4")
        sizePolicy8.setHeightForWidth(self.frame_ori_nub_4.sizePolicy().hasHeightForWidth())
        self.frame_ori_nub_4.setSizePolicy(sizePolicy8)
        self.frame_ori_nub_4.setFrameShape(QFrame.StyledPanel)
        self.frame_ori_nub_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_ori_nub_4)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_44 = QLabel(self.frame_ori_nub_4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setPixmap(QPixmap(u":/iconos/Iconos/cloud.svg"))

        self.horizontalLayout_22.addWidget(self.label_44, 0, Qt.AlignRight)

        self.label_45 = QLabel(self.frame_ori_nub_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font3)

        self.horizontalLayout_22.addWidget(self.label_45, 0, Qt.AlignHCenter)

        self.label_46 = QLabel(self.frame_ori_nub_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setPixmap(QPixmap(u":/iconos/Iconos/cloud.svg"))

        self.horizontalLayout_22.addWidget(self.label_46, 0, Qt.AlignTop)


        self.verticalLayout_28.addWidget(self.frame_ori_nub_4)

        self.combo_origen_nub = QComboBox(self.frame_25)
        self.combo_origen_nub.addItem("")
        self.combo_origen_nub.addItem("")
        self.combo_origen_nub.addItem("")
        self.combo_origen_nub.setObjectName(u"combo_origen_nub")
        sizePolicy8.setHeightForWidth(self.combo_origen_nub.sizePolicy().hasHeightForWidth())
        self.combo_origen_nub.setSizePolicy(sizePolicy8)

        self.verticalLayout_28.addWidget(self.combo_origen_nub, 0, Qt.AlignTop)

        self.ruta_origen_nub = QPushButton(self.frame_25)
        self.ruta_origen_nub.setObjectName(u"ruta_origen_nub")
        self.ruta_origen_nub.setFont(font7)
        self.ruta_origen_nub.setIcon(icon9)

        self.verticalLayout_28.addWidget(self.ruta_origen_nub)


        self.verticalLayout_10.addWidget(self.frame_25, 0, Qt.AlignTop)


        self.gridLayout_4.addWidget(self.clm_ori_perso, 0, 0, 1, 1)

        self.clm_dest_perso = QFrame(self.columnas_custom_5)
        self.clm_dest_perso.setObjectName(u"clm_dest_perso")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.clm_dest_perso.sizePolicy().hasHeightForWidth())
        self.clm_dest_perso.setSizePolicy(sizePolicy10)
        self.clm_dest_perso.setMaximumSize(QSize(266, 424))
        self.clm_dest_perso.setFrameShape(QFrame.StyledPanel)
        self.clm_dest_perso.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.clm_dest_perso)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.clm_dest_perso)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_19)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_perso_dest_lcl = QFrame(self.frame_19)
        self.frame_perso_dest_lcl.setObjectName(u"frame_perso_dest_lcl")
        sizePolicy8.setHeightForWidth(self.frame_perso_dest_lcl.sizePolicy().hasHeightForWidth())
        self.frame_perso_dest_lcl.setSizePolicy(sizePolicy8)
        self.frame_perso_dest_lcl.setFrameShape(QFrame.StyledPanel)
        self.frame_perso_dest_lcl.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_perso_dest_lcl)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_23 = QLabel(self.frame_perso_dest_lcl)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setPixmap(QPixmap(u":/iconos/Iconos/server.svg"))

        self.horizontalLayout_11.addWidget(self.label_23, 0, Qt.AlignRight)

        self.label_24 = QLabel(self.frame_perso_dest_lcl)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)

        self.horizontalLayout_11.addWidget(self.label_24, 0, Qt.AlignHCenter)

        self.label_25 = QLabel(self.frame_perso_dest_lcl)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setPixmap(QPixmap(u":/iconos/Iconos/server.svg"))

        self.horizontalLayout_11.addWidget(self.label_25)


        self.verticalLayout_21.addWidget(self.frame_perso_dest_lcl)

        self.comboBox_3 = QComboBox(self.frame_19)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_21.addWidget(self.comboBox_3, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.frame_19, 0, Qt.AlignTop)

        self.frame_18 = QFrame(self.clm_dest_perso)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_18)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_perso_dest_ext = QFrame(self.frame_18)
        self.frame_perso_dest_ext.setObjectName(u"frame_perso_dest_ext")
        sizePolicy8.setHeightForWidth(self.frame_perso_dest_ext.sizePolicy().hasHeightForWidth())
        self.frame_perso_dest_ext.setSizePolicy(sizePolicy8)
        self.frame_perso_dest_ext.setFrameShape(QFrame.StyledPanel)
        self.frame_perso_dest_ext.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_perso_dest_ext)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_22 = QLabel(self.frame_perso_dest_ext)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setPixmap(QPixmap(u":/iconos/Iconos/map-pin.svg"))

        self.horizontalLayout_8.addWidget(self.label_22, 0, Qt.AlignRight)

        self.label_92 = QLabel(self.frame_perso_dest_ext)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_92, 0, Qt.AlignHCenter)

        self.label_93 = QLabel(self.frame_perso_dest_ext)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setPixmap(QPixmap(u":/iconos/Iconos/map-pin.svg"))

        self.horizontalLayout_8.addWidget(self.label_93)


        self.gridLayout_3.addWidget(self.frame_perso_dest_ext, 0, 0, 1, 1)

        self.comboBox_20 = QComboBox(self.frame_18)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")

        self.gridLayout_3.addWidget(self.comboBox_20, 1, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.frame_20 = QFrame(self.clm_dest_perso)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_20)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_perso_dest_nub = QFrame(self.frame_20)
        self.frame_perso_dest_nub.setObjectName(u"frame_perso_dest_nub")
        sizePolicy8.setHeightForWidth(self.frame_perso_dest_nub.sizePolicy().hasHeightForWidth())
        self.frame_perso_dest_nub.setSizePolicy(sizePolicy8)
        self.frame_perso_dest_nub.setFrameShape(QFrame.StyledPanel)
        self.frame_perso_dest_nub.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_perso_dest_nub)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_8 = QLabel(self.frame_perso_dest_nub)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/iconos/Iconos/cloud.svg"))

        self.horizontalLayout_12.addWidget(self.label_8, 0, Qt.AlignRight)

        self.label_26 = QLabel(self.frame_perso_dest_nub)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)

        self.horizontalLayout_12.addWidget(self.label_26, 0, Qt.AlignHCenter)

        self.label_27 = QLabel(self.frame_perso_dest_nub)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setPixmap(QPixmap(u":/iconos/Iconos/cloud.svg"))

        self.horizontalLayout_12.addWidget(self.label_27)


        self.verticalLayout_22.addWidget(self.frame_perso_dest_nub)

        self.comboBox_4 = QComboBox(self.frame_20)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy8.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy8)

        self.verticalLayout_22.addWidget(self.comboBox_4, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.frame_20)


        self.gridLayout_4.addWidget(self.clm_dest_perso, 0, 2, 1, 1)

        self.frame_btns_ejec_4 = QFrame(self.columnas_custom_5)
        self.frame_btns_ejec_4.setObjectName(u"frame_btns_ejec_4")
        self.frame_btns_ejec_4.setFrameShape(QFrame.StyledPanel)
        self.frame_btns_ejec_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_btns_ejec_4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_39 = QPushButton(self.frame_btns_ejec_4)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setFont(font2)
        self.pushButton_39.setIcon(icon8)

        self.horizontalLayout_20.addWidget(self.pushButton_39)

        self.pushButton_40 = QPushButton(self.frame_btns_ejec_4)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setFont(font2)
        self.pushButton_40.setIcon(icon9)

        self.horizontalLayout_20.addWidget(self.pushButton_40)

        self.pushButton_41 = QPushButton(self.frame_btns_ejec_4)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setFont(font2)
        self.pushButton_41.setIcon(icon10)

        self.horizontalLayout_20.addWidget(self.pushButton_41)


        self.gridLayout_4.addWidget(self.frame_btns_ejec_4, 1, 0, 1, 3, Qt.AlignTop)

        self.clm_icons = QFrame(self.columnas_custom_5)
        self.clm_icons.setObjectName(u"clm_icons")
        sizePolicy7.setHeightForWidth(self.clm_icons.sizePolicy().hasHeightForWidth())
        self.clm_icons.setSizePolicy(sizePolicy7)
        self.clm_icons.setMaximumSize(QSize(266, 424))
        self.clm_icons.setFrameShape(QFrame.StyledPanel)
        self.clm_icons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.clm_icons)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.stackedWidget_2 = QStackedWidget(self.clm_icons)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(0, 0))
        self.stackedWidget_2.setMaximumSize(QSize(1000, 500))
        self.page_2_1 = QWidget()
        self.page_2_1.setObjectName(u"page_2_1")
        self.page_2_1.setMinimumSize(QSize(0, 0))
        self.page_2_1.setMaximumSize(QSize(0, 16777215))
        self.page_2_1.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.page_2_1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.origen_externo = QFrame(self.page_2_1)
        self.origen_externo.setObjectName(u"origen_externo")
        sizePolicy4.setHeightForWidth(self.origen_externo.sizePolicy().hasHeightForWidth())
        self.origen_externo.setSizePolicy(sizePolicy4)
        self.origen_externo.setMinimumSize(QSize(80, 80))
        self.origen_externo.setMaximumSize(QSize(1000, 8000))
        self.origen_externo.setStyleSheet(u"#origen_externo{\n"
"\n"
"border: solid #8f8f91;\n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    min-width: 80px;\n"
"}")
        self.origen_externo.setFrameShape(QFrame.StyledPanel)
        self.origen_externo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.origen_externo)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_49 = QFrame(self.origen_externo)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_49)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_50)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_67 = QLabel(self.frame_50)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"")
        self.label_67.setPixmap(QPixmap(u":/iconos/Iconos/arrow-down-right.svg"))

        self.verticalLayout_45.addWidget(self.label_67, 0, Qt.AlignLeft)


        self.gridLayout_15.addWidget(self.frame_50, 0, 0, 1, 1)

        self.frame_51 = QFrame(self.frame_49)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_51)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_30 = QLabel(self.frame_51)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setPixmap(QPixmap(u":/iconos/Iconos/arrow-up-right.svg"))

        self.verticalLayout_46.addWidget(self.label_30, 0, Qt.AlignRight)


        self.gridLayout_15.addWidget(self.frame_51, 0, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_49)

        self.label_31 = QLabel(self.origen_externo)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_14.addWidget(self.label_31)

        self.label_68 = QLabel(self.origen_externo)
        self.label_68.setObjectName(u"label_68")

        self.verticalLayout_14.addWidget(self.label_68)

        self.frame_52 = QFrame(self.origen_externo)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_52)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_47 = QLabel(self.frame_52)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setPixmap(QPixmap(u":/iconos/Iconos/mail.svg"))

        self.gridLayout_16.addWidget(self.label_47, 0, 1, 1, 1, Qt.AlignHCenter)

        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_53)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_32 = QLabel(self.frame_53)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setPixmap(QPixmap(u":/iconos/Iconos/arrow-right.svg"))

        self.verticalLayout_47.addWidget(self.label_32, 0, Qt.AlignRight)


        self.gridLayout_16.addWidget(self.frame_53, 0, 2, 1, 1)

        self.frame_54 = QFrame(self.frame_52)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_54)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_48 = QLabel(self.frame_54)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_48.addWidget(self.label_48)


        self.gridLayout_16.addWidget(self.frame_54, 0, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_52)

        self.label_69 = QLabel(self.origen_externo)
        self.label_69.setObjectName(u"label_69")

        self.verticalLayout_14.addWidget(self.label_69)

        self.label_36 = QLabel(self.origen_externo)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_14.addWidget(self.label_36)

        self.frame_55 = QFrame(self.origen_externo)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_55)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_56)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_70 = QLabel(self.frame_56)
        self.label_70.setObjectName(u"label_70")

        self.verticalLayout_49.addWidget(self.label_70)


        self.gridLayout_17.addWidget(self.frame_56, 0, 0, 1, 1)

        self.frame_57 = QFrame(self.frame_55)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_57)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_71 = QLabel(self.frame_57)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setPixmap(QPixmap(u":/iconos/Iconos/arrow-down-right.svg"))

        self.verticalLayout_50.addWidget(self.label_71, 0, Qt.AlignRight)


        self.gridLayout_17.addWidget(self.frame_57, 0, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_55)

        self.label_72 = QLabel(self.origen_externo)
        self.label_72.setObjectName(u"label_72")

        self.verticalLayout_14.addWidget(self.label_72)


        self.verticalLayout_15.addWidget(self.origen_externo)

        self.stackedWidget_2.addWidget(self.page_2_1)
        self.page_2_3 = QWidget()
        self.page_2_3.setObjectName(u"page_2_3")
        self.page_2_3.setMaximumSize(QSize(0, 16777215))
        self.page_2_3.setStyleSheet(u"background-image: url(:/imagenes/imgQuienes1.png);")
        self.verticalLayout_13 = QVBoxLayout(self.page_2_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.origen_local = QFrame(self.page_2_3)
        self.origen_local.setObjectName(u"origen_local")
        sizePolicy4.setHeightForWidth(self.origen_local.sizePolicy().hasHeightForWidth())
        self.origen_local.setSizePolicy(sizePolicy4)
        self.origen_local.setMinimumSize(QSize(80, 0))
        self.origen_local.setMaximumSize(QSize(16777215, 16777215))
        self.origen_local.setStyleSheet(u"#origen_local{\n"
"\n"
"border: solid #8f8f91;\n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    min-width: 80px;\n"
"}")
        self.origen_local.setFrameShape(QFrame.StyledPanel)
        self.origen_local.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.origen_local)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_39 = QFrame(self.origen_local)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMaximumSize(QSize(16777215, 64))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_39)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_40)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_58 = QLabel(self.frame_40)
        self.label_58.setObjectName(u"label_58")

        self.verticalLayout_38.addWidget(self.label_58, 0, Qt.AlignLeft)


        self.gridLayout_12.addWidget(self.frame_40, 0, 0, 1, 1)

        self.frame_41 = QFrame(self.frame_39)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_41)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_20 = QLabel(self.frame_41)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setPixmap(QPixmap(u":/iconos/Iconos/arrow-up-right.svg"))

        self.verticalLayout_39.addWidget(self.label_20, 0, Qt.AlignRight)


        self.gridLayout_12.addWidget(self.frame_41, 0, 1, 1, 1)


        self.verticalLayout_37.addWidget(self.frame_39)

        self.label_28 = QLabel(self.origen_local)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_37.addWidget(self.label_28)

        self.label_59 = QLabel(self.origen_local)
        self.label_59.setObjectName(u"label_59")

        self.verticalLayout_37.addWidget(self.label_59)

        self.frame_42 = QFrame(self.origen_local)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_42)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_60 = QLabel(self.frame_42)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setPixmap(QPixmap(u":/iconos/Iconos/mail.svg"))

        self.gridLayout_13.addWidget(self.label_60, 0, 1, 1, 1, Qt.AlignHCenter)

        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_43)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_29 = QLabel(self.frame_43)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setPixmap(QPixmap(u":/iconos/Iconos/arrow-right.svg"))

        self.verticalLayout_40.addWidget(self.label_29, 0, Qt.AlignRight)


        self.gridLayout_13.addWidget(self.frame_43, 0, 2, 1, 1)

        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_44)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_61 = QLabel(self.frame_44)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setPixmap(QPixmap(u":/iconos/Iconos/arrow-right.svg"))

        self.verticalLayout_41.addWidget(self.label_61)


        self.gridLayout_13.addWidget(self.frame_44, 0, 0, 1, 1)


        self.verticalLayout_37.addWidget(self.frame_42)

        self.label_62 = QLabel(self.origen_local)
        self.label_62.setObjectName(u"label_62")

        self.verticalLayout_37.addWidget(self.label_62)

        self.label_63 = QLabel(self.origen_local)
        self.label_63.setObjectName(u"label_63")

        self.verticalLayout_37.addWidget(self.label_63)

        self.frame_45 = QFrame(self.origen_local)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_45)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_46)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_64 = QLabel(self.frame_46)
        self.label_64.setObjectName(u"label_64")

        self.verticalLayout_42.addWidget(self.label_64)


        self.gridLayout_14.addWidget(self.frame_46, 0, 0, 1, 1)

        self.frame_47 = QFrame(self.frame_45)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_47)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_65 = QLabel(self.frame_47)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setPixmap(QPixmap(u":/iconos/Iconos/arrow-down-right.svg"))

        self.verticalLayout_43.addWidget(self.label_65, 0, Qt.AlignRight)


        self.gridLayout_14.addWidget(self.frame_47, 0, 1, 1, 1)


        self.verticalLayout_37.addWidget(self.frame_45)

        self.label_66 = QLabel(self.origen_local)
        self.label_66.setObjectName(u"label_66")

        self.verticalLayout_37.addWidget(self.label_66)


        self.verticalLayout_13.addWidget(self.origen_local)

        self.stackedWidget_2.addWidget(self.page_2_3)
        self.page_2_2 = QWidget()
        self.page_2_2.setObjectName(u"page_2_2")
        self.page_2_2.setMaximumSize(QSize(0, 16777215))
        self.horizontalLayout_9 = QHBoxLayout(self.page_2_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.origen_nube = QFrame(self.page_2_2)
        self.origen_nube.setObjectName(u"origen_nube")
        sizePolicy4.setHeightForWidth(self.origen_nube.sizePolicy().hasHeightForWidth())
        self.origen_nube.setSizePolicy(sizePolicy4)
        self.origen_nube.setStyleSheet(u"#origen_nube{\n"
"\n"
"border: solid #8f8f91;\n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #fcc253 stop: 1 #ddebdd);\n"
"    min-width: 80px;\n"
"}")
        self.origen_nube.setFrameShape(QFrame.StyledPanel)
        self.origen_nube.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.origen_nube)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_29 = QFrame(self.origen_nube)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_29)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_30)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_52 = QLabel(self.frame_30)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_27.addWidget(self.label_52, 0, Qt.AlignLeft)


        self.gridLayout_9.addWidget(self.frame_30, 0, 0, 1, 1)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_31)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_17 = QLabel(self.frame_31)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setPixmap(QPixmap(u":/iconos/Iconos/arrow-up-right.svg"))

        self.verticalLayout_30.addWidget(self.label_17, 0, Qt.AlignRight)


        self.gridLayout_9.addWidget(self.frame_31, 0, 1, 1, 1)


        self.verticalLayout_26.addWidget(self.frame_29)

        self.label_18 = QLabel(self.origen_nube)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_26.addWidget(self.label_18)

        self.label_53 = QLabel(self.origen_nube)
        self.label_53.setObjectName(u"label_53")

        self.verticalLayout_26.addWidget(self.label_53)

        self.frame_32 = QFrame(self.origen_nube)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_32)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_39 = QLabel(self.frame_32)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setPixmap(QPixmap(u":/iconos/Iconos/mail.svg"))

        self.gridLayout_10.addWidget(self.label_39, 0, 1, 1, 1, Qt.AlignHCenter)

        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_33)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_19 = QLabel(self.frame_33)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setPixmap(QPixmap(u":/iconos/Iconos/arrow-right.svg"))

        self.verticalLayout_32.addWidget(self.label_19, 0, Qt.AlignRight)


        self.gridLayout_10.addWidget(self.frame_33, 0, 2, 1, 1)

        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_34)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_40 = QLabel(self.frame_34)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_34.addWidget(self.label_40)


        self.gridLayout_10.addWidget(self.frame_34, 0, 0, 1, 1)


        self.verticalLayout_26.addWidget(self.frame_32)

        self.label_54 = QLabel(self.origen_nube)
        self.label_54.setObjectName(u"label_54")

        self.verticalLayout_26.addWidget(self.label_54)

        self.label_35 = QLabel(self.origen_nube)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_26.addWidget(self.label_35)

        self.frame_35 = QFrame(self.origen_nube)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_35)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_36)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_55 = QLabel(self.frame_36)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setPixmap(QPixmap(u":/iconos/Iconos/arrow-up-right.svg"))

        self.verticalLayout_35.addWidget(self.label_55)


        self.gridLayout_11.addWidget(self.frame_36, 0, 0, 1, 1)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_37)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_56 = QLabel(self.frame_37)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setPixmap(QPixmap(u":/iconos/Iconos/arrow-down-right.svg"))

        self.verticalLayout_36.addWidget(self.label_56, 0, Qt.AlignRight)


        self.gridLayout_11.addWidget(self.frame_37, 0, 1, 1, 1)


        self.verticalLayout_26.addWidget(self.frame_35)

        self.label_57 = QLabel(self.origen_nube)
        self.label_57.setObjectName(u"label_57")

        self.verticalLayout_26.addWidget(self.label_57)


        self.horizontalLayout_9.addWidget(self.origen_nube)

        self.stackedWidget_2.addWidget(self.page_2_2)

        self.verticalLayout_11.addWidget(self.stackedWidget_2)


        self.gridLayout_4.addWidget(self.clm_icons, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.columnas_custom_5)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.pagina2)
        self.pagina3 = QWidget()
        self.pagina3.setObjectName(u"pagina3")
        self.verticalLayout_7 = QVBoxLayout(self.pagina3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_8 = QFrame(self.pagina3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.pagina3)

        self.gridLayout_8.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boton_menu.setText("")
        self.boton1.setText(QCoreApplication.translate("MainWindow", u"Prueba Diaria", None))
        self.boton2.setText(QCoreApplication.translate("MainWindow", u"Actividad Hosts", None))
        self.boton3.setText(QCoreApplication.translate("MainWindow", u"Disponibilidad", None))
        self.boton4.setText(QCoreApplication.translate("MainWindow", u"Estadisticas Test", None))
        self.boton5.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.btn_gral_2.setText(QCoreApplication.translate("MainWindow", u"Prueba General", None))
        self.btn_particular_prt_2.setText(QCoreApplication.translate("MainWindow", u"Prueba Personalizada", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Informacion", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_82.setText("")
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Destinos Locales", None))
        self.label_84.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"TestLocalPromi", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TestLocalEMV", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TestLocalBRT", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TestLocalBRA", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TestLocalBRH", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TestLocalMTV", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TestLocalBRF", None))
        self.label_10.setText("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label_80.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"dcmonitoreo7x24", None))
        self.label_86.setText("")
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Destinos Nube", None))
        self.label_88.setText("")
        self.label_16.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Test365Promi", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Test365EMV", None))
        self.label_13.setText("")
        self.btn_gral_3.setText(QCoreApplication.translate("MainWindow", u"Prueba General", None))
        self.btn_particular_prt_3.setText(QCoreApplication.translate("MainWindow", u"Prueba Personalizada", None))
        self.label_43.setText("")
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Origen Externo", None))
        self.label_101.setText("")
        self.combo_origen_ext.setItemText(0, "")
        self.combo_origen_ext.setItemText(1, QCoreApplication.translate("MainWindow", u"dcmonitoreo7x24@gmail.com", None))

        self.ruta_origen_ext.setText(QCoreApplication.translate("MainWindow", u"Ruta de Envio", None))
        self.label_21.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Origen Local", None))
        self.label_42.setText("")
        self.combo_origen_loc.setItemText(0, "")
        self.combo_origen_loc.setItemText(1, QCoreApplication.translate("MainWindow", u"TestLocalPromi", None))
        self.combo_origen_loc.setItemText(2, QCoreApplication.translate("MainWindow", u"TestLocalEMV", None))
        self.combo_origen_loc.setItemText(3, QCoreApplication.translate("MainWindow", u"TestLocalBRT", None))
        self.combo_origen_loc.setItemText(4, QCoreApplication.translate("MainWindow", u"TestLocalBRA", None))
        self.combo_origen_loc.setItemText(5, QCoreApplication.translate("MainWindow", u"TestLocalBRH", None))
        self.combo_origen_loc.setItemText(6, QCoreApplication.translate("MainWindow", u"TestLocalMTV", None))
        self.combo_origen_loc.setItemText(7, QCoreApplication.translate("MainWindow", u"TestLocalBRF", None))

        self.ruta_origen_loc.setText(QCoreApplication.translate("MainWindow", u"Ruta de Envio", None))
        self.label_44.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Origen Nube", None))
        self.label_46.setText("")
        self.combo_origen_nub.setItemText(0, "")
        self.combo_origen_nub.setItemText(1, QCoreApplication.translate("MainWindow", u"Test365Promi", None))
        self.combo_origen_nub.setItemText(2, QCoreApplication.translate("MainWindow", u"Test365EMV", None))

        self.ruta_origen_nub.setText(QCoreApplication.translate("MainWindow", u"Ruta de Envio", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Destino Local", None))
        self.label_25.setText("")
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"TestLocalEMV", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"TestLocalPromi", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"TestLocalBRT", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"TestLocalBRA", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"TestLocalBRH", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"TestLocalMTV", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"TestLocalBRF", None))

        self.label_22.setText("")
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Destino Externo", None))
        self.label_93.setText("")
        self.comboBox_20.setItemText(0, "")
        self.comboBox_20.setItemText(1, QCoreApplication.translate("MainWindow", u"dcmonitoreo7x24@gmail.com", None))

        self.label_8.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Destino Nube", None))
        self.label_27.setText("")
        self.comboBox_4.setItemText(0, "")
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Test365EMV", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Test365Promi", None))

        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"Informacion General", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_67.setText("")
        self.label_30.setText("")
        self.label_31.setText("")
        self.label_68.setText("")
        self.label_47.setText("")
        self.label_32.setText("")
        self.label_48.setText("")
        self.label_69.setText("")
        self.label_36.setText("")
        self.label_70.setText("")
        self.label_71.setText("")
        self.label_72.setText("")
        self.label_58.setText("")
        self.label_20.setText("")
        self.label_28.setText("")
        self.label_59.setText("")
        self.label_60.setText("")
        self.label_29.setText("")
        self.label_61.setText("")
        self.label_62.setText("")
        self.label_63.setText("")
        self.label_64.setText("")
        self.label_65.setText("")
        self.label_66.setText("")
        self.label_52.setText("")
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_53.setText("")
        self.label_39.setText("")
        self.label_19.setText("")
        self.label_40.setText("")
        self.label_54.setText("")
        self.label_35.setText("")
        self.label_55.setText("")
        self.label_56.setText("")
        self.label_57.setText("")
    # retranslateUi


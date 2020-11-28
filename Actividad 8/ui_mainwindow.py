# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 705)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayout_2 = QFormLayout(self.tab)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.ID_lineEdit = QLineEdit(self.groupBox)
        self.ID_lineEdit.setObjectName(u"ID_lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ID_lineEdit)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.OrigenX_spinBox = QSpinBox(self.groupBox)
        self.OrigenX_spinBox.setObjectName(u"OrigenX_spinBox")
        self.OrigenX_spinBox.setMaximum(500)
        self.OrigenX_spinBox.setSingleStep(1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.OrigenX_spinBox)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.OrigenY_spinBox = QSpinBox(self.groupBox)
        self.OrigenY_spinBox.setObjectName(u"OrigenY_spinBox")
        self.OrigenY_spinBox.setMaximum(500)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.OrigenY_spinBox)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.DestinoX_spinBox = QSpinBox(self.groupBox)
        self.DestinoX_spinBox.setObjectName(u"DestinoX_spinBox")
        self.DestinoX_spinBox.setMaximum(500)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.DestinoX_spinBox)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.DestinoY_spinBox = QSpinBox(self.groupBox)
        self.DestinoY_spinBox.setObjectName(u"DestinoY_spinBox")
        self.DestinoY_spinBox.setMaximum(500)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.DestinoY_spinBox)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.Velocidad_lineEdit = QLineEdit(self.groupBox)
        self.Velocidad_lineEdit.setObjectName(u"Velocidad_lineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.Velocidad_lineEdit)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setTextFormat(Qt.AutoText)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.Red_spinBox = QSpinBox(self.groupBox)
        self.Red_spinBox.setObjectName(u"Red_spinBox")
        self.Red_spinBox.setMaximum(255)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.Red_spinBox)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.Green_spinBox = QSpinBox(self.groupBox)
        self.Green_spinBox.setObjectName(u"Green_spinBox")
        self.Green_spinBox.setMaximum(255)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.Green_spinBox)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_10)

        self.Blue_spinBox = QSpinBox(self.groupBox)
        self.Blue_spinBox.setObjectName(u"Blue_spinBox")
        self.Blue_spinBox.setMaximum(255)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.Blue_spinBox)

        self.Agregar_Inicio_pushButton = QPushButton(self.groupBox)
        self.Agregar_Inicio_pushButton.setObjectName(u"Agregar_Inicio_pushButton")

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.Agregar_Inicio_pushButton)

        self.Agregar_Final_pushButton = QPushButton(self.groupBox)
        self.Agregar_Final_pushButton.setObjectName(u"Agregar_Final_pushButton")

        self.formLayout.setWidget(11, QFormLayout.SpanningRole, self.Agregar_Final_pushButton)

        self.Mostar_pushButton = QPushButton(self.groupBox)
        self.Mostar_pushButton.setObjectName(u"Mostar_pushButton")

        self.formLayout.setWidget(12, QFormLayout.SpanningRole, self.Mostar_pushButton)

        self.Ordenar_ID_pushButton = QPushButton(self.groupBox)
        self.Ordenar_ID_pushButton.setObjectName(u"Ordenar_ID_pushButton")

        self.formLayout.setWidget(13, QFormLayout.SpanningRole, self.Ordenar_ID_pushButton)

        self.Ordenar_Distancia_pushButton = QPushButton(self.groupBox)
        self.Ordenar_Distancia_pushButton.setObjectName(u"Ordenar_Distancia_pushButton")

        self.formLayout.setWidget(14, QFormLayout.SpanningRole, self.Ordenar_Distancia_pushButton)

        self.Ordenar_Velocidad_pushButton = QPushButton(self.groupBox)
        self.Ordenar_Velocidad_pushButton.setObjectName(u"Ordenar_Velocidad_pushButton")

        self.formLayout.setWidget(15, QFormLayout.SpanningRole, self.Ordenar_Velocidad_pushButton)

        self.Mostrar_Grafo = QPushButton(self.groupBox)
        self.Mostrar_Grafo.setObjectName(u"Mostrar_Grafo")

        self.formLayout.setWidget(16, QFormLayout.SpanningRole, self.Mostrar_Grafo)


        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.groupBox)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.salida)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ordenarVelocidadT_pushButton = QPushButton(self.tab_2)
        self.ordenarVelocidadT_pushButton.setObjectName(u"ordenarVelocidadT_pushButton")

        self.gridLayout_4.addWidget(self.ordenarVelocidadT_pushButton, 2, 2, 1, 1)

        self.ordenarDistanciaT_pushButton = QPushButton(self.tab_2)
        self.ordenarDistanciaT_pushButton.setObjectName(u"ordenarDistanciaT_pushButton")

        self.gridLayout_4.addWidget(self.ordenarDistanciaT_pushButton, 2, 1, 1, 1)

        self.table = QTableWidget(self.tab_2)
        self.table.setObjectName(u"table")

        self.gridLayout_4.addWidget(self.table, 0, 0, 1, 3)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.ordenarIDT_pushButton = QPushButton(self.tab_2)
        self.ordenarIDT_pushButton.setObjectName(u"ordenarIDT_pushButton")

        self.gridLayout_4.addWidget(self.ordenarIDT_pushButton, 2, 0, 1, 1)

        self.mostar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostar_tabla_pushButton.setObjectName(u"mostar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.mostar_tabla_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.Dibujar = QPushButton(self.tab_3)
        self.Dibujar.setObjectName(u"Dibujar")

        self.gridLayout_5.addWidget(self.Dibujar, 1, 0, 1, 1)

        self.limpiar = QPushButton(self.tab_3)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_5.addWidget(self.limpiar, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 550, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mostrar Grafo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino x:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino y:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color (rgb)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue: ", None))
        self.Agregar_Inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.Agregar_Final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.Mostar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Ordenar_ID_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por ID", None))
        self.Ordenar_Distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Distancia", None))
        self.Ordenar_Velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Velocidad", None))
        self.Mostrar_Grafo.setText(QCoreApplication.translate("MainWindow", u"Mostrar Grafo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.ordenarVelocidadT_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Velocidad", None))
        self.ordenarDistanciaT_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Distancia", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.ordenarIDT_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por ID", None))
        self.mostar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.Dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"P\u00e1gina", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi


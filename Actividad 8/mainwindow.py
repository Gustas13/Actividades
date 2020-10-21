from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from administradorP import AdministradorP
from particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.administradorP = AdministradorP()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Agregar_Inicio_pushButton.clicked.connect(self.click_agregar)
        self.ui.Agregar_Final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.Mostar_pushButton.clicked.connect(self.click_mostrar)
    @Slot()
    def click_mostrar(self):
        #self.administradorP.mostrar()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.administradorP))

    def click_agregar(self):
        id = self.ui.ID_lineEdit.text()
        origen_x = self.ui.OrigenX_spinBox.value()
        origen_y = self.ui.OrigenY_spinBox.value()
        destino_x = self.ui.DestinoX_spinBox.value()
        destino_y = self.ui.DestinoY_spinBox.value()
        velocidad = self.ui.Velocidad_lineEdit.text()
        red = self.ui.Red_spinBox.value()
        green = self.ui.Green_spinBox.value()
        blue = self.ui.Blue_spinBox.value()

        particula = Particula (id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.administradorP.agregar_inicio(particula)
        #print(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        #self.ui.salida.insertPlainText(id + str(origen_x) + str(origen_y) + str(destino_x) + str(destino_y) + velocidad + str(red) + str(green) + str(blue))
    
    def click_agregar_final(self):
        id = self.ui.ID_lineEdit.text()
        origen_x = self.ui.OrigenX_spinBox.value()
        origen_y = self.ui.OrigenY_spinBox.value()
        destino_x = self.ui.DestinoX_spinBox.value()
        destino_y = self.ui.DestinoY_spinBox.value()
        velocidad = self.ui.Velocidad_lineEdit.text()
        red = self.ui.Red_spinBox.value()
        green = self.ui.Green_spinBox.value()
        blue = self.ui.Blue_spinBox.value()

        particula = Particula (id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.administradorP.agregar_final(particula)
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
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

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
    
    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.administradorP.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrio el archivo: " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Errro al abrir el archivo: " + ubicacion
            )
        #print('abiri_archivo')
    
    def action_guardar_archivo(self):
        #print('guardar_archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.administradorP.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo: " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo"+ ubicacion
            )
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
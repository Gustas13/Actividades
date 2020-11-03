from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
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

        self.ui.mostar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)
    
    @Slot()

    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.administradorP:
            if id == particula.id:
                self.ui.table.clear()
                self.ui.table.setColumnCount(10)
                headers = ["ID","Origen X", "Origen Y", "Destino X", "Destino Y", "Distancia","Red","Green","Blue","Velocidad"]
                self.ui.table.setHorizontalHeaderLabels(headers)
                self.ui.table.setRowCount(1)
                id_widget = QTableWidgetItem (str(particula.id))
                origenx_widget = QTableWidgetItem (str(particula.origen_x))
                origeny_widget = QTableWidgetItem (str(particula.origen_y))
                destinox_widget = QTableWidgetItem (str(particula.destino_x))
                destinoy_widget = QTableWidgetItem (str(particula.destino_y))
                velocidad_widget = QTableWidgetItem (str(particula.velocidad))
                red_widget = QTableWidgetItem (str(particula.red))
                green_widget = QTableWidgetItem (str(particula.green))
                blue_widget = QTableWidgetItem (str(particula.blue))
                distancia_widget = QTableWidgetItem (str(particula.distancia))

                self.ui.table.setItem(0, 0, id_widget)
                self.ui.table.setItem(0, 1, origenx_widget)
                self.ui.table.setItem(0, 2, origeny_widget)
                self.ui.table.setItem(0, 3, destinox_widget)
                self.ui.table.setItem(0, 4, destinoy_widget)
                self.ui.table.setItem(0, 5, velocidad_widget)
                self.ui.table.setItem(0, 6, red_widget)
                self.ui.table.setItem(0, 7, green_widget)
                self.ui.table.setItem(0, 8, blue_widget)
                self.ui.table.setItem(0, 9, distancia_widget)
                encontrado = True
                return
                
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'La partícula con el ID "{id}" no fue encontrado'
            )

    def mostrar_tabla(self):
        self.ui.table.setColumnCount(10)
        headers = ["ID","Origen X", "Origen Y", "Destino X", "Destino Y", "Distancia","Red","Green","Blue","Velocidad"]
        self.ui.table.setHorizontalHeaderLabels(headers)

        self.ui.table.setRowCount(len(self.administradorP))
        row = 0
        for particula in self.administradorP:
            id_widget = QTableWidgetItem (str(particula.id))
            origenx_widget = QTableWidgetItem (str(particula.origen_x))
            origeny_widget = QTableWidgetItem (str(particula.origen_y))
            destinox_widget = QTableWidgetItem (str(particula.destino_x))
            destinoy_widget = QTableWidgetItem (str(particula.destino_y))
            velocidad_widget = QTableWidgetItem (str(particula.velocidad))
            red_widget = QTableWidgetItem (str(particula.red))
            green_widget = QTableWidgetItem (str(particula.green))
            blue_widget = QTableWidgetItem (str(particula.blue))
            distancia_widget = QTableWidgetItem (str(particula.distancia))

            self.ui.table.setItem(row, 0, id_widget)
            self.ui.table.setItem(row, 1, origenx_widget)
            self.ui.table.setItem(row, 2, origeny_widget)
            self.ui.table.setItem(row, 3, destinox_widget)
            self.ui.table.setItem(row, 4, destinoy_widget)
            self.ui.table.setItem(row, 5, velocidad_widget)
            self.ui.table.setItem(row, 6, red_widget)
            self.ui.table.setItem(row, 7, green_widget)
            self.ui.table.setItem(row, 8, blue_widget)
            self.ui.table.setItem(row, 9, distancia_widget)

            row +=1 

            #print('mostar_tabla')

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
                "Error al abrir el archivo: " + ubicacion
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
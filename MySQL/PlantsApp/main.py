import sys
import qtpy
from PyQt5 import QtWidgets, QtCore, QtGui
from PlantApp_ui.mainwindow import Ui_MainWindow
from DB_Interface import DB_Interface

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.DB = DB_Interface()
        self.plant_types = []
        self.chosen_plants = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('My Plants')

        self.ui.comboBox_plantTypes.addItems(self.get_plant_types())
        self.ui.comboBox_plants.addItems(self.get_plants())

        self.ui.comboBox_plantTypes.currentIndexChanged.connect(self.update_plants)
        self.ui.comboBox_plants.currentIndexChanged.connect(self.update_neighbours)

    def get_plant_types(self):
        self.DB.check_databases()
        self.plant_types = self.DB.get_plant_types()
        return [entry[0] for entry in self.plant_types]

    def get_plants(self):
        pt_id = self.ui.comboBox_plantTypes.currentIndex() + 1    # because the database IDs start at 1
        #print(pt_id)
        self.chosen_plants = self.DB.get_plants(pt_id)
        return [entry[0] for entry in self.chosen_plants]

    def update_plants(self):
        self.ui.comboBox_plants.clear()
        self.ui.comboBox_plants.addItems(self.get_plants())
        return

    def update_neighbours(self):
        plant_name = self.ui.comboBox_plants.currentText()
        print('plant ', plant_name)
        nb = self.DB.get_neighbours(plant_name)
        print(nb)
        if nb:
            self.ui.textBrowser_neighbours.setText(nb[0][0])
        return



window = MainWindow()
window.show()

sys.exit(app.exec_())

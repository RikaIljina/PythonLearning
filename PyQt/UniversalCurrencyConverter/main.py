import sys
from converter_ui.mainwindow import Ui_MainWindow
from qtpy import QtWidgets, QtGui, QtCore
from universal_crawler import Crawler

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.my_crawler = Crawler()

        self.my_crawler.get_daily()

        self.ui.doubleSpinBox_eur.setValue(1)

        self.ui.comboBox_options.setMaxVisibleItems(20)
        self.ui.comboBox_options.addItems(self.get_option_list())

        self.ui.label_chosen_currency.setText('[choose a currency]')

        self.ui.comboBox_options.currentIndexChanged.connect(self.update_label)
        self.ui.pushButton.clicked.connect(self.crawl_rate)

    def get_option_list(self):
        return ['----------------'] + [str(el) for el in self.my_crawler.get_daily()]   #  + ' -- ' + el[1]) for el in self.my_crawler.get_options()]

    def update_label(self):
        idx = self.ui.comboBox_options.currentIndex()
        self.ui.label_chosen_currency.setText(str(self.my_crawler.return_options()[idx-1]))

    def crawl_rate(self):
        idx = self.ui.comboBox_options.currentIndex()
        self.my_crawler.crawl_rates(idx-1)
        self.my_crawler.get_last_rate()
        rate, date = self.my_crawler.return_info()
        self.ui.doubleSpinBox_currency.setValue(float(rate))
        self.ui.label_info.setText(date)


window = MainWindow()
window.show()


sys.exit(app.exec_())


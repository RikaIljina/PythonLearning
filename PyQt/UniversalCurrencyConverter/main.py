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
        self.default_label = '[choose a currency]'
        self.current_value = float()

        self.ui.doubleSpinBox_eur.setValue(1)
        self.ui.doubleSpinBox_currency.setValue(0)

        self.ui.comboBox_options.setMaxVisibleItems(20)
        self.ui.comboBox_options.addItem('------------------')

        self.ui.label_chosen_currency.setText(self.default_label)

        self.ui.comboBox_options.currentIndexChanged.connect(self.update_currency_infos)
        self.ui.pushButton.clicked.connect(self.crawl_rates)

        self.ui.doubleSpinBox_eur.valueChanged.connect(self.calc_currency)
        self.ui.doubleSpinBox_currency.valueChanged.connect(self.calc_eur)

    def get_option_list(self):
        return [str(el) for el in self.my_crawler.return_options()]

    def update_currency_infos(self):
        idx = self.ui.comboBox_options.currentIndex()
        # ignore first entry (division line)
        if idx != 0:
            chosen_currency = str(self.ui.comboBox_options.currentText())
            self.current_value = float(self.my_crawler.return_rates(idx-1))
        else:
            chosen_currency = self.default_label
            self.current_value = 0

        self.ui.label_chosen_currency.setText(chosen_currency)

        if self.ui.doubleSpinBox_eur.value() > 1 or self.ui.doubleSpinBox_eur.value() < 1:
            self.calc_currency()
        else:
            self.ui.doubleSpinBox_currency.setValue(self.current_value)


    def crawl_rates(self):
        # fill dropdown with currencies
        # clear it if rates have already been crawled
        ct = self.ui.comboBox_options.count()
        if ct > 1:
            self.ui.comboBox_options.clear()
            self.ui.comboBox_options.addItem('------------------')
        self.ui.comboBox_options.addItems(self.get_option_list())

        date = self.my_crawler.last_date
        self.ui.label_info.setText(date)

    def calc_currency(self):
        eur_rate = self.ui.doubleSpinBox_eur.value()
        self.ui.doubleSpinBox_currency.setValue(eur_rate * self.current_value)

    def calc_eur(self):
        currency_rate = self.ui.doubleSpinBox_currency.value()
        if self.current_value != 0:
            self.ui.doubleSpinBox_eur.setValue(currency_rate / self.current_value)


window = MainWindow()
window.show()


sys.exit(app.exec_())


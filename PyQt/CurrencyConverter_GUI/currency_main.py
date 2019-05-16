import sys
from qtpy import QtWidgets
import currency_crawl

from currency_ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)


def get_data(file_path):

    with open(file_path, 'r', encoding='utf-8', newline='') as f:
        lines = 0
        while f.readline():
            lines += 1
        f.seek(0)
        for i in range(lines - 1):
            next(f)
        old_line = f.readline()
        try:
            sek_rate = old_line.split(';')[1]
            usd_rate = old_line.split(';')[2]
            assert type(float(sek_rate)) == float
            assert type(float(usd_rate)) == float
            return round(float(sek_rate), 3), round(float(usd_rate), 3)
        except:
            window.ui.label_progress.show()
            window.ui.label_progress.setText("Unable to parse file: <br>\"EUR to SEK\" rate must be in column 2,"
                                             "<br>\"EUR to USD\" rate must be in column 3, <br>last line will be read")
            return 0, 0


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sek_rate, self.usd_rate = 0, 0

        self.change_labels()

        self.ui.doubleSpinBox_currency_1.setDecimals(3)
        self.ui.doubleSpinBox_currency_2.setDecimals(3)

        self.ui.label_progress.setTextFormat(1)
        self.ui.label_progress.setText("<html><head/><body><p><span style=\"color:#ff0004;\">"
                                       "No values entered</span></p></body></html>")

        self.ui.comboBox_currency_choice.currentTextChanged.connect(self.change_labels)
        self.ui.doubleSpinBox_currency_1.valueChanged.connect(self.calc_currency)
        self.ui.doubleSpinBox_currency_2.valueChanged.connect(self.calc_eur)

        self.ui.pushButton_browse.clicked.connect(self.browse)
        self.ui.pushButton_crawl.clicked.connect(self.crawl)

    def browse(self):
        file_path = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open File', ".", "*.csv")
        print(file_path)
        if len(file_path[0]) != 0:
            self.sek_rate, self.usd_rate = get_data(file_path[0][0])
            self.change_labels()
            if self.sek_rate != 0 or self.usd_rate != 0:
                self.ui.label_progress.setText("")

    def crawl(self):
        self.ui.label_progress.setText("<html><head/><body><p><span style=\"color:#ff0004;\">"
                                       "Crawling...</span></p></body></html>")

        #app.processEvents()
        self.repaint()                     # This (or previous statement) redraws the GUI before getting the next value

        path = currency_crawl.update_csv()
        self.ui.label_progress.setText("")

        self.sek_rate, self.usd_rate = get_data(path)
        self.change_labels()

    def change_labels(self):
        if self.ui.comboBox_currency_choice.currentIndex() == 0:
            self.ui.label_currency_1.setText("EUR")
            self.ui.label_currency_2.setText("SEK")
            self.ui.doubleSpinBox_currency_2.setValue(self.sek_rate)
            self.ui.doubleSpinBox_currency_1.setValue(1)
        elif self.ui.comboBox_currency_choice.currentIndex() == 1:
            self.ui.label_currency_1.setText("EUR")
            self.ui.label_currency_2.setText("USD")
            self.ui.doubleSpinBox_currency_2.setValue(self.usd_rate)
            self.ui.doubleSpinBox_currency_1.setValue(1)

    def calc_currency(self):
        if self.sek_rate != 0 and self.usd_rate != 0:
            if self.ui.comboBox_currency_choice.currentIndex() == 0:
                self.ui.doubleSpinBox_currency_2.setValue(self.ui.doubleSpinBox_currency_1.value() * self.sek_rate)
            else:
                self.ui.doubleSpinBox_currency_2.setValue(self.ui.doubleSpinBox_currency_1.value() * self.usd_rate)

    def calc_eur(self):
        if self.sek_rate != 0 and self.usd_rate != 0:
            if self.ui.comboBox_currency_choice.currentIndex() == 0:
                self.ui.doubleSpinBox_currency_1.setValue(
                    round(self.ui.doubleSpinBox_currency_2.value() / self.sek_rate, 2))
            else:
                self.ui.doubleSpinBox_currency_1.setValue(
                    round(self.ui.doubleSpinBox_currency_2.value() / self.usd_rate, 2))


window = MainWindow()
window.show()

sys.exit(app.exec_())


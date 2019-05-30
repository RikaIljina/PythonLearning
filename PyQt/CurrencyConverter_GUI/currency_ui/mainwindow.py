# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'currency_ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 261)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_currency_choice = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_currency_choice.setObjectName("comboBox_currency_choice")
        self.comboBox_currency_choice.addItem("")
        self.comboBox_currency_choice.addItem("")
        self.gridLayout.addWidget(self.comboBox_currency_choice, 0, 2, 1, 1)
        self.label_select = QtWidgets.QLabel(self.centralWidget)
        self.label_select.setObjectName("label_select")
        self.gridLayout.addWidget(self.label_select, 0, 1, 1, 1)
        self.doubleSpinBox_currency_1 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_currency_1.setMaximum(100000000.0)
        self.doubleSpinBox_currency_1.setObjectName("doubleSpinBox_currency_1")
        self.gridLayout.addWidget(self.doubleSpinBox_currency_1, 1, 2, 1, 1)
        self.doubleSpinBox_currency_2 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_currency_2.setMaximum(100000000.0)
        self.doubleSpinBox_currency_2.setObjectName("doubleSpinBox_currency_2")
        self.gridLayout.addWidget(self.doubleSpinBox_currency_2, 2, 2, 1, 1)
        self.label_currency_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_currency_2.setText("")
        self.label_currency_2.setObjectName("label_currency_2")
        self.gridLayout.addWidget(self.label_currency_2, 2, 1, 1, 1)
        self.label_currency_1 = QtWidgets.QLabel(self.centralWidget)
        self.label_currency_1.setText("")
        self.label_currency_1.setObjectName("label_currency_1")
        self.gridLayout.addWidget(self.label_currency_1, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_browse = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.horizontalLayout.addWidget(self.pushButton_browse)
        self.pushButton_crawl = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_crawl.setObjectName("pushButton_crawl")
        self.horizontalLayout.addWidget(self.pushButton_crawl)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.label_progress = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_progress.setFont(font)
        self.label_progress.setAlignment(QtCore.Qt.AlignCenter)
        self.label_progress.setObjectName("label_progress")
        self.gridLayout_2.addWidget(self.label_progress, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 421, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Converter"))
        self.comboBox_currency_choice.setCurrentText(_translate("MainWindow", "EUR - SEK"))
        self.comboBox_currency_choice.setItemText(0, _translate("MainWindow", "EUR - SEK"))
        self.comboBox_currency_choice.setItemText(1, _translate("MainWindow", "EUR - USD"))
        self.label_select.setText(_translate("MainWindow", "Select currency pair:"))
        self.pushButton_browse.setText(_translate("MainWindow", "Open local csv file..."))
        self.pushButton_crawl.setText(_translate("MainWindow", "Crawl rates from ECB website"))
        self.label_progress.setText(_translate("MainWindow", "Crawling ..."))



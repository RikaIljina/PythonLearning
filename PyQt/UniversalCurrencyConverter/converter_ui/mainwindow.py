# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converter_ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 364)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label_info = QtWidgets.QLabel(self.centralWidget)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.gridLayout.addWidget(self.label_info, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 5, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_options = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_options.setObjectName("comboBox_options")
        self.horizontalLayout.addWidget(self.comboBox_options)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_eur = QtWidgets.QLabel(self.centralWidget)
        self.label_eur.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_eur.setObjectName("label_eur")
        self.horizontalLayout_4.addWidget(self.label_eur)
        self.doubleSpinBox_eur = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_eur.setDecimals(3)
        self.doubleSpinBox_eur.setMaximum(9999999.0)
        self.doubleSpinBox_eur.setSingleStep(0.01)
        self.doubleSpinBox_eur.setObjectName("doubleSpinBox_eur")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_eur)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_chosen_currency = QtWidgets.QLabel(self.centralWidget)
        self.label_chosen_currency.setText("")
        self.label_chosen_currency.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_chosen_currency.setObjectName("label_chosen_currency")
        self.horizontalLayout_5.addWidget(self.label_chosen_currency)
        self.doubleSpinBox_currency = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_currency.setDecimals(3)
        self.doubleSpinBox_currency.setMaximum(99999999.0)
        self.doubleSpinBox_currency.setSingleStep(0.01)
        self.doubleSpinBox_currency.setObjectName("doubleSpinBox_currency")
        self.horizontalLayout_5.addWidget(self.doubleSpinBox_currency)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 553, 21))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Crawl latest rates"))
        self.label_info.setText(_translate("MainWindow", "No rates available"))
        self.label.setText(_translate("MainWindow", "Choose a currency:"))
        self.label_eur.setText(_translate("MainWindow", "EUR"))



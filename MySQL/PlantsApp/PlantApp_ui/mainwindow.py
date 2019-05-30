# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlantApp_ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 379)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.comboBox_plantTypes = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_plantTypes.setGeometry(QtCore.QRect(230, 40, 221, 31))
        self.comboBox_plantTypes.setObjectName("comboBox_plantTypes")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 131, 21))
        self.label.setObjectName("label")
        self.comboBox_plants = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_plants.setGeometry(QtCore.QRect(230, 100, 221, 31))
        self.comboBox_plants.setObjectName("comboBox_plants")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 131, 21))
        self.label_3.setObjectName("label_3")
        self.textBrowser_neighbours = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_neighbours.setGeometry(QtCore.QRect(230, 160, 221, 141))
        self.textBrowser_neighbours.setObjectName("textBrowser_neighbours")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 497, 21))
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
        self.label.setText(_translate("MainWindow", "All plant types"))
        self.label_2.setText(_translate("MainWindow", "All plants"))
        self.label_3.setText(_translate("MainWindow", "Good neighbours"))



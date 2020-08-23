# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from reelgetiri import Ui_ReelGetiri

class Ui_MainWindow(object):

    def openWindowReelGetiri(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ReelGetiri()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ReelGetiriH = QtWidgets.QPushButton(self.centralwidget)
        self.ReelGetiriH.setGeometry(QtCore.QRect(420, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ReelGetiriH.setFont(font)
        self.ReelGetiriH.setObjectName("ReelGetiriH")

        self.ReelGetiriH.clicked.connect(self.openWindowReelGetiri)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Finansal Hesaplama Araçları"))
        self.label.setText(_translate("MainWindow", "Reel getiri hesabı"))
        self.ReelGetiriH.setText(_translate("MainWindow", "Hesapla"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

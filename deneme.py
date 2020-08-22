from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 454)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.hesapla1 = QtWidgets.QPushButton(self.centralwidget)
        self.hesapla1.setGeometry(QtCore.QRect(410, 30, 111, 61))
        self.hesapla1.setObjectName("hesapla1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.hesapla = QtWidgets.QPushButton(self.centralwidget)
        self.hesapla.setGeometry(QtCore.QRect(410, 90, 100, 200))
        self.hesapla.setObjectName("lavlav")

        self.faiz=QtWidgets.QLineEdit(self.centralwidget)
        self.faiz.setGeometry(QtCore.QRect(200,200,50,20))
        self.faiz.setObjectName("FaizGiris")

        self.sonuc=QtWidgets.QLabel(self.centralwidget)
        self.sonuc.setGeometry(QtCore.QRect(160,110,331,161))
        self.sonuc.setObjectName("sonuc")
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Finansal Hesaplama Araçları"))
        self.label.setText(_translate("MainWindow", "Reel getiri oranı hesaplama"))
        self.hesapla1.setText(_translate("MainWindow", "Hesapla"))

        self.hesapla.setText(_translate("Dialog","TIKLA"))

        self.sonuc.setText(_translate("MainWindow","Sonuç = "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
sad

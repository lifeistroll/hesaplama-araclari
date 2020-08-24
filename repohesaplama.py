# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'repohesaplama.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_repogethesaplama(object):
    def setupUi(self, repogethesaplama):
        repogethesaplama.setObjectName("repogethesaplama")
        repogethesaplama.resize(459, 361)
        self.centralwidget = QtWidgets.QWidget(repogethesaplama)
        self.centralwidget.setObjectName("centralwidget")
        self.label_anapara = QtWidgets.QLabel(self.centralwidget)
        self.label_anapara.setGeometry(QtCore.QRect(50, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_anapara.setFont(font)
        self.label_anapara.setObjectName("label_anapara")
        self.label_gun = QtWidgets.QLabel(self.centralwidget)
        self.label_gun.setGeometry(QtCore.QRect(50, 172, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_gun.setFont(font)
        self.label_gun.setObjectName("label_gun")
        self.input_anapara = QtWidgets.QLineEdit(self.centralwidget)
        self.input_anapara.setGeometry(QtCore.QRect(50, 50, 371, 31))
        self.input_anapara.setObjectName("input_anapara")
        self.input_faiz = QtWidgets.QLineEdit(self.centralwidget)
        self.input_faiz.setGeometry(QtCore.QRect(50, 129, 371, 31))
        self.input_faiz.setObjectName("input_faiz")
        self.input_gun = QtWidgets.QLineEdit(self.centralwidget)
        self.input_gun.setGeometry(QtCore.QRect(50, 200, 371, 31))
        self.input_gun.setObjectName("input_gun")
        self.btn_hesapla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hesapla.setGeometry(QtCore.QRect(320, 250, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_hesapla.setFont(font)
        self.btn_hesapla.setObjectName("btn_hesapla")

        self.btn_hesapla.clicked.connect(self.pressed)
        
        self.label_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_sonuc.setGeometry(QtCore.QRect(50, 250, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_sonuc.setFont(font)
        self.label_sonuc.setObjectName("label_sonuc")
        self.label_faiz = QtWidgets.QLabel(self.centralwidget)
        self.label_faiz.setGeometry(QtCore.QRect(50, 90, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_faiz.setFont(font)
        self.label_faiz.setObjectName("label_faiz")
        repogethesaplama.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(repogethesaplama)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName("menubar")
        repogethesaplama.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(repogethesaplama)
        self.statusbar.setObjectName("statusbar")
        repogethesaplama.setStatusBar(self.statusbar)

        self.retranslateUi(repogethesaplama)
        QtCore.QMetaObject.connectSlotsByName(repogethesaplama)

    def retranslateUi(self, repogethesaplama):
        _translate = QtCore.QCoreApplication.translate
        repogethesaplama.setWindowTitle(_translate("repogethesaplama", "Repo Getirisi Hesaplama"))
        self.label_anapara.setText(_translate("repogethesaplama", "Anapara (örn: 42500.75)"))
        self.label_gun.setText(_translate("repogethesaplama", "Gün (örn: 30)"))
        self.btn_hesapla.setText(_translate("repogethesaplama", "Hesapla"))
        self.label_sonuc.setText(_translate("repogethesaplama", "Brüt= "))
        self.label_faiz.setText(_translate("repogethesaplama", "Faiz (örn: 12.75)"))

    def pressed(self):
        anapara = float(self.input_anapara.text())
        faiz = float(self.input_faiz.text())
        gun = float(self.input_gun.text())
        getiri= float((anapara/100)*(faiz/365)*gun)
        self.label_sonuc.setText("Brüt = "+str(getiri))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    repogethesaplama = QtWidgets.QMainWindow()
    ui = Ui_repogethesaplama()
    ui.setupUi(repogethesaplama)
    repogethesaplama.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reelgetiri.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReelGetiri(object):
    def setupUi(self, ReelGetiri):
        ReelGetiri.setObjectName("ReelGetiri")
        ReelGetiri.resize(522, 320)
        self.centralwidget = QtWidgets.QWidget(ReelGetiri)
        self.centralwidget.setObjectName("centralwidget")
        self.nominal = QtWidgets.QLineEdit(self.centralwidget)
        self.nominal.setGeometry(QtCore.QRect(30, 40, 471, 41))
        self.nominal.setObjectName("nominal")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.enflasyon = QtWidgets.QLineEdit(self.centralwidget)
        self.enflasyon.setGeometry(QtCore.QRect(30, 140, 471, 41))
        self.enflasyon.setObjectName("enflasyon")
        self.hesapla = QtWidgets.QPushButton(self.centralwidget)
        self.hesapla.setGeometry(QtCore.QRect(380, 210, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hesapla.setFont(font)
        self.hesapla.setObjectName("hesapla")

        self.hesapla.clicked.connect(self.pressed)
        
        self.sonuc = QtWidgets.QLabel(self.centralwidget)
        self.sonuc.setGeometry(QtCore.QRect(30, 220, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sonuc.setFont(font)
        self.sonuc.setObjectName("sonuc")
        ReelGetiri.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ReelGetiri)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 21))
        self.menubar.setObjectName("menubar")
        ReelGetiri.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ReelGetiri)
        self.statusbar.setObjectName("statusbar")
        ReelGetiri.setStatusBar(self.statusbar)

        self.retranslateUi(ReelGetiri)
        QtCore.QMetaObject.connectSlotsByName(ReelGetiri)

    def retranslateUi(self, ReelGetiri):
        _translate = QtCore.QCoreApplication.translate
        ReelGetiri.setWindowTitle(_translate("ReelGetiri", "Reel Getiri Hesaplama"))
        self.label.setText(_translate("ReelGetiri", "Nominal getiri (örn: 0.18)"))
        self.label_2.setText(_translate("ReelGetiri", "Enflasyon oranı (örn: 0.08) "))
        self.hesapla.setText(_translate("ReelGetiri", "Hesapla"))
        self.sonuc.setText(_translate("ReelGetiri", "Reel getiri oranı = "))

    def pressed(self):
        enflasyon=float(self.enflasyon.text())
        nominal=float(self.nominal.text())
        reelgetiri= float((1+nominal)/(1+enflasyon)-1)
        self.sonuc.setText("Reel getiri oranı = "+str(reelgetiri))
    

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReelGetiri = QtWidgets.QMainWindow()
    ui = Ui_ReelGetiri()
    ui.setupUi(ReelGetiri)
    ReelGetiri.show()
    sys.exit(app.exec_())

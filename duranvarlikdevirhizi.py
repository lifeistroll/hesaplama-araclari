# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'duranvarlikdevirhizi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_duranvarlikdevirhizi(object):
    def setupUi(self, duranvarlikdevirhizi):
        duranvarlikdevirhizi.setObjectName("duranvarlikdevirhizi")
        duranvarlikdevirhizi.resize(466, 326)
        self.widget = QtWidgets.QWidget(duranvarlikdevirhizi)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 20, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.netsatislar = QtWidgets.QLineEdit(self.widget)
        self.netsatislar.setGeometry(QtCore.QRect(30, 60, 391, 31))
        self.netsatislar.setObjectName("netsatislar")
        self.ortduranvarlik = QtWidgets.QLineEdit(self.widget)
        self.ortduranvarlik.setGeometry(QtCore.QRect(30, 160, 391, 31))
        self.ortduranvarlik.setObjectName("ortduranvarlik")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.hesapla = QtWidgets.QPushButton(self.widget)
        self.hesapla.setGeometry(QtCore.QRect(330, 220, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hesapla.setFont(font)
        self.hesapla.setObjectName("hesapla")

        self.hesapla.clicked.connect(self.pressed)
        
        self.sonuc = QtWidgets.QLabel(self.widget)
        self.sonuc.setGeometry(QtCore.QRect(30, 220, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sonuc.setFont(font)
        self.sonuc.setObjectName("sonuc")
        duranvarlikdevirhizi.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(duranvarlikdevirhizi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 21))
        self.menubar.setObjectName("menubar")
        duranvarlikdevirhizi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(duranvarlikdevirhizi)
        self.statusbar.setObjectName("statusbar")
        duranvarlikdevirhizi.setStatusBar(self.statusbar)

        self.retranslateUi(duranvarlikdevirhizi)
        QtCore.QMetaObject.connectSlotsByName(duranvarlikdevirhizi)

    def retranslateUi(self, duranvarlikdevirhizi):
        _translate = QtCore.QCoreApplication.translate
        duranvarlikdevirhizi.setWindowTitle(_translate("duranvarlikdevirhizi", "Duran Varlıklar Devir Hızı Oranı Hesaplama"))
        self.label.setText(_translate("duranvarlikdevirhizi", "Net Satışlar"))
        self.label_2.setText(_translate("duranvarlikdevirhizi", "Ortalama Duran Varlıklar"))
        self.hesapla.setText(_translate("duranvarlikdevirhizi", "Hesapla"))
        self.sonuc.setText(_translate("duranvarlikdevirhizi", "Sonuç ="))
    
    def pressed(self):
        netsatislar = float(self.netsatislar.text())
        ortduranvarlik = float(self.ortduranvarlik.text())
        sonuc=float(netsatislar/ortduranvarlik)
        self.sonuc.setText("Sonuç = "+str(sonuc))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    duranvarlikdevirhizi = QtWidgets.QMainWindow()
    ui = Ui_duranvarlikdevirhizi()
    ui.setupUi(duranvarlikdevirhizi)
    duranvarlikdevirhizi.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'donervarlikdevirhizi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_donervarlikdevirhizi_2(object):
    def setupUi(self, donervarlikdevirhizi_2):
        donervarlikdevirhizi_2.setObjectName("donervarlikdevirhizi_2")
        donervarlikdevirhizi_2.resize(466, 326)
        self.widget = QtWidgets.QWidget(donervarlikdevirhizi_2)
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
        self.ortdonenvarlik = QtWidgets.QLineEdit(self.widget)
        self.ortdonenvarlik.setGeometry(QtCore.QRect(30, 160, 391, 31))
        self.ortdonenvarlik.setObjectName("ortdonenvarlik")
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
        donervarlikdevirhizi_2.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(donervarlikdevirhizi_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 21))
        self.menubar.setObjectName("menubar")
        donervarlikdevirhizi_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(donervarlikdevirhizi_2)
        self.statusbar.setObjectName("statusbar")
        donervarlikdevirhizi_2.setStatusBar(self.statusbar)

        self.retranslateUi(donervarlikdevirhizi_2)
        QtCore.QMetaObject.connectSlotsByName(donervarlikdevirhizi_2)

    def retranslateUi(self, donervarlikdevirhizi_2):
        _translate = QtCore.QCoreApplication.translate
        donervarlikdevirhizi_2.setWindowTitle(_translate("donervarlikdevirhizi_2", "Dönen Varlıklar Devir Hızı Oranı Hesaplama"))
        self.label.setText(_translate("donervarlikdevirhizi_2", "Net Satışlar"))
        self.label_2.setText(_translate("donervarlikdevirhizi_2", "Ortalama Dönen Varlıklar"))
        self.hesapla.setText(_translate("donervarlikdevirhizi_2", "Hesapla"))
        self.sonuc.setText(_translate("donervarlikdevirhizi_2", "Sonuç ="))
    
    def pressed(self):
        netsatislar = float(self.netsatislar.text())
        ortalamadonen= float(self.ortdonenvarlik.text())
        sonuc= float(netsatislar/ortalamadonen)
        self.sonuc.setText("Sonuç = "+ str(sonuc))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    donervarlikdevirhizi_2 = QtWidgets.QMainWindow()
    ui = Ui_donervarlikdevirhizi_2()
    ui.setupUi(donervarlikdevirhizi_2)
    donervarlikdevirhizi_2.show()
    sys.exit(app.exec_())

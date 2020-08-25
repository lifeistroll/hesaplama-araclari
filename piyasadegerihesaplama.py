# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_piyasadegerihesaplama(object):
    def setupUi(self, piyasadegerihesaplama):
        piyasadegerihesaplama.setObjectName("piyasadegerihesaplama")
        piyasadegerihesaplama.resize(475, 313)
        self.centralwidget = QtWidgets.QWidget(piyasadegerihesaplama)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(40, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.edit_hissefiyat = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_hissefiyat.setGeometry(QtCore.QRect(40, 60, 421, 31))
        self.edit_hissefiyat.setObjectName("edit_hissefiyat")
        self.btn_hesapla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hesapla.setGeometry(QtCore.QRect(360, 210, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_hesapla.setFont(font)
        self.btn_hesapla.setObjectName("btn_hesapla")

        self.btn_hesapla.clicked.connect(self.pressed)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.edit_hissesayi = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_hissesayi.setGeometry(QtCore.QRect(40, 150, 421, 31))
        self.edit_hissesayi.setObjectName("edit_hissesayi")
        self.sonuc = QtWidgets.QLabel(self.centralwidget)
        self.sonuc.setGeometry(QtCore.QRect(40, 210, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sonuc.setFont(font)
        self.sonuc.setObjectName("sonuc")
        piyasadegerihesaplama.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(piyasadegerihesaplama)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 21))
        self.menubar.setObjectName("menubar")
        piyasadegerihesaplama.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(piyasadegerihesaplama)
        self.statusbar.setObjectName("statusbar")
        piyasadegerihesaplama.setStatusBar(self.statusbar)

        self.retranslateUi(piyasadegerihesaplama)
        QtCore.QMetaObject.connectSlotsByName(piyasadegerihesaplama)

    def retranslateUi(self, piyasadegerihesaplama):
        _translate = QtCore.QCoreApplication.translate
        piyasadegerihesaplama.setWindowTitle(_translate("piyasadegerihesaplama", "Piyasa değeri hesaplama"))
        self.label_1.setText(_translate("piyasadegerihesaplama", "Hissenin fiyatı (örn: 5.74)"))
        self.btn_hesapla.setText(_translate("piyasadegerihesaplama", "Hesapla"))
        self.label_2.setText(_translate("piyasadegerihesaplama", "Hissenin toplam sayısı (örn: 1000000)"))
        self.sonuc.setText(_translate("piyasadegerihesaplama", "Piyasa değeri = "))
    def pressed(self):
        hissesayi = int(self.edit_hissesayi.text())
        hissefiyat = float(self.edit_hissefiyat.text())
        piyasadeg= float(hissefiyat*hissesayi)
        self.sonuc.setText("Piyasa değeri = "+str(piyasadeg))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    piyasadegerihesaplama = QtWidgets.QMainWindow()
    ui = Ui_piyasadegerihesaplama()
    ui.setupUi(piyasadegerihesaplama)
    piyasadegerihesaplama.show()
    sys.exit(app.exec_())

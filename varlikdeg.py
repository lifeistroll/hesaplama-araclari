# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_varlikdeg(object):
    def setupUi(self, varlikdeg):
        varlikdeg.setObjectName("varlikdeg")
        varlikdeg.resize(489, 404)
        self.centralwidget = QtWidgets.QWidget(varlikdeg)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 0, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.sonuc = QtWidgets.QLabel(self.centralwidget)
        self.sonuc.setGeometry(QtCore.QRect(30, 290, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sonuc.setFont(font)
        self.sonuc.setObjectName("sonuc")
        self.edit_aktifler = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_aktifler.setGeometry(QtCore.QRect(30, 40, 421, 31))
        self.edit_aktifler.setObjectName("edit_aktifler")
        self.edit_kvadeborc = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_kvadeborc.setGeometry(QtCore.QRect(30, 140, 421, 31))
        self.edit_kvadeborc.setObjectName("edit_kvadeborc")
        self.edit_uvadeborc = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_uvadeborc.setGeometry(QtCore.QRect(30, 240, 421, 31))
        self.edit_uvadeborc.setObjectName("edit_uvadeborc")
        self.btn_hesapla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hesapla.setGeometry(QtCore.QRect(364, 300, 91, 51))
        self.btn_hesapla.clicked.connect(self.pressed)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_hesapla.setFont(font)
        self.btn_hesapla.setObjectName("btn_hesapla")
        varlikdeg.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(varlikdeg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 21))
        self.menubar.setObjectName("menubar")
        varlikdeg.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(varlikdeg)
        self.statusbar.setObjectName("statusbar")
        varlikdeg.setStatusBar(self.statusbar)

        self.retranslateUi(varlikdeg)
        QtCore.QMetaObject.connectSlotsByName(varlikdeg)

    def retranslateUi(self, varlikdeg):
        _translate = QtCore.QCoreApplication.translate
        varlikdeg.setWindowTitle(_translate("varlikdeg", "MainWindow"))
        self.label1.setText(_translate("varlikdeg", "Toplam aktifler"))
        self.label_2.setText(_translate("varlikdeg", "Kısa vadeli borçlar toplamı"))
        self.label_3.setText(_translate("varlikdeg", "Uzun vadeli borçlar toplamı"))
        self.sonuc.setText(_translate("varlikdeg", "Varlık değeri = "))
        self.btn_hesapla.setText(_translate("varlikdeg", "Hesapla"))
    def pressed(self):
        aktiler = float(self.edit_aktifler.text())
        kvade = float(self.edit_kvadeborc.text())
        uvade = float(self.edit_uvadeborc.text())
        varlikdeg = float(aktiler-kvade-uvade)
        self.sonuc.setText("Varlık değeri =  "+str(varlikdeg))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    varlikdeg = QtWidgets.QMainWindow()
    ui = Ui_varlikdeg()
    ui.setupUi(varlikdeg)
    varlikdeg.show()
    sys.exit(app.exec_())

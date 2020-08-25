from PyQt5 import QtCore, QtGui, QtWidgets
from reelgetiri import Ui_ReelGetiri
from repohesaplama import Ui_repogethesaplama
from piyasadegerihesaplama import Ui_piyasadegerihesaplama
from varlikdeg import Ui_varlikdeg

class Ui_MainWindow(object):

    def openWindowReelGetiri(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ReelGetiri()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindowRepoGetiri(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Ui_repogethesaplama()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindowPiyasaDegeri(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Ui_piyasadegerihesaplama()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindowVarlikDegeri(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Ui_varlikdeg()
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
        font.setPointSize(18)
        self.ReelGetiriH.setFont(font)
        self.ReelGetiriH.setObjectName("ReelGetiriH")

        self.ReelGetiriH.clicked.connect(self.openWindowReelGetiri)


        self.label_repo = QtWidgets.QLabel(self.centralwidget)
        self.label_repo.setGeometry(QtCore.QRect(30, 50, 291, 61))
        self.label_repo.setFont(font)
        self.label_repo.setObjectName("label_repo")
        font = QtGui.QFont()
        font.setPointSize(18)

        self.repo_btn = QtWidgets.QPushButton(self.centralwidget)
        self.repo_btn.setGeometry(QtCore.QRect(420, 60, 101, 41))
        self.repo_btn.setFont(font)
        self.repo_btn.setObjectName("ReelGetiriH")

        self.repo_btn.clicked.connect(self.openWindowRepoGetiri)

        self.label_piyasadeg = QtWidgets.QLabel(self.centralwidget)
        self.label_piyasadeg.setGeometry(QtCore.QRect(30, 100, 291, 61))
        self.label_piyasadeg.setFont(font)
        self.label_piyasadeg.setObjectName("label_piyasadeg")
        font = QtGui.QFont()
        font.setPointSize(18)

        self.piyasadeg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.piyasadeg_btn.setGeometry(QtCore.QRect(420, 110, 101, 41))
        self.piyasadeg_btn.setFont(font)
        self.piyasadeg_btn.setObjectName("piyasadegH")

        self.piyasadeg_btn.clicked.connect(self.openWindowPiyasaDegeri)


        self.label_varlıkdeg = QtWidgets.QLabel(self.centralwidget)
        self.label_varlıkdeg.setGeometry(QtCore.QRect(30, 150, 291, 61))
        self.label_varlıkdeg.setFont(font)
        self.label_varlıkdeg.setObjectName("label_varlıkdeg")
        font = QtGui.QFont()
        font.setPointSize(18)

        self.varlıkdeg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.varlıkdeg_btn.setGeometry(QtCore.QRect(420, 160, 101, 41))
        self.varlıkdeg_btn.setFont(font)
        self.varlıkdeg_btn.setObjectName("varlıkdegH")

        self.varlıkdeg_btn.clicked.connect(self.openWindowVarlikDegeri)

        
        
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
        self.label.setText(_translate("MainWindow", "Reel getiri hesaplama"))
        self.ReelGetiriH.setText(_translate("MainWindow", "Hesapla"))
        self.label_repo.setText(_translate("MainWindow", "Repo getirisi hesaplama"))
        self.repo_btn.setText(_translate("MainWindow", "Hesapla"))
        self.label_piyasadeg.setText(_translate("MainWindow", "Piyasa değeri hesaplama"))
        self.piyasadeg_btn.setText(_translate("MainWindow", "Hesapla"))
        self.label_varlıkdeg.setText(_translate("MainWindow", "Varlık değeri hesaplama"))
        self.varlıkdeg_btn.setText(_translate("MainWindow", "Hesapla"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

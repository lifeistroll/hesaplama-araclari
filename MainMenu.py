from PyQt5 import QtCore, QtGui, QtWidgets
from reelgetiri import Ui_ReelGetiri
from repohesaplama import Ui_repogethesaplama
from piyasadegerihesaplama import Ui_piyasadegerihesaplama
from varlikdeg import Ui_varlikdeg
from donervarlikdevirhizi import Ui_donervarlikdevirhizi_2
from duranvarlikdevirhizi import Ui_duranvarlikdevirhizi

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
    def openWindowdonervarlikdevirhizi(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Ui_donervarlikdevirhizi_2()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWidnowduranvarlikdevirhizi(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Ui_duranvarlikdevirhizi()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 489, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        

        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0)
        self.label.setMaximumSize(QtCore.QSize(400, 50))
        
        self.ReelGetiriH = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ReelGetiriH.setFont(font)
        self.ReelGetiriH.setObjectName("ReelGetiriH")
        self.gridLayout.addWidget(self.ReelGetiriH, 0,1)
        self.ReelGetiriH.setMaximumSize(QtCore.QSize(100, 50))
        self.ReelGetiriH.clicked.connect(self.openWindowReelGetiri)

        
        self.label_repo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_repo.setGeometry(QtCore.QRect(30, 50, 291, 61))
        self.label_repo.setFont(font)
        self.label_repo.setObjectName("label_repo")
        self.gridLayout.addWidget(self.label_repo, 1, 0)
        self.label_repo.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(18)

        self.repo_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        
        self.repo_btn.setFont(font)
        self.repo_btn.setMaximumSize(QtCore.QSize(100, 50))
        self.gridLayout.addWidget(self.repo_btn, 1, 1)
        self.repo_btn.setObjectName("repo_btn")

        self.repo_btn.clicked.connect(self.openWindowRepoGetiri)

        self.label_piyasadeg = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.label_piyasadeg, 2,0)
        
        self.label_piyasadeg.setFont(font)
        self.label_piyasadeg.setObjectName("label_piyasadeg")
        self.label_piyasadeg.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(18)

        self.piyasadeg_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        
        self.piyasadeg_btn.setFont(font)
        self.piyasadeg_btn.setObjectName("piyasadegH")
        self.gridLayout.addWidget(self.piyasadeg_btn, 2,1)
        self.piyasadeg_btn.setMaximumSize(QtCore.QSize(100, 50))

        self.piyasadeg_btn.clicked.connect(self.openWindowPiyasaDegeri)

        self.label_varlıkdeg = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        
        self.label_varlıkdeg.setFont(font)
        self.label_varlıkdeg.setObjectName("label_varlıkdeg")
        self.label_varlıkdeg.setMaximumSize(QtCore.QSize(400, 50))
        self.gridLayout.addWidget(self.label_varlıkdeg, 3,0)
        font = QtGui.QFont()
        font.setPointSize(18)

        self.varlıkdeg_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        
        self.varlıkdeg_btn.setFont(font)
        self.varlıkdeg_btn.setObjectName("varlıkdegH")
        self.gridLayout.addWidget(self.varlıkdeg_btn, 3,1)
        self.varlıkdeg_btn.setMaximumSize(QtCore.QSize(100, 50))

        self.varlıkdeg_btn.clicked.connect(self.openWindowVarlikDegeri)

        self.label_donenvarlikdevir = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        
        self.label_donenvarlikdevir.setFont(font)
        self.label_donenvarlikdevir.setObjectName("label_donenvarlikdevir")
        self.label_donenvarlikdevir.setMaximumSize(QtCore.QSize(400, 50))
        self.gridLayout.addWidget(self.label_donenvarlikdevir, 4,0)
        font = QtGui.QFont()
        font.setPointSize(18)

        self.donenvarlikdevir_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        
        self.donenvarlikdevir_btn.setFont(font)
        self.donenvarlikdevir_btn.setObjectName("donenvarlikdevirH")
        self.gridLayout.addWidget(self.donenvarlikdevir_btn, 4,1)
        self.donenvarlikdevir_btn.setMaximumSize(QtCore.QSize(100, 50))

        self.donenvarlikdevir_btn.clicked.connect(self.openWindowdonervarlikdevirhizi)

        self.label_duranvarlikdevir = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        
        self.label_duranvarlikdevir.setFont(font)
        self.label_duranvarlikdevir.setObjectName("label_duranvarlikdevir")
        self.gridLayout.addWidget(self.label_duranvarlikdevir, 5,0)
        self.label_duranvarlikdevir.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(18)

        self.duranvarlikdevir_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        

        self.duranvarlikdevir_btn.setFont(font)
        self.duranvarlikdevir_btn.setObjectName("duranvarlikdevirH")
        self.gridLayout.addWidget(self.duranvarlikdevir_btn, 5,1)
        self.duranvarlikdevir_btn.setMaximumSize(QtCore.QSize(100, 50))

        self.duranvarlikdevir_btn.clicked.connect(self.openWidnowduranvarlikdevirhizi)

        
        self.gridLayout.addWidget(self.label)
        self.gridLayout.addWidget(self.ReelGetiriH)
        self.gridLayout.addWidget(self.label_repo)
        self.gridLayout.addWidget(self.repo_btn)
        self.gridLayout.addWidget(self.label_piyasadeg)
        self.gridLayout.addWidget(self.piyasadeg_btn)
        self.gridLayout.addWidget(self.label_varlıkdeg)
        self.gridLayout.addWidget(self.varlıkdeg_btn)
        self.gridLayout.addWidget(self.label_donenvarlikdevir)
        self.gridLayout.addWidget(self.donenvarlikdevir_btn)
        self.gridLayout.addWidget(self.label_duranvarlikdevir)
        self.gridLayout.addWidget(self.duranvarlikdevir_btn)



        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
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
        self.label_donenvarlikdevir.setText(_translate("MainWindow", "Dönen varlıkların devir hızını hes."))
        self.donenvarlikdevir_btn.setText(_translate("MainWindow", "Hesapla"))
        self.label_duranvarlikdevir.setText(_translate("MainWindow", "Duran varlıkların devir hızını hes."))
        self.duranvarlikdevir_btn.setText(_translate("MainWindow", "Hesapla"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

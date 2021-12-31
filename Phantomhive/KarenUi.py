
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KarenUI(object):
    def setupUi(self, KarenUI):
        KarenUI.setObjectName("KarenUI")
        KarenUI.resize(1235, 803)
        self.centralwidget = QtWidgets.QWidget(KarenUI)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_1 = QtWidgets.QLabel(self.centralwidget)
        self.bg_1.setGeometry(QtCore.QRect(-10, -20, 1671, 831))
        self.bg_1.setText("")
        self.bg_1.setPixmap(QtGui.QPixmap("drive-download-20211227T071319Z-001/B.G/Black_Template.jpg"))
        self.bg_1.setScaledContents(True)
        self.bg_1.setObjectName("bg_1")
        self.bg_2 = QtWidgets.QLabel(self.centralwidget)
        self.bg_2.setGeometry(QtCore.QRect(20, 20, 411, 241))
        self.bg_2.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.bg_2.setText("")
        self.bg_2.setObjectName("bg_2")

        self.Gif_1 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_1.setGeometry(QtCore.QRect(20, 20, 411, 241))
        self.Gif_1.setText("")
        self.Gif_1.setPixmap(QtGui.QPixmap("drive-download-20211227T071319Z-001/ExtraGui/B.G_Template_1.gif"))
        self.Gif_1.setScaledContents(True)
        self.Gif_1.setObjectName("Gif_1")

        self.Gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_2.setGeometry(QtCore.QRect(450, 290, 751, 491))
        self.Gif_2.setText("")
        self.Gif_2.setPixmap(QtGui.QPixmap("drive-download-20211227T071319Z-001/ExtraGui/Hero_Template.gif"))
        self.Gif_2.setScaledContents(True)
        self.Gif_2.setObjectName("Gif_2")

        self.bg_4 = QtWidgets.QLabel(self.centralwidget)
        self.bg_4.setGeometry(QtCore.QRect(30, 300, 331, 261))
        self.bg_4.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.bg_4.setText("")
        self.bg_4.setObjectName("bg_4")

        self.Gif_3 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_3.setGeometry(QtCore.QRect(30, 300, 331, 261))
        self.Gif_3.setText("")
        self.Gif_3.setPixmap(QtGui.QPixmap("drive-download-20211227T071319Z-001/ExtraGui/Earth.gif"))
        self.Gif_3.setScaledContents(True)
        self.Gif_3.setObjectName("Gif_3")

        self.Gif_5 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_5.setGeometry(QtCore.QRect(900, 50, 301, 181))
        self.Gif_5.setText("")
        self.Gif_5.setPixmap(QtGui.QPixmap("drive-download-20211227T071319Z-001/ExtraGui/Earth_Template.gif"))
        self.Gif_5.setScaledContents(True)
        self.Gif_5.setObjectName("Gif_5")

        self.Gif_6 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_6.setGeometry(QtCore.QRect(470, 0, 431, 261))
        self.Gif_6.setText("")
        self.Gif_6.setPixmap(QtGui.QPixmap("drive-download-20211227T071319Z-001/ExtraGui/Health_Template.gif"))
        self.Gif_6.setScaledContents(True)
        self.Gif_6.setObjectName("Gif_6")
        
        self.Gif_4 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_4.setGeometry(QtCore.QRect(30, 580, 331, 201))
        self.Gif_4.setText("")
        self.Gif_4.setPixmap(QtGui.QPixmap("drive-download-20211227T071319Z-001/ExtraGui/Jarvis_Gui (1).gif"))
        self.Gif_4.setScaledContents(True)
        self.Gif_4.setObjectName("Gif_4")
        KarenUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(KarenUI)
        QtCore.QMetaObject.connectSlotsByName(KarenUI)

    def retranslateUi(self, KarenUI):
        _translate = QtCore.QCoreApplication.translate
        KarenUI.setWindowTitle(_translate("KarenUI", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KarenUI = QtWidgets.QMainWindow()
    ui = Ui_KarenUI()
    ui.setupUi(KarenUI)
    KarenUI.show()
    sys.exit(app.exec_())

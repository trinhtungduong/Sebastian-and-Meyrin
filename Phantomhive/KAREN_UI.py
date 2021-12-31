from KarenUi import Ui_KarenUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import KAREN 
import sys
import os

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()       
    
    def run(self):
        self.start_vitural_assistant()
        os._exit(0)       
                      
    def start_vitural_assistant(self):
        KAREN.run_vitural_assistant()    
       
class Gui_Start(QMainWindow):
    def __init__ (self):
        super().__init__()                
        self.gui = Ui_KarenUI()
        self.gui.setupUi(self)
        self.karen = MainThread()

        self.startVA()         

    def startVA(self):
        self.gui.label1 = QtGui.QMovie("drive-download-20211227T071319Z-001//ExtraGui//B.G_Template_1.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("drive-download-20211227T071319Z-001//ExtraGui//Hero_Template.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("drive-download-20211227T071319Z-001//ExtraGui//Earth.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("drive-download-20211227T071319Z-001//ExtraGui//Jarvis_Gui (1).gif")
        self.gui.Gif_4.setMovie(self.gui.label4)
        self.gui.label4.start() 

        self.gui.label5 = QtGui.QMovie("drive-download-20211227T071319Z-001//ExtraGui//Earth_Template.gif")
        self.gui.Gif_5.setMovie(self.gui.label5)
        self.gui.label5.start() 

        self.gui.label6 = QtGui.QMovie("drive-download-20211227T071319Z-001//ExtraGui//Health_Template.gif")
        self.gui.Gif_6.setMovie(self.gui.label6)
        self.gui.label6.start()

        self.karen.start()

#START:                                             
GuiApp = QApplication(sys.argv)
karen_gui = Gui_Start()
karen_gui.show()
exit(GuiApp.exec_())

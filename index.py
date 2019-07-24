from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import MySQLdb
ui,_ = loadUiType('libs.ui')

class MainApp(QMainWindow,ui):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()
    
    ##### Opening Tabs ####
    def Handle_UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)

    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)

    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)
        

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)        

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(2)   
        

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)   
    
    ########################################

        ####BOOKS#####

    def Add_New_Book(self):
        pass

    def Search_Books(self):
        pass

    def Edit_Books(self):
        pass

    def Delete_Books(self):
        pass

    ###################

    ##USERS###

    def Add_New_User(self):
        pass

    def Login(self ):
        pass

    def Edit_User(self):
        pass
























    

        


def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_()
    

if __name__=='__main__':
    main()

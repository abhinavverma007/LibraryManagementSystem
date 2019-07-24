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
        self.pushButton_7.clicked.connect(self.Add_New_Book)
        self.pushButton_14.clicked.connect(self.Add_Category)
        self.pushButton_15.clicked.connect(self.Add_Author)
        self.pushButton_16.clicked.connect(self.Add_Publisher)

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
        self.db=MySQLdb.connect(host='localhost',user='root',password='kirtisaloni2',db='library')
        self.cur=self.db.cursor()
        book_title=self.lineEdit_3.text()
        book_code=self.lineEdit_2.text()
        book_category=self.comboBox_3.CurrentText()
        book_author=self.comboBox_3.CurrentText()
        book_publisher=self.comboBox_3.CurrentText()
        book_price=self.comboBox_3.CurrentText()

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

   #####################
    ## SETTINGS ###

    def Add_Category(self):
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()
        category_name=self.lineEdit_19.text()
        self.cur.execute('''
            INSERT INTO category (category_name) VALUES(%s)
            ''',(category_name,))

        self.db.commit()
        self.statusBar().showMessage('New Category Added')

    def Add_Author(self):
        
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()
        author_name=self.lineEdit_20.text()
        self.cur.execute('''
            INSERT INTO authors (author_name) VALUES(%s)
            ''',(author_name,))

        self.db.commit()
        self.statusBar().showMessage('New Author Added')

    def Add_Publisher(self):
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()
        publisher_name=self.lineEdit_20.text()
        self.cur.execute('''
            INSERT INTO publisher (publisher_name) VALUES(%s)
            ''',(publisher_name,))

        self.db.commit()
        self.statusBar().showMessage('New Publisher Added')
 

        


def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_()
    

if __name__=='__main__':
    main()

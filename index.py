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
        self.Show_Category()
        self.Show_Publisher()
        self.Show_Author()
        self.Show_Category_Combobox()
        self.Show_Author_Combobox()
        self.Show_Publisher_Combobox() 
    
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
        self.pushButton_9.clicked.connect(self.Search_Books)

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
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()
        book_title=self.lineEdit_3.text()
        book_description=self.textEdit.toPlainText()
        book_code=self.lineEdit_2.text()
        book_category=self.comboBox_3.currentIndex()
        book_author=self.comboBox_4.currentIndex()
        book_publisher=self.comboBox_5.currentIndex()
        book_price=self.lineEdit_4.text()

        self.cur.execute(''' INSERT INTO book(book_name,book_description,book_code,book_category,book_author,book_publisher,book_price)
                    VALUES(book_name,book_description,book_code,book_category,book_author,book_publisher,book_price)''')
        self.db.commit()
        self.statusBar().showMessage('New Book Added')

        self.lineEdit_3.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_3.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)

    def Search_Books(self):
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()

        book_title=self.lineEdit_5.text()
        sql=''' SELECT * FROM book WHERE book_name= %s '''
        self.cur.execute(sql,[(book_title)])
        data=self.cur.fetchone()
        self.lineEdit_8.setText(data[1])
        self.textEdit_2.setPlainText(data[2])
        self.lineEdit_7.setText(data[3])
        self.comboBox_7.setCurrentIndex(data[4])
        self.comboBox_8.setCurrentIndex(data[5])
        self.comboBox_6.setCurrentIndex(data[6])
        self.lineEdit_6.setText(data[7])
        
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
        self.lineEdit_19.setText('')
        self.Show_Category()
        self.Show_Category_Combobox()

    def Show_Category(self):
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category ''')
        data=self.cur.fetchall()
        print(data)
        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column,item in enumerate(form):
                    self.tableWidget_2.setItem(row,column,QTableWidgetItem(str(item)))
                    column=column+1

                row_position=self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)
        

    def Add_Author(self):
        
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()
        author_name=self.lineEdit_20.text()
        self.cur.execute('''
            INSERT INTO authors (author_name) VALUES(%s)
            ''',(author_name,))

        self.db.commit()
        self.lineEdit_20.setText('')
        self.statusBar().showMessage('New Author Added')
        self.Show_Author()
        self.Show_Author_Combobox()

    def Show_Author(self):
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors ''')
        data=self.cur.fetchall()
        
        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column,item in enumerate(form):
                    self.tableWidget_3.setItem(row,column,QTableWidgetItem(str(item)))
                    column=column+1

                row_position=self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)

    def Add_Publisher(self):
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()
        publisher_name=self.lineEdit_21.text()
        self.cur.execute('''
            INSERT INTO publisher (publisher_name) VALUES(%s)
            ''',(publisher_name,))

        self.db.commit()
        self.lineEdit_21.setText('')
        self.statusBar().showMessage('New Publisher Added')
        self.Show_Publisher()
        self.Show_Publisher_Combobox()
    def Show_Publisher(self):
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data=self.cur.fetchall()
        
        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column,item in enumerate(form):
                    self.tableWidget_4.setItem(row,column,QTableWidgetItem(str(item)))
                    column=column+1

                row_position=self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)

    #################################

    ####### SHOW SETTINGS DATA IN UI #########
    def Show_Category_Combobox(self):
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category ''')
        data=self.cur.fetchall()
        self.comboBox_3.clear()
        for category in  data:
            self.comboBox_3.addItem(category[0])
            self.comboBox_7.addItem(category[0])
            
            

    def Show_Author_Combobox(self):
        
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors ''')
        data=self.cur.fetchall()
        self.comboBox_4.clear()
        for author in  data:
            self.comboBox_4.addItem(author[0])
            self.comboBox_8.addItem(author[0])

    def Show_Publisher_Combobox(self):
        
        self.db=MySQLdb.connect(host='localhost',user='root',password='**',db='library')
        self.cur=self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data=self.cur.fetchall()
        self.comboBox_5.clear()
        for publisher in  data:
            self.comboBox_5.addItem(publisher[0])
            self.comboBox_6.addItem(publisher[0])
        
        


def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_() 
    

if __name__=='__main__':
    main()

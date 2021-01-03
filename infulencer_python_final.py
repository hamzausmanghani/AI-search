from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
import pandas as pd
import sqlite3 as sql
import sklearn
from sklearn.neighbors import KNeighborsClassifier

conn=sql.connect('Influencer.db')

class login(object):
    def __init__(self,MainWindow):
        self.setupUi()
        
    def setupUi(self):
#         self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.showMaximized()
#         MainWindow.setFixedSize(MainWindow.size())
        #height and width of a window
#         MainWindow.resize(1366, 768)
#         MainWindow.setFixedSize(MainWindow.size())
#         print(height,width)
#         MainWindow.setWindowIcon(QtGui.QIcon('icon.jpg')) 
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(33, 66, 82);\nQToolBar->setStyleSheet(\"color: rgb(255,255,255)\");")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_label = QtWidgets.QLabel(self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(640, 240, 101, 61))
#         self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color:rgb(240, 84, 84)")
        self.login_label.setObjectName("login_label")
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(590, 440, 250, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("color:rgb(255, 220, 8)")
        
        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(570, 300, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.username_input.setFont(font)
        self.username_input.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.username_input.setStyleSheet("background-color:rgb(240, 84, 84)")
        self.username_input.setMaxLength(8)
        self.username_input.setAlignment(QtCore.Qt.AlignCenter)
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setGeometry(QtCore.QRect(570, 360, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.password_input.setFont(font)
        self.password_input.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.password_input.setStyleSheet("background-color:rgb(240, 84, 84)")
        self.password_input.setMaxLength(8)
        self.password_input.setAlignment(QtCore.Qt.AlignCenter)
        self.password_input.setObjectName("password_input")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(650, 420, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.login_button.setStyleSheet("background-color:rgb(240, 84, 84)")
        self.login_button.setAutoDefault(False)
        self.login_button.setDefault(False)
        self.login_button.setFlat(False)
        self.login_button.setObjectName("login_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login-InfluBusiness"))
        self.login_label.setText(_translate("MainWindow", "LOGIN"))
        self.username_input.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "login"))
        #Button click function calling
        self.login_button.clicked.connect(self.button_operation)
    
    def button_operation(self):
        _translate = QtCore.QCoreApplication.translate
        print(self.username_input.text())
        print(self.password_input.text())
#         if self.username_input.text()=="admin" and self.password_input.text()=="admin321":
        if True:
            print("Succesfully logged in")
            self.main_window = QtWidgets.QMainWindow()
            self.ui = view_window()
            self.ui.setupUi(self.main_window)
    #         self.add_data_window.setEnabled(True)
    #         MainWindow.setEnabled(True)
            self.main_window.show()
            MainWindow.close()

            
        
            #redirection to new window
        elif self.username_input.text()=="" and self.password_input.text()=="":
            print("Please Enter username and password")
            self.error_label.setText(_translate("MainWindow", "*Missing credentials*"))
        elif self.username_input.text()=="":
            print("Please Enter username")
            self.error_label.setText(_translate("MainWindow", "*Missing credentials*"))
        elif self.password_input.text()=="":
            print("Please Enter password")
            self.error_label.setText(_translate("MainWindow", "*Missing credentials*"))
        else:
            self.error_label.setText(_translate("MainWindow", "*Incorrect credentials*"))
            print("Incorrect credentials")
            #error popup
        

#search

class search(object):
    def __init__(self):
        # super(search, self).__init__(parent)
        self.result=["","","","",""]
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(MainWindow.size())
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(33, 66, 82);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.tableWidget.setGeometry(QtCore.QRect(270, 290, 280, 180))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setItalic(False)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet("background-color:rgb(240, 176, 86);\n"
"gridline-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setObjectName("tableWidget")
#         self.maxrow=15
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(5)
#         item = QtWidgets.QTableWidgetItem()
#         self.tableWidget.setVerticalHeaderItem(0, item)
#         item = QtWidgets.QTableWidgetItem()
#         self.tableWidget.setVerticalHeaderItem(1, item)
#         item = QtWidgets.QTableWidgetItem()
#         self.tableWidget.setVerticalHeaderItem(2, item)
#         item = QtWidgets.QTableWidgetItem()
#         self.tableWidget.setVerticalHeaderItem(3, item)
#         item = QtWidgets.QTableWidgetItem()
#         self.tableWidget.setVerticalHeaderItem(4, item)
        for i in range(len(self.result)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)           
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
#         item = QtWidgets.QTableWidgetItem()
#         item.setTextAlignment(QtCore.Qt.AlignCenter)
#         self.tableWidget.setItem(0, 0, item)
#         item = QtWidgets.QTableWidgetItem()
#         item.setTextAlignment(QtCore.Qt.AlignCenter)
#         self.tableWidget.setItem(1, 0, item)
#         item = QtWidgets.QTableWidgetItem()
#         item.setTextAlignment(QtCore.Qt.AlignCenter)
#         self.tableWidget.setItem(2, 0, item)
#         item = QtWidgets.QTableWidgetItem()
#         item.setTextAlignment(QtCore.Qt.AlignCenter)
#         self.tableWidget.setItem(3, 0, item)
#         item = QtWidgets.QTableWidgetItem()
#         item.setTextAlignment(QtCore.Qt.AlignCenter)
#         self.tableWidget.setItem(4, 0, item)
        for i in range(len(self.result)):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, 0, item)

        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(187)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(23)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.search.setGeometry(QtCore.QRect(415, 250, 81, 27))
        self.search.setStyleSheet("background-color:rgb(240, 84, 84);\n"
"font: 10pt \"Lucida Fax\";\n"
"color: rgb(0, 0, 0);")
        self.search.setObjectName("search")
        self.remuneration = QtWidgets.QLineEdit(self.centralwidget)
        self.remuneration.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remuneration.setGeometry(QtCore.QRect(410, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.remuneration.setFont(font)
        self.remuneration.setStyleSheet("background-color:rgb(240, 84, 84);")
        self.remuneration.setText("")
        self.remuneration.setMaxLength(15)
        self.remuneration.setAlignment(QtCore.Qt.AlignCenter)
        self.remuneration.setObjectName("remuneration")
        self.sector = QtWidgets.QLineEdit(self.centralwidget)
        self.sector.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sector.setGeometry(QtCore.QRect(280, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sector.setFont(font)
        self.sector.setStyleSheet("background-color:rgb(240, 84, 84);")
        self.sector.setText("")
        self.sector.setMaxLength(30)
        self.sector.setAlignment(QtCore.Qt.AlignCenter)
        self.sector.setObjectName("sector")
        self.login_label = QtWidgets.QLabel(self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(320, 120, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color:rgb(240, 84, 84)")
        self.login_label.setObjectName("login_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        #------
        # creating a combo box widget 
        self.combo_box = QComboBox(MainWindow) 
        #design
        self.combo_box.setStyleSheet("background-color:rgb(240, 84, 84);")
        #font
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.combo_box.setFont(font)
        #place holder
#         self.combo_box.setPlaceholderText("count")
        # setting geometry of combo box 
        self.combo_box.setGeometry(325, 250, 81, 27) 
        # geek list 
        k_list = ["5", "10", "15"] 
  
        # adding list of items to combo box 
        self.combo_box.addItems(k_list) 
        #------

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    


    def search_data(self):
        try:
            self.kvalue= int(self.combo_box.currentText())
        except:
            return
        read_all_query="""
        SELECT *
        FROM influencer_information;
        """
        cursor=conn.execute(read_all_query)
        data=[]
        for i in cursor:
            data.append(i)
        self.data =pd.DataFrame(data)
        self.data.iloc[:,2]=self.data.iloc[:,2].apply(lambda x: x.lower())
        le = sklearn.preprocessing.LabelEncoder()
        sector=le.fit_transform(self.data.iloc[:,2])
        self.data["sector_num"]=sector

        rumeneartion=self.data.loc[:,3]
        features=list(zip(sector,rumeneartion))
        #training
        model = sklearn.neighbors.KNeighborsClassifier(n_neighbors=self.kvalue)
        model.fit(features,self.data.iloc[:,1])

        #testing
        try:
            Rumen_in=int(self.remuneration.text())
        except:
            return
        sec_in=(self.sector.text()).lower()

        sec=self.data.loc[:,2].to_list()
        sec.append(sec_in)
        # print("sec:" ,(le.fit_transform(sec)))
        sec=(le.fit_transform(sec))[-1]
        print("input----",sec,Rumen_in)



        influencer=model.kneighbors([[sec,Rumen_in]])[1][0]
 
        self.result=[]
        for i in influencer:
            self.result.append(self.data.iloc[i,1])
    
        
        
#         self.retranslateUi(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Search-InfluBusiness"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(len(self.result))
        for i in range(len(self.result)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = self.tableWidget.verticalHeaderItem(i)
#             item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", str(i+1)))        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name Influencer"))
        for i in range(len(self.result)):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i,0, item)
#             item = self.tableWidget.item(i, 0)
            item.setText(_translate("MainWindow", self.result[i]))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Search-InfluBusiness"))
#         self.tableWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">hhh</p></body></html>"))
        self.tableWidget.setSortingEnabled(True)
#         item = self.tableWidget.verticalHeaderItem(0)
#         item.setText(_translate("MainWindow", "1"))
#         item = self.tableWidget.verticalHeaderItem(1)
#         item.setText(_translate("MainWindow", "2"))
#         item = self.tableWidget.verticalHeaderItem(2)
#         item.setText(_translate("MainWindow", "3"))
#         item = self.tableWidget.verticalHeaderItem(3)
#         item.setText(_translate("MainWindow", "4"))
#         item = self.tableWidget.verticalHeaderItem(4)
#         item.setText(_translate("MainWindow", "5"))

        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(len(self.result))

        for i in range(len(self.result)):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", str(i+1)))        
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name Influencer"))
        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        
#         item = self.tableWidget.item(0, 0)
#         item.setText(_translate("MainWindow", self.result[0]))
#         item = self.tableWidget.item(1, 0)
#         item.setText(_translate("MainWindow", self.result[1]))
#         item = self.tableWidget.item(2, 0)
#         item.setText(_translate("MainWindow", self.result[2]))
#         item = self.tableWidget.item(3, 0)
#         item.setText(_translate("MainWindow", self.result[3]))
#         item = self.tableWidget.item(4, 0)
#         item.setText(_translate("MainWindow", self.result[4]))
        for i in range(len(self.result)):
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("MainWindow", self.result[i]))
        
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.search.setText(_translate("MainWindow", "Search"))
        self.remuneration.setPlaceholderText(_translate("MainWindow", "Remuneration"))
        self.sector.setPlaceholderText(_translate("MainWindow", "Sector"))
        self.login_label.setText(_translate("MainWindow", "AI SEARCH"))
        self.search.clicked.connect(self.search_data)



#add info
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class add_info(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 135)
        MainWindow.setFixedSize(MainWindow.size())
        MainWindow.setStyleSheet("background-color:rgb(33, 66, 82);\n""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 22, 461, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777181, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet("background-color:rgb(240, 176, 86);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"gridline-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(153)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(41)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(33)
        self.tableWidget.verticalHeader().setMinimumSectionSize(15)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 90, 56, 25))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton.setStyleSheet("background-color:rgb(240, 84, 84);\n"
"font: 63 10pt \"Lucida Fax\";\n"
"font: 10pt \"Lucida Fax\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def add_data(self):
#         MainWindow.close()
        influencer_add = self.tableWidget.item(0,0).text()
        sector_add=self.tableWidget.item(0,1).text()
        reum_add=self.tableWidget.item(0,2).text()
        print(str(influencer_add),str(sector_add),str(reum_add))

        insert_query="INSERT INTO influencer_information(influencer_id,influencer_name,sector,remuneration) VALUES(null,'"+str(influencer_add)+"','"+str(sector_add)+"','"+str(reum_add)+"');"
        conn.execute(insert_query)
        conn.commit()
        _translate = QtCore.QCoreApplication.translate
        for i in range(3):
            item = self.tableWidget.item(0, i)
            item.setText(_translate("MainWindow", ""))        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add-InfluBusiness"))
#         self.tableWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">hhh</p></body></html>"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name Influencer"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sector"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Remuneration"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "ADD"))
        self.pushButton.clicked.connect(self.add_data)




import time
class view_window(object):
    
    def __init__(self):
        read_all_query="""
        SELECT *
        FROM influencer_information;
        """
        cursor=conn.execute(read_all_query)
        data=[]
        for i in cursor:
            data.append(i)
        self.data =pd.DataFrame(data)


    def update_data(self):
        read_all_query="""
        SELECT *
        FROM influencer_information;
        """
        cursor=conn.execute(read_all_query)
        data=[]
        for i in cursor:
            data.append(i)
        self.data =pd.DataFrame(data)
        
        self.tableWidget.setColumnCount(len(self.data.columns))
        self.tableWidget.setRowCount(len(self.data))
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         display(self.data)
#         self.retranslateUi(MainWindow)

        for row in range(len(self.data)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(row, item)
            item = self.tableWidget.verticalHeaderItem(row)
            item.setText(_translate("MainWindow", str(row+1)))

        #column head
        item = self.tableWidget.horizontalHeaderItem(0) 
        item.setText(_translate("MainWindow", "Id influencer"))
        item = self.tableWidget.horizontalHeaderItem(1) 
        item.setText(_translate("MainWindow", "Name influencer"))
        item = self.tableWidget.horizontalHeaderItem(2) 
        item.setText(_translate("MainWindow", "Sector"))
        item = self.tableWidget.horizontalHeaderItem(3) 
        item.setText(_translate("MainWindow", "Remuneration"))
        
        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        
        #items
        print(self.data)
        for row in range(len(self.data)):
            for column in range(len(self.data.columns)):
                if (column==0 or column==3):
                    item = QtWidgets.QTableWidgetItem()
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(row,column, item)
#                     item = self.tableWidget.item(row, column)
                    item.setText(_translate("MainWindow",str(self.data.iloc[row,column])))
                else:
                    item = QtWidgets.QTableWidgetItem()
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(row,column, item)
#                     item = self.tableWidget.item(row, column)
                    item.setText(_translate("MainWindow",self.data.iloc[row,column]))
        print("update data called")
        
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("Main")
#         MainWindow.resize(803, 600)
        MainWindow.setStyleSheet("background-color:rgb(33, 66, 82);\n""")
        MainWindow.showMaximized()
#         MainWindow.setEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(292, 190, 824, 401))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) #disabling write
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setItalic(False)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet("background-color:rgb(240, 176, 86);\n""gridline-color: rgb(0, 0, 0);\n""color: rgb(0, 0, 0);")
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(len(self.data.columns))
        self.tableWidget.setRowCount(len(self.data))
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(590, 100, 270, 90))
#         self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color:rgb(240, 84, 84)")
        
        #rows
        for index in range(len(self.data)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(index, item)
        #columns
        for column_count in range(len(self.data.columns)):
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(QtGui.QColor(255, 0, 0))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setFamily("Lucida Fax")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(column_count, item)
        
        #items
        for row in range(len(self.data)):
            for column in range(len(self.data.columns)):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(row,column, item)

        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(73)
#         self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
#         self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton.setGeometry(QtCore.QRect(400, 610, 151, 31))
        self.pushButton.setStyleSheet("background-color:rgb(240, 84, 84);\n""font: 10pt \"Lucida Fax\";\n""color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_2.setGeometry(QtCore.QRect(560, 610, 151, 31))
        self.pushButton_2.setStyleSheet("background-color:rgb(240, 84, 84);\n""font: 10pt \"Lucida Fax\";\n""color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_3.setGeometry(QtCore.QRect(720, 610, 151, 31))
        self.pushButton_3.setStyleSheet("background-color:rgb(240, 84, 84);\n""font: 10pt \"Lucida Fax\";\n""color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton_4.setGeometry(QtCore.QRect(880, 610, 151, 31))
        self.pushButton_4.setStyleSheet("background-color:rgb(240, 84, 84);\n""font: 10pt \"Lucida Fax\";\n""color: rgb(0, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def delete_data(self):
        if self.tableWidget.selectionModel().hasSelection():
            index = self.tableWidget.currentRow()
            idd=int(self.data.iloc[index,0])
            delete_Query=("delete from influencer_information where influencer_id="+str(idd))
            conn.execute(delete_Query)
            conn.commit()
        else:
            pass
        self.update_data()

            
            
    def add_data(self):

        self.add_data_window = QtWidgets.QMainWindow()
        self.ui = add_info()
        self.ui.setupUi(self.add_data_window)
        self.add_data_window.show()

    def search_data(self):
        self.search_data_window = QtWidgets.QMainWindow()
        self.ui = search()
        self.ui.setupUi(self.search_data_window)
        self.search_data_window.show()
       

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main-InfluBusiness"))
        self.title_label.setText(_translate("MainWindow", "InfluBusiness"))

        #row head
        for row in range(len(self.data)):
            item = self.tableWidget.verticalHeaderItem(row)
            item.setText(_translate("MainWindow", str(row+1)))
        
        #column head
        item = self.tableWidget.horizontalHeaderItem(0) 
        item.setText(_translate("MainWindow", "Id influencer"))
        item = self.tableWidget.horizontalHeaderItem(1) 
        item.setText(_translate("MainWindow", "Name influencer"))
        item = self.tableWidget.horizontalHeaderItem(2) 
        item.setText(_translate("MainWindow", "Sector"))
        item = self.tableWidget.horizontalHeaderItem(3) 
        item.setText(_translate("MainWindow", "Remuneration"))
        
        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        
        #items

        print(self.data)
        for row in range(len(self.data)):
            for column in range(len(self.data.columns)):
                if (column==0 or column==3):
                    item = self.tableWidget.item(row, column)
                    self.tableWidget.setItem(row,column, item)
                    item.setText(_translate("MainWindow",str(self.data.iloc[row,column])))
                else:
                    item = self.tableWidget.item(row, column)
                    self.tableWidget.setItem(row,column, item)
                    item.setText(_translate("MainWindow",self.data.iloc[row,column]))

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Add influencer"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete influencer"))
        self.pushButton_3.setText(_translate("MainWindow", "Price quotation"))
        self.pushButton_4.setText(_translate("MainWindow", "Reload"))
        self.pushButton.clicked.connect(self.add_data)
        self.pushButton_2.clicked.connect(self.delete_data)
        self.pushButton_3.clicked.connect(self.search_data)
        self.pushButton_4.clicked.connect(self.update_data)
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    input()
        
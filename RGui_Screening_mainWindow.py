# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RGui_Screening_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScreeningSys_mainWindow(object):
    def setupUi(self, ScreeningSys_mainWindow):
        ScreeningSys_mainWindow.setObjectName("ScreeningSys_mainWindow")
        ScreeningSys_mainWindow.resize(910, 1143)
        self.centralwidget = QtWidgets.QWidget(ScreeningSys_mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        ScreeningSys_mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ScreeningSys_mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTemplate_File = QtWidgets.QMenu(self.menuFile)
        self.menuTemplate_File.setObjectName("menuTemplate_File")
        self.menuData_File = QtWidgets.QMenu(self.menuFile)
        self.menuData_File.setObjectName("menuData_File")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHardware = QtWidgets.QMenu(self.menuOptions)
        self.menuHardware.setObjectName("menuHardware")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuReport = QtWidgets.QMenu(self.menubar)
        self.menuReport.setObjectName("menuReport")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        ScreeningSys_mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ScreeningSys_mainWindow)
        self.statusbar.setObjectName("statusbar")
        ScreeningSys_mainWindow.setStatusBar(self.statusbar)
        self.actionPrint = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrinter_Setup = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionPrinter_Setup.setObjectName("actionPrinter_Setup")
        self.actionExit = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSet_Path = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionSet_Path.setObjectName("actionSet_Path")
        self.actionSample_Data_Viewing = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionSample_Data_Viewing.setObjectName("actionSample_Data_Viewing")
        self.actionSample_Search = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionSample_Search.setObjectName("actionSample_Search")
        self.actionUser_Guide = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionUser_Guide.setObjectName("actionUser_Guide")
        self.actionAbout = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAdd_New_Tempate_File = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionAdd_New_Tempate_File.setObjectName("actionAdd_New_Tempate_File")
        self.actionOpen_Template_File = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionOpen_Template_File.setObjectName("actionOpen_Template_File")
        self.actionDupplicate_a_Template_File = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionDupplicate_a_Template_File.setObjectName("actionDupplicate_a_Template_File")
        self.actionAdd_New_Date_File = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionAdd_New_Date_File.setObjectName("actionAdd_New_Date_File")
        self.actionOpen_Date_File = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionOpen_Date_File.setObjectName("actionOpen_Date_File")
        self.actionConverting_Final_Screening_Data_to_excel_Format = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionConverting_Final_Screening_Data_to_excel_Format.setObjectName("actionConverting_Final_Screening_Data_to_excel_Format")
        self.actionBarcode_Config = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionBarcode_Config.setObjectName("actionBarcode_Config")
        self.actionBK_Power_Bank_Config = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionBK_Power_Bank_Config.setObjectName("actionBK_Power_Bank_Config")
        self.actionView_All_Report_And_Graph = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionView_All_Report_And_Graph.setObjectName("actionView_All_Report_And_Graph")
        self.actionRaw_Data_Table = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionRaw_Data_Table.setObjectName("actionRaw_Data_Table")
        self.actionFront_Page = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionFront_Page.setObjectName("actionFront_Page")
        self.actionPrint_All_Peport_And_Graph = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionPrint_All_Peport_And_Graph.setObjectName("actionPrint_All_Peport_And_Graph")
        self.actionUser_Gulid = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionUser_Gulid.setObjectName("actionUser_Gulid")
        self.actionAbout_2 = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionPost_Graph = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionPost_Graph.setObjectName("actionPost_Graph")
        self.actionPre_Graph = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionPre_Graph.setObjectName("actionPre_Graph")
        self.actionPre_Graph_2 = QtWidgets.QAction(ScreeningSys_mainWindow)
        self.actionPre_Graph_2.setObjectName("actionPre_Graph_2")
        self.menuTemplate_File.addAction(self.actionAdd_New_Tempate_File)
        self.menuTemplate_File.addAction(self.actionOpen_Template_File)
        self.menuTemplate_File.addAction(self.actionDupplicate_a_Template_File)
        self.menuData_File.addAction(self.actionAdd_New_Date_File)
        self.menuData_File.addAction(self.actionOpen_Date_File)
        self.menuData_File.addAction(self.actionConverting_Final_Screening_Data_to_excel_Format)
        self.menuFile.addAction(self.menuTemplate_File.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuData_File.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHardware.addAction(self.actionBarcode_Config)
        self.menuHardware.addAction(self.actionBK_Power_Bank_Config)
        self.menuOptions.addAction(self.menuHardware.menuAction())
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionSet_Path)
        self.menuAnalysis.addAction(self.actionSample_Data_Viewing)
        self.menuAnalysis.addAction(self.actionSample_Search)
        self.menuReport.addAction(self.actionView_All_Report_And_Graph)
        self.menuReport.addSeparator()
        self.menuReport.addAction(self.actionPrint_All_Peport_And_Graph)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(ScreeningSys_mainWindow)
        QtCore.QMetaObject.connectSlotsByName(ScreeningSys_mainWindow)

    def retranslateUi(self, ScreeningSys_mainWindow):
        _translate = QtCore.QCoreApplication.translate
        ScreeningSys_mainWindow.setWindowTitle(_translate("ScreeningSys_mainWindow", "BTC-Screening System"))
        self.menuFile.setTitle(_translate("ScreeningSys_mainWindow", "File"))
        self.menuTemplate_File.setTitle(_translate("ScreeningSys_mainWindow", "Template File"))
        self.menuData_File.setTitle(_translate("ScreeningSys_mainWindow", "Data File"))
        self.menuOptions.setTitle(_translate("ScreeningSys_mainWindow", "Options"))
        self.menuHardware.setTitle(_translate("ScreeningSys_mainWindow", "Hardware"))
        self.menuAnalysis.setTitle(_translate("ScreeningSys_mainWindow", "Analysis"))
        self.menuReport.setTitle(_translate("ScreeningSys_mainWindow", "Report"))
        self.menuHelp.setTitle(_translate("ScreeningSys_mainWindow", "Help"))
        self.menuAbout.setTitle(_translate("ScreeningSys_mainWindow", "About"))
        self.actionPrint.setText(_translate("ScreeningSys_mainWindow", "Print"))
        self.actionPrinter_Setup.setText(_translate("ScreeningSys_mainWindow", "Printer Setup"))
        self.actionExit.setText(_translate("ScreeningSys_mainWindow", "Exit"))
        self.actionSet_Path.setText(_translate("ScreeningSys_mainWindow", "Set Path"))
        self.actionSample_Data_Viewing.setText(_translate("ScreeningSys_mainWindow", "Sample Data Viewing"))
        self.actionSample_Search.setText(_translate("ScreeningSys_mainWindow", "Sample Search"))
        self.actionUser_Guide.setText(_translate("ScreeningSys_mainWindow", "Pre-Graph"))
        self.actionAbout.setText(_translate("ScreeningSys_mainWindow", "Post-Graph"))
        self.actionAdd_New_Tempate_File.setText(_translate("ScreeningSys_mainWindow", "Add New Tempate File"))
        self.actionOpen_Template_File.setText(_translate("ScreeningSys_mainWindow", "Open Template File"))
        self.actionDupplicate_a_Template_File.setText(_translate("ScreeningSys_mainWindow", "Duplicate a Template File"))
        self.actionAdd_New_Date_File.setText(_translate("ScreeningSys_mainWindow", "Add New Data File"))
        self.actionOpen_Date_File.setText(_translate("ScreeningSys_mainWindow", "Open Data File"))
        self.actionConverting_Final_Screening_Data_to_excel_Format.setText(_translate("ScreeningSys_mainWindow", "Converting Final Screening Data to excel Format"))
        self.actionBarcode_Config.setText(_translate("ScreeningSys_mainWindow", "Barcode Config."))
        self.actionBK_Power_Bank_Config.setText(_translate("ScreeningSys_mainWindow", "BK-Power Bank Config."))
        self.actionView_All_Report_And_Graph.setText(_translate("ScreeningSys_mainWindow", "View All Report And Graph"))
        self.actionRaw_Data_Table.setText(_translate("ScreeningSys_mainWindow", "Raw Data Table"))
        self.actionFront_Page.setText(_translate("ScreeningSys_mainWindow", "Front Page"))
        self.actionPrint_All_Peport_And_Graph.setText(_translate("ScreeningSys_mainWindow", "Print All Peport And Graph"))
        self.actionUser_Gulid.setText(_translate("ScreeningSys_mainWindow", "User Guide"))
        self.actionAbout_2.setText(_translate("ScreeningSys_mainWindow", "About"))
        self.actionPost_Graph.setText(_translate("ScreeningSys_mainWindow", "Post-Graph"))
        self.actionPre_Graph.setText(_translate("ScreeningSys_mainWindow", "Pre-Graph"))
        self.actionPre_Graph_2.setText(_translate("ScreeningSys_mainWindow", "Pre-Graph"))

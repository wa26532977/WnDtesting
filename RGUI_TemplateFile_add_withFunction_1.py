import pyodbc
import datetime
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import mysql.connector

pd.options.display.max_columns = 999
pd.options.display.max_rows = 999
pd.set_option("display.precision", 6)


class NewTemplateAdd(QDialog):
    def __init__(self):
        super(NewTemplateAdd, self).__init__()
        loadUi("RGui_TemplateFile_add.ui", self)
        self.tabWidget.setCurrentIndex(0)
        # self.lineEdit_1.returnPressed.connect(self.search_radley)
        self.lineEdit_1.editingFinished.connect(self.search_radley)
        self.pushButton.clicked.connect(self.cancel_button)
        self.pushButton_5.clicked.connect(self.cancel_button)
        self.pushButton_7.clicked.connect(self.cancel_button)
        self.pushButton_2.clicked.connect(self.save_button)
        self.pushButton_6.clicked.connect(self.save_button)
        self.pushButton_8.clicked.connect(self.save_button)
        self.cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="weightanddimensions")
        self.mycursor = self.cnx.cursor(dictionary=True)

    def duplicate_number(self, test):
        self.set_header(test)
        self.lineEdit_2.setText("")

    def save_button_pre_check(self):
        if str(self.lineEdit_2.text()) == "" or str(self.lineEdit_1.text()) == "":
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setText("A Lot number and Test No. is Required")
            msgbox.exec()
            return False
        # fix this to dupicated lot no.
        if self.label.text() == "Lot No.":
            test_no = self.lineEdit_2.text()
            self.mycursor.execute("select count(*) as count from header where Test_number like %s", (test_no,))
            for db in self.mycursor:
                if db["count"] != 0:
                    msgbox = QtWidgets.QMessageBox(self)
                    msgbox.setText("Please enter a new test number")
                    msgbox.exec()
                    return False
        return True

    def set_header(self, x):
        self.mycursor.execute("select * from header where test_number=%s ", (x,))
        all_item = []
        for i in self.mycursor:
            all_item = [value if value is not None else "" for key, value in i.items()]
        gui_ids = (1, 2, 3, 4, 5, 6, 7, 8, 10, 16, 18, 11, 12, 13, 15, 14, 20, 21, 22, 23, 17)
        for key, value in enumerate(gui_ids):
            set_each_line = "self.lineEdit_" + str(value) + ".setText('" + str(all_item[key]) + "')"
            exec(set_each_line)
        # set the button
        if all_item[21] == "Cell":
            self.radioButton_2.setChecked(True)
        elif all_item[21] == "Battery":
            self.radioButton.setChecked(True)
        # set note
        self.plainTextEdit.setPlainText(all_item[22])

    def save_button(self):
        my_header_info = []
        gui_ids = (1, 2, 3, 4, 5, 6, 7, 8, 10, 16, 18, 11, 12, 13, 15, 14, 20, 21, 22, 23, 17)
        if self.save_button_pre_check():
            # save all files
            for ids in gui_ids:
                # this is for int variables in database
                add_header = "my_header_info.append(self.lineEdit_" + str(ids) + ".text())"
                exec(add_header)
            my_header_info = [x if x != "" else None for x in my_header_info]
            # append button
            if self.radioButton.isChecked():
                my_header_info.append("Battery")
            elif self.radioButton_2.isChecked():
                my_header_info.append("Cell")
            else:
                my_header_info.append(None)
            # append note
            my_header_info.append(self.plainTextEdit.toPlainText())
            print(my_header_info)
            self.mycursor.execute("INSERT INTO header (lot_number, test_number, screen_file_name, sample_name, "
                                  "chemistry, transmittal_number, project_number, project_engineer, test_purpose, "
                                  "finished_date, cell_load, sample_size, date_made, date_received, date_storage_start,"
                                  " date_storage_stop, storage_temp, date_on_drain_start, date_on_drain_stop, "
                                  "on_drain_temp, total_sample_to_be_screened, battery_cell, note) "
                                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                                  "%s, %s, %s, %s, %s, %s, %s)", my_header_info)
            self.cnx.commit()
            self.close()

    def cancel_button(self):
        self.close()

    def search_radley(self):
        constr = 'DRIVER={SQL Server};SERVER=BTC-SQL2016\\BTCSQL2016;DATABASE=RADLEY_PROD;Trusted_Connection=Yes'
        con = pyodbc.connect(constr)
        query = "SELECT XLSM_LOT as [Lot], " + \
                "XIM_ITEM as [Item], " + \
                "XEF_USER_CHAR1 as [Manufacturer], " + \
                "XIC_NAME as [Chemistry], " + \
                "XPT_NAME as [Form Factor], " + \
                "XIT_NAME as [Type], " + \
                "XIM_GRADE as [Nominal Capacity], " + \
                "XIM_UPC_CODE as [Nominal Voltage], " + \
                "XIM_HEIGHT as [Height], " + \
                "XIM_WIDTH as [Width], " + \
                "XIM_DEPTH as [Depth], " + \
                "XIM_WEIGHT as [Weight], " + \
                "XIM_DIAMETER as [Diameter], " + \
                "XLSM_RECEIPT_DATE as [Receipt Date], " + \
                "XLSM_MFG_DATE as [Mfg Date] " + \
                "FROM XINV_LOT_SERIAL_MASTER " + \
                "JOIN XINV_ITEM_MASTER ON XLSM_ITEM_ID = XIM_ID " + \
                "JOIN XINV_ITEM_CLASS ON XIM_CLASS_ID = XIC_ID " + \
                "JOIN XAS_EXTENDED_FIELD ON XIM_EXTENDED_FIELD_ID = XEF_ID " + \
                "LEFT JOIN XINV_PACKAGE_TYPE ON XIM_PACKAGE_TYPE_ID = XPT_ID " + \
                "LEFT JOIN XINV_ITEM_TYPE ON XIM_TYPE_ID = XIT_ID "
        query += "WHERE XLSM_LOT = '" + str(self.lineEdit_1.text()) + "' "
        print(str(self.lineEdit_1.text()))
        df = pd.read_sql_query(query, con)
        print("DF = ")
        print(df)
        if df.empty:
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setText("Can't find this lot number, please check.")
            msgbox.exec()
            return
        if df.iloc[0]["Diameter"] is not None:
            self.lineEdit_11.setText(str(df.iloc[0]["Height"]) + "(H) X " + str(df.iloc[0]["Diameter"]) + "(D)")
        elif df.iloc[0]["Width"] is not None:
            self.lineEdit_11.setText(str(df.iloc[0]["Height"]) + "(H) X" + str(df.iloc[0]["Width"]) + "(W) X" + str(
                df.iloc[0]["Depth"]) + "(D)")
        self.lineEdit_20.setText("24")
        self.lineEdit_23.setText("24")
        self.lineEdit_5.setText(str(df.iloc[0]["Chemistry"]))
        self.lineEdit_12.setText(str(df.iloc[0]["Mfg Date"])[0:10])
        self.lineEdit_13.setText(str(df.iloc[0]["Receipt Date"])[0:10])
        # set sample name
        self.lineEdit_4.setText(str(df.iloc[0]["Manufacturer"]) + " " + str(df.iloc[0]["Item"]))
        # set finished date as today
        self.lineEdit_16.setText(str(datetime.date.today()))
        # self.lineEdit_5.setText(str(df.iloc[0]["Form Factor"]) + " " + str(df.iloc[0]["Type"]))
        # self.lineEdit_6.setText(str(df.iloc[0]["Nominal Capacity"]))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = NewTemplateAdd()
    qt_app.set_header("test1")
    # qt_app.getTestNumber2("14575A00.txt")
    qt_app.show()
    sys._excepthook = sys.excepthook


    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys.excepthook(exctype, value, traceback)
        sys.exit(1)


    sys.excepthook = exception_hook

    app.exec_()

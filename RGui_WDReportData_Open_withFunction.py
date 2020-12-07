import os
import pyodbc
import datetime
import pandas as pd
import math
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from Screening_System_PyQt5 import client
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from scipy import stats
from docx import Document
import docx
import mysql.connector

pd.options.display.max_columns = 999
pd.options.display.max_rows = 999
pd.set_option("display.precision", 6)


class WDReportDataWithFunction(QDialog):
    def __init__(self, week_name="14567A01-W00"):
        super(WDReportDataWithFunction, self).__init__()
        loadUi("RGui_WND_ReportData.ui", self)
        self.week_name = week_name
        self.cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="weightanddimensions")
        self.mycursor = self.cnx.cursor(dictionary=True)
        self.mycursor.execute("select * from cells where week_name = %s", (str(self.week_name),))
        self.allItem = [x for x in self.mycursor]
        self.label_4.setText(self.week_name)
        self.populate_data_table()

    def populate_data_table(self):
        self.label_10.setText(str(len(self.allItem)))
        self.tableWidget.setRowCount(len(self.allItem))
        for index, value in enumerate(self.allItem):
            # this remove the None
            new_value = {}
            for k, v in value.items():
                if v is None:
                    v = ""
                new_value[k] = v

            print(new_value)
            self.tableWidget.setItem(index, 0, QTableWidgetItem(str(index+1)))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(new_value["sample_barcode"])))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(str(new_value["Manufacture_Serial_Number"])))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(str(new_value["weight"])))
            self.tableWidget.setItem(index, 4, QTableWidgetItem(str(new_value["off_drain_weight"])))
            self.tableWidget.setItem(index, 5, QTableWidgetItem(
                str(self.calculate_differ(new_value["weight"], new_value["off_drain_weight"]))))
            self.tableWidget.setItem(index, 6, QTableWidgetItem(
                str(self.calculate_percentDiffer(new_value["weight"], new_value["off_drain_weight"]))))
            self.tableWidget.setItem(index, 7, QTableWidgetItem(str(new_value["height"])))
            self.tableWidget.setItem(index, 8, QTableWidgetItem(str(new_value["off_drain_height"])))
            self.tableWidget.setItem(index, 9, QTableWidgetItem(
                str(self.calculate_differ(new_value["height"], new_value["off_drain_height"]))))
            self.tableWidget.setItem(index, 10, QTableWidgetItem(
                str(self.calculate_percentDiffer(new_value["height"], new_value["off_drain_height"]))))
            self.tableWidget.setItem(index, 11, QTableWidgetItem(str(new_value["width"])))
            self.tableWidget.setItem(index, 12, QTableWidgetItem(str(new_value["off_drain_width"])))
            self.tableWidget.setItem(index, 13, QTableWidgetItem(
                str(self.calculate_differ(new_value["width"], new_value["off_drain_width"]))))
            self.tableWidget.setItem(index, 14, QTableWidgetItem(
                str(self.calculate_percentDiffer(new_value["width"], new_value["off_drain_width"]))))
            self.tableWidget.setItem(index, 15, QTableWidgetItem(str(new_value["thickness"])))
            self.tableWidget.setItem(index, 16, QTableWidgetItem(str(new_value["off_drain_thickness"])))
            self.tableWidget.setItem(index, 17, QTableWidgetItem(
                str(self.calculate_differ(new_value["thickness"], new_value["off_drain_thickness"]))))
            self.tableWidget.setItem(index, 18, QTableWidgetItem(
                str(self.calculate_percentDiffer(new_value["thickness"], new_value["off_drain_thickness"]))))

    def calculate_differ(self, value_1, value_2):
        if value_1 == "" or value_2 == "":
            return ""
        else:
            return round((value_2-value_1), 3)

    def calculate_percentDiffer(self, value_1, value_2):
        if value_1 == "" or value_2 == "":
            return ""
        else:
            print(value_1, value_2)
            return round(((value_2-value_1)/value_1)*100, 3)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = WDReportDataWithFunction(week_name="14567A01-W00")
    # qt_app.getTestNumber("14665A01.txt")
    # qt_app.getTestNumber2("14575A00.txt")
    qt_app.show()
    sys._excepthook = sys.excepthook


    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys.excepthook(exctype, value, traceback)
        sys.exit(1)


    sys.excepthook = exception_hook

    app.exec_()
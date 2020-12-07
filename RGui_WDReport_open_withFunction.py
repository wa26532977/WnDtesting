import pandas as pd
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi
from WeightAndDimensionSystem import RGui_WDReportData_Open_withFunction
import mysql.connector

pd.options.display.max_columns = 999
pd.options.display.max_rows = 999
pd.set_option("display.precision", 6)


class WDReportOpenWithFunction(QDialog):
    def __init__(self, duplicated="No"):
        super(WDReportOpenWithFunction, self).__init__()
        loadUi("RGui_WDReport_Open.ui", self)
        self.cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="weightanddimensions")
        self.mycursor = self.cnx.cursor()
        self.mycursor.execute("select week_name from cells group by week_name")
        self.allItem = [x[0] for x in self.mycursor]
        self.populate_list_widget()
        self.lineEdit.textChanged.connect(self.search_in_list)
        self.listWidget.itemClicked.connect(self.item_clicked)
        self.pushButton_2.clicked.connect(self.ok_pressed)

    def populate_list_widget(self):
        self.listWidget.clear()
        for i in self.allItem:
            self.listWidget.addItem(i)
        if self.listWidget.count() == 1:
            self.listWidget.setCurrentRow(0)
            print(self.listWidget.currentItem().text())

    def search_in_list(self):
        search = self.lineEdit.text()
        self.listWidget.clear()
        if search == "":
            self.populate_list_widget()
        else:
            for i in self.allItem:
                if search in i:
                    self.listWidget.addItem(i)
        # highlight the item when list size is 1
        if self.listWidget.count() == 1:
            self.listWidget.setCurrentRow(0)

    def item_clicked(self):
        search = self.listWidget.currentItem().text()
        self.lineEdit.setText(search)

    def ok_pressed(self):
        while self.listWidget.currentItem() is None:
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setText("No item is selected, please select an item.")
            msgbox.exec()
            return
        ui = RGui_WDReportData_Open_withFunction.WDReportDataWithFunction(
            week_name=str(self.listWidget.currentItem().text()))
        self.close()
        ui.show()
        ui.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = WDReportOpenWithFunction()
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

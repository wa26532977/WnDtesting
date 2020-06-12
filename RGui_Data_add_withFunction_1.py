import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi
from WeightAndDimensionSystem import RGUI_TemplateFile_add_withFunction_1
import mysql.connector


class DataAddWithFunctions(QDialog):
    def __init__(self):
        super(DataAddWithFunctions, self).__init__()
        loadUi("RGui_Data_add.ui", self)
        self.cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="weightanddimensions")
        self.mycursor = self.cnx.cursor()
        self.mycursor.execute("select test_number from header")
        self.allItem = [x[0] for x in self.mycursor]
        self.populate_list_widget()
        self.lineEdit.textChanged.connect(self.search_in_list)
        self.listWidget.itemClicked.connect(self.item_clicked)
        self.pushButton_2.clicked.connect(self.OK_pressed)

    def populate_list_widget(self):
        self.listWidget.clear()
        for i in self.allItem:
            self.listWidget.addItem(i)
        if self.listWidget.count() == 1:
            self.listWidget.setCurrentRow(0)
            print(self.listWidget.currentItem().text())

    def search_in_list(self):
        search = self.lineEdit.text()
        if search == "":
            self.lineEdit_2.setText("")
            self.populate_list_widget()
        elif "W" in search or "M" in search or "-" in search:
            pass
        else:
            self.listWidget.clear()
            self.lineEdit_2.setText(search)
            for i in self.allItem:
                if search in i:
                    self.listWidget.addItem(i)
            # highlight the item when list size is 1
            if self.listWidget.count() == 1:
                self.listWidget.setCurrentRow(0)
                self.lineEdit_2.setText(search)


    def item_clicked(self):
        search = self.listWidget.currentItem().text()
        self.lineEdit.setText(search)
        self.lineEdit_2.setText(search)

    def OK_pressed(self):
        # change this to start measureing
        ui = RGUI_TemplateFile_add_withFunction_1.NewTemplateAdd()
        while self.listWidget.currentItem() is None:
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setText("No item is selected, please select an item.")
            msgbox.exec()
            return
        if self.duplicated == "Yes":
            ui.duplicate_number(self.listWidget.currentItem().text())
        else:
            ui.set_header(self.listWidget.currentItem().text())
        self.close()
        ui.show()
        ui.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = DataAddWithFunctions()
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
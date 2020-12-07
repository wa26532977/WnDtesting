from PyQt5 import QtWidgets
import sys
import pandas as pd
from WeightAndDimensionSystem import RGui_WeightAndDimension_mainWindow
from WeightAndDimensionSystem import RGUI_TemplateFile_add_withFunction_1
from WeightAndDimensionSystem import RGui_TemplateFile_open_withFunction_1
from WeightAndDimensionSystem import RGui_Data_add_withFunction_1
from WeightAndDimensionSystem import RGui_WDReport_open_withFunction


pd.options.display.max_columns = 999
pd.options.display.max_rows = 999
pd.set_option("display.precision", 6)


class WNDApp1(RGui_WeightAndDimension_mainWindow.Ui_WeightSys_mainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(WNDApp1, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.actionAdd_New_Tempate_File.triggered.connect(self.create_new_template)
        self.actionOpen_Template_File.triggered.connect(self.open_template_file)
        self.actionDupplicate_a_Template_File.triggered.connect(self.dupplicate_temple)
        self.actionAdd_New_Date_File.triggered.connect(self.add_new_datafile)
        self.actionOpen_Report.triggered.connect(self.open_report)

    def open_report(self):
        ui = RGui_WDReport_open_withFunction.WDReportOpenWithFunction()
        ui.show()
        ui.exec_()

    def add_new_datafile(self):
        ui = RGui_Data_add_withFunction_1.DataAddWithFunctions()
        ui.show()
        ui.exec_()

    def dupplicate_temple(self):
        ui = RGui_TemplateFile_open_withFunction_1.TemplateFileOpenWithFunction(duplicated="Yes")
        ui.show()
        ui.exec_()

    def create_new_template(self):
        ui = RGUI_TemplateFile_add_withFunction_1.NewTemplateAdd()
        ui.show()
        ui.exec_()

    def open_template_file(self):
        ui = RGui_TemplateFile_open_withFunction_1.TemplateFileOpenWithFunction()
        ui.show()
        ui.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = WNDApp1()
    qt_app.show()
    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys.excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook

    app.exec_()
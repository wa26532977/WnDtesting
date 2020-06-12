import sys
import datetime
import math
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import mysql.connector
import serial


class WNDDataCollectionWithFunctions(QDialog):

    def __init__(self, post="false", test_name="test1", template_name="template1"):
        super(WNDDataCollectionWithFunctions, self).__init__()
        loadUi("RGui_Screening_DataCollection.ui", self)
        self.post = post
        self.test_name = test_name
        self.template_name = template_name
        self.cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="weightanddimensions")
        self.mycursor = self.cnx.cursor(dictionary=True)
        self.set_test_number()
        self.lineEdit_1.returnPressed.connect(self.scan_barcode_check)
        self.lineEdit_2.returnPressed.connect(self.sample_sn)
        self.lineEdit_7.returnPressed.connect(self.manufacture_sn)
        self.lineEdit_3.returnPressed.connect(self.get_weight)
        self.lineEdit_3.returnPressed.connect(self.get_height)

    def get_height(self):
        self.lineEdit_4.setFocus()

    def get_weight(self):
        try:
            ser = serial.Serial('COM3', baudrate=9600, timeout=0.020, parity=serial.PARITY_EVEN, bytesize=serial.SEVENBITS, stopbits=1)
        except serial.SerialException:
            print("not found")
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setText("The COM4 port is not found, please check!")
            msgbox.exec()
        else:
            transmit = "SEND \r"
            sizeof = ser.write(transmit.encode('ascii'))
            while 1:
                data = ser.readline()
                print(data)
                if data != b'':
                    rxdata = data.decode('ascii')
                    rxdata = rxdata.split()
                    print(rxdata)
                    try:
                        changeToFloat = float(rxdata[0])
                    except:
                        print("geting again")
                    else:
                        print(rxdata)
                        self.lineEdit_4.setText(str(rxdata[0]))
                        self.lineEdit_4.setFocus()
                        break


    def manufacture_sn(self):
        self.lineEdit_3.setText(str(datetime.date.today()))
        self.lineEdit_3.setFocus()

    def sample_sn(self):
        self.lineEdit_7.setFocus()

    def check_duplicated_barcode(self):
        barcode = self.lineEdit_1.text()
        if self.post == "false":
            self.mycursor.execute("select count(*) as count from cells where sample_barcode = %s", (barcode,))
            for db in self.mycursor:
                if db["count"] != 0:
                    msgbox = QtWidgets.QMessageBox(self)
                    msgbox.setText(
                        f"{barcode} already has weight and dimensions value for pre-drain in {self.label_1.text()} ")
                    msgbox.exec()
                    return False
        else:
            self.mycursor.execute("select * from cells where sample_barcode = %s", (barcode,))
            for db in self.mycursor:
                if db["off_drain_weight"] is not None or db["off_drain_height"] is not None or \
                        db["off_drain_diameter"] is not None:
                    msgbox = QtWidgets.QMessageBox(self)
                    msgbox.setText(
                        f"{barcode} already has weight and dimensions value for Post-drain in {self.label_1.text()}")
                    msgbox.exec()
                    return False

        return True

    def scan_barcode_check(self):
        if self.check_duplicated_barcode():
            self.lineEdit_2.setFocus()

    def set_test_number(self):
        self.label_1.setText(str(self.test_name))
        self.label_5.setText(str(self.template_name))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = WNDDataCollectionWithFunctions(post="true", test_name="test12", template_name="template1")
    # qt_app.getTestNumber("14665A01.txt")
    # qt_app.getTestNumber2("14575A00.txt")
    qt_app.show()
    app.exec_()
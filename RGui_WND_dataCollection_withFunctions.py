import sys
import datetime
import math
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import mysql.connector
import serial
import time


class WNDDataCollectionWithFunctions(QDialog):

    def __init__(self, post="false", test_name="test1", template_name="template1", size="cylinder"):
        super(WNDDataCollectionWithFunctions, self).__init__()
        loadUi("RGui_Screening_DataCollection.ui", self)
        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer_2 = QtCore.QTimer(self)
        self.checkThreadTimer_3 = QtCore.QTimer(self)
        self.checkThreadTimer_4 = QtCore.QTimer(self)
        self.post = post
        self.test_name = test_name
        self.template_name = template_name
        self.size = size
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
        self.pushButton_3.clicked.connect(self.get_weight)
        self.lineEdit_4.returnPressed.connect(self.get_height)
        self.pushButton_4.clicked.connect(self.get_height)
        self.lineEdit_5.returnPressed.connect(self.get_diameter)
        self.pushButton_5.clicked.connect(self.get_diameter)
        self.lineEdit_8.returnPressed.connect(self.get_thickness)
        self.pushButton_6.clicked.connect(self.get_thickness)
        self.lineEdit_9.returnPressed.connect(self.get_comments)
        self.lineEdit_6.returnPressed.connect(self.high_light_save)
        self.pushButton_2.clicked.connect(self.save_data)

    def save_data(self):
        my_header_info = []
        gui_ids = (1, 2, 7, 3, 4, 5, 8, 6)
        label_ids = (1, 5, 6, 15)
        # save all files
        for ids in gui_ids:
            # this is for int variables in database
            add_header = "my_header_info.append(self.lineEdit_" + str(ids) + ".text())"
            exec(add_header)
        for ids in label_ids:
            if ids == 6:
                # this is the note, it has two label
                my_header_info.append(self.label_6.text() + ", " + self.label_31.text())
            else:
                add_header = "my_header_info.append(self.label_" + str(ids) + ".text())"
                exec(add_header)

        my_header_info = [x if x != "" else None for x in my_header_info]
        print(my_header_info)

    def get_comments(self):
        self.checkThreadTimer_4.stop()
        self.lineEdit_6.setFocus()

    def high_light_save(self):
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFocus()

    def get_thickness(self):
        self.checkThreadTimer_3.stop()
        if self.size == "cylinder":
            self.lineEdit_6.setFocus()
        else:
            self.lineEdit_9.setFocus()
            self.checkThreadTimer_4.timeout.connect(self.read_thickness_data)
            self.checkThreadTimer_4.start(350)

    def read_thickness_data(self):
        ser = serial.Serial('COM4', baudrate=2400, timeout=0.2)
        ser.write(b'x01')
        data = ser.readline()
        try:
            print("read_height_data")
            print(data.decode("ascii"))
            self.lineEdit_9.setText(str(data.decode("ascii").split('+')[1][:-1]))
        except:
            print("not working")
        ser.close()

    def get_diameter(self):
        self.checkThreadTimer_2.stop()
        self.lineEdit_8.setFocus()
        self.checkThreadTimer_3.timeout.connect(self.read_diameter_data)
        self.checkThreadTimer_3.start(350)

    def read_diameter_data(self):
        ser = serial.Serial('COM4', baudrate=2400, timeout=0.2)
        ser.write(b'x01')
        data = ser.readline()
        try:
            print("read_height_data")
            print(data.decode("ascii"))
            self.lineEdit_8.setText(str(data.decode("ascii").split('+')[1][:-1]))
        except:
            print("not working")
        ser.close()

    def get_height(self):
        self.checkThreadTimer.stop()
        print("get Hight")
        self.lineEdit_5.setFocus()
        self.checkThreadTimer_2.timeout.connect(self.read_height_data)
        self.checkThreadTimer_2.start(350)

    def read_height_data(self):
        print("getting data")
        ser = serial.Serial('COM4', baudrate=2400, timeout=0.2)
        ser.write(b'x01')
        data = ser.readline()
        try:
            print("read_height_data")
            print(data.decode("ascii"))
            self.lineEdit_5.setText(str(data.decode("ascii").split('+')[1][:-1]))
        except:
            print("not working")
        ser.close()

    def get_weight(self):
        self.checkThreadTimer.timeout.connect(self.get_weight_data)
        self.checkThreadTimer.start(350)

    def get_weight_data(self):
        ser = serial.Serial('COM3', baudrate=9600, timeout=0.020, parity=serial.PARITY_EVEN,
                            bytesize=serial.SEVENBITS, stopbits=1)
        transmit = "SEND \r"
        ser.write(transmit.encode('ascii'))
        data = ser.readline()
        try:
            print("read_weight_data")
            rxdata = data.decode('ascii').split()
            changetofloat = float(rxdata[0])
        except:
            print("getting again")
        else:
            if data == b'':
                ser.close()
            else:
                print(rxdata)
                self.lineEdit_4.setText(str(changetofloat))
                self.lineEdit_4.setFocus()
                ser.close()

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

            self.mycursor.execute("select count(*) as count from cells where sample_barcode = %s", (barcode,))
            for db in self.mycursor:
                if db["count"] != 1:
                    msgbox = QtWidgets.QMessageBox(self)
                    msgbox.setText(
                        f"{barcode} has no pre value of the test {self.label_1.text()} ")
                    msgbox.exec()
                    return False

            self.mycursor.execute("select * from cells where sample_barcode = %s", (barcode,))
            for db in self.mycursor:
                print("happy")
                print(db)
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
        self.label_5.setText(str(self.template_name))
        self.label_1.setText(str(self.test_name))
        if self.post != "false":
            self.label_12.setText("POST ")
        if self.size == "cylinder":
            self.label_38.setText("Diameter")
            self.pushButton_5.setText("Take Diameter")
            self.label_39.setText("")
            self.lineEdit_9.setEnabled(False)
            self.pushButton_6.setText("")
            self.pushButton_6.setEnabled(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = WNDDataCollectionWithFunctions(post="true", test_name="test12", template_name="template1", size='cylinder')
    # qt_app.getTestNumber("14665A01.txt")
    # qt_app.getTestNumber2("14575A00.txt")
    qt_app.show()
    app.exec_()
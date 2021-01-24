# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableWidgetItem
import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets


class Data_Speed_Window(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 437)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 601, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Unit")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 0, 381, 73))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBoxselect = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBoxselect.setObjectName("comboBoxselect")
        self.comboBoxselect.addItem("")
        self.comboBoxselect.addItem("")
        self.comboBoxselect.addItem("")
        self.comboBoxselect.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxselect)
        self.selectsubmitbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.selectsubmitbutton.setObjectName("selectsubmitbutton")
        self.horizontalLayout.addWidget(self.selectsubmitbutton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 191, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditsearch = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEditsearch.setObjectName("lineEditsearch")
        self.horizontalLayout_2.addWidget(self.lineEditsearch)
        self.pushButtonsearch = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonsearch.setFont(font)
        self.pushButtonsearch.setObjectName("pushButtonsearch")
        self.horizontalLayout_2.addWidget(self.pushButtonsearch)

        self.itemset_header(Form)
        self.comboBoxselect.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def itemset_header(self, Form):
        """
        :return: Header Items
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Speedtablesorting"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Upload speed"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Unit"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Download speed"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Provider"))

        self.comboBoxselect.setItemText(0, _translate("Form", "Upload speed"))
        self.comboBoxselect.setItemText(1, _translate("Form", "Download speed"))
        self.comboBoxselect.setItemText(2, _translate("Form", "Provider"))
        self.selectsubmitbutton.setText(_translate("Form", "sort"))
        self.pushButtonsearch.setText(_translate("Form", "search"))

        self.loaddata()
        self.pushButtonsearch.clicked.connect(self.Tosearch)
        self.selectsubmitbutton.clicked.connect(self.Tosort)

    ######## To Load the Data from CSV  File #####################
    def loaddata(self):
        """
        To Load the Data from CSV  File
        :return: Csv data uploaded to Table widget
        """
        ruta = "csvgenerated_speed_data.csv"
        infile = open(ruta, "r")
        next(infile)
        lines = infile.readlines()
        # next(lines)
        infile.close()
        self.tableWidget.setRowCount(len(lines))
        for i in range(0, len(lines)):
            tokens = lines[i].strip().split(",")
            uploadspd = QTableWidgetItem(tokens[0])
            uploadunit = QTableWidgetItem(tokens[1])
            downloadspd = QTableWidgetItem(tokens[2])
            downloadunit = QTableWidgetItem(tokens[3])
            provider = QTableWidgetItem(tokens[4])

            self.tableWidget.setItem(i, 0, uploadspd)
            self.tableWidget.setItem(i, 1, uploadunit)
            self.tableWidget.setItem(i, 2, downloadspd)
            self.tableWidget.setItem(i, 3, downloadunit)
            self.tableWidget.setItem(i, 4, provider)

        self.tableWidget.resizeColumnsToContents()

    def Tosearch(self):
        """
        When Search Button is clicked this Function will be called
        :return: Text in lineedit box from table widget and highlighted the text
        """
        self.searchdata = self.lineEditsearch.text()                              # The text entered in the lineedit box
        items = self.tableWidget.findItems(self.searchdata, QtCore.Qt.MatchContains)     # Find the text in table widget
        brush = QtGui.QBrush(QtGui.QColor("red"))                                     # Highlighted text color
        brush.setStyle(QtCore.Qt.SolidPattern)
        for item in items:
            item.setForeground(brush)

    def Tosort(self):
        """
        When submit button is clicked this function will be called
        :return: Sorted data object according to selected text from combo box
        """
        self.sortdata=self.comboBoxselect.currentText()
        print(self.sortdata)
        ruta = "csvgenerated_speed_data.csv"
        reader = csv.reader(open(ruta), delimiter=',')
        next(reader)
        for row in reader:
            if self.sortdata =="Upload speed":
                self.sortedlist = sorted(reader, key=lambda row: float(row[0]), reverse=True)
            elif self.sortdata == "Download speed":
                self.sortedlist = sorted(reader, key=lambda row: float(row[2]), reverse=True)
            else:
                self.sortedlist = sorted(reader, key=lambda row: row[4], reverse=False)
        print(self.sortedlist)
        self.sorteddatainput()

    def sorteddatainput(self):
        """
        Once data will sorted, this function will be called to upload the sorted data to the table widget
        :return: Updated sorted data
        """
        tablerow = 0
        for row in self.sortedlist:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            tablerow = tablerow+1
            self.tableWidget.resizeColumnsToContents()

if __name__ == "__main__":
    import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QDialog()
dataui = Data_Speed_Window()
dataui.setupUi(window)
window.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")

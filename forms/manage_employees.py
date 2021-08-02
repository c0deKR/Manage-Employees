from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QEvent, Qt, QObject
from forms.new_employee import NewEmployeeDialog
from forms.salary_position import EmployeeInofWindow
from database import Database
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setWindowIcon(QtGui.QIcon('resources/office.png'))
        MainWindow.setStyleSheet("*{\n"
                                 """font: 12pt "MV Boli";;\n"""
                                 """font-size:18px;\n"""
                                 "}\n"
                                 "QPushButton::default{\n"
                                 "    border-style: solid;\n"
                                 "    border-color: #050a0e;\n"
                                 "    border-width: 1px;\n"
                                 "    border-radius: 5px;\n"
                                 "    color: #FFFFFF;\n"
                                 "    padding: 2px;\n"
                                 "    background-color: #151a1e;;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "    border-style: solid;\n"
                                 "    border-color: #050a0e;\n"
                                 "    border-width: 1px;\n"
                                 "    border-radius: 5px;\n"
                                 "    color: #d3dae3;\n"
                                 "    padding: 2px;\n"
                                 "    background-color: #1c1f1f;\n"
                                 "}\n"
                                 "QPushButton:pressed{\n"
                                 "    border-style: solid;\n"
                                 "    border-color: #050a0e;\n"
                                 "    border-width: 1px;\n"
                                 "    border-radius: 5px;\n"
                                 "    color: #d3dae3;\n"
                                 "    padding: 2px;\n"
                                 "    background-color: #2c2f2f;\n"
                                 "}\n"
                                 "QPushButton:disabled{\n"
                                 "    border-style: solid;\n"
                                 "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
                                 "    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
                                 "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
                                 "    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
                                 "    border-width: 1px;\n"
                                 "    border-radius: 5px;\n"
                                 "    color: #808086;\n"
                                 "    padding: 2px;\n"
                                 "    background-color: rgb(142,142,142);\n"
                                 "}\n"
                                 )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.UpperGridLayout = QtWidgets.QGridLayout()
        self.UpperGridLayout.setObjectName("UpperGridLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")

        self.toolButton.setIcon(
            QtGui.QIcon("resources/arrow_ap.png"))
        self.toolButton.setAutoRaise(True)
        self.UpperGridLayout.addWidget(self.toolButton, 0, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(
            688, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.UpperGridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.UpperGridLayout, 0, 0, 1, 1)
        self.FilterWidget = QtWidgets.QWidget(self.centralwidget)
        self.FilterWidget.setObjectName("FilterWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.FilterWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.FirstGridlayout = QtWidgets.QGridLayout()
        self.FirstGridlayout.setObjectName("FirstGridlayout")
        self.IdLabel = QtWidgets.QLabel(self.FilterWidget)
        self.IdLabel.setObjectName("IdLabel")
        self.FirstGridlayout.addWidget(self.IdLabel, 0, 0, 1, 1)
        self.IdEntry = QtWidgets.QLineEdit(self.FilterWidget)
        self.IdEntry.setObjectName("IdEntry")
        self.FirstGridlayout.addWidget(self.IdEntry, 0, 1, 1, 1)
        self.FirstNameLabel = QtWidgets.QLabel(self.FilterWidget)
        self.FirstNameLabel.setObjectName("FirstNameLabel")
        self.FirstGridlayout.addWidget(self.FirstNameLabel, 1, 0, 1, 1)
        self.FirstNameEntry = QtWidgets.QLineEdit(self.FilterWidget)
        self.FirstNameEntry.setObjectName("FirstNameEntry")
        self.FirstGridlayout.addWidget(self.FirstNameEntry, 1, 1, 1, 1)
        self.LastNameLabel = QtWidgets.QLabel(self.FilterWidget)
        self.LastNameLabel.setObjectName("LastNameLabel")
        self.FirstGridlayout.addWidget(self.LastNameLabel, 2, 0, 1, 1)
        self.LastNameEntry = QtWidgets.QLineEdit(self.FilterWidget)
        self.LastNameEntry.setObjectName("LastNameEntry")
        self.FirstGridlayout.addWidget(self.LastNameEntry, 2, 1, 1, 1)
        self.BirthdayLabel = QtWidgets.QLabel(self.FilterWidget)
        self.BirthdayLabel.setObjectName("BirthdayLabel")
        self.FirstGridlayout.addWidget(self.BirthdayLabel, 3, 0, 1, 1)
        self.BirthdayEntry = QtWidgets.QLineEdit(self.FilterWidget)
        self.BirthdayEntry.setObjectName("BirthdayEntry")
        self.FirstGridlayout.addWidget(self.BirthdayEntry, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.FirstGridlayout, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            30, 108, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.SecondGridlayout = QtWidgets.QGridLayout()
        self.SecondGridlayout.setObjectName("SecondGridlayout")
        self.DepartementLabel = QtWidgets.QLabel(self.FilterWidget)
        self.DepartementLabel.setObjectName("DepartementLabel")
        self.SecondGridlayout.addWidget(self.DepartementLabel, 0, 0, 1, 1)
        self.DepartementEntry = QtWidgets.QLineEdit(self.FilterWidget)
        self.DepartementEntry.setObjectName("DepartementEntry")
        self.SecondGridlayout.addWidget(self.DepartementEntry, 0, 1, 1, 1)
        self.SalaryLabel = QtWidgets.QLabel(self.FilterWidget)
        self.SalaryLabel.setObjectName("SalaryLabel")
        self.SecondGridlayout.addWidget(self.SalaryLabel, 1, 0, 1, 1)
        self.SalaryEntry = QtWidgets.QLineEdit(self.FilterWidget)
        self.SalaryEntry.setObjectName("SalaryEntry")
        self.SecondGridlayout.addWidget(self.SalaryEntry, 1, 1, 1, 1)
        self.PositionLabel = QtWidgets.QLabel(self.FilterWidget)
        self.PositionLabel.setObjectName("PositionLabel")
        self.SecondGridlayout.addWidget(self.PositionLabel, 2, 0, 1, 1)
        self.PositionEntry = QtWidgets.QLineEdit(self.FilterWidget)
        self.PositionEntry.setObjectName("PositionEntry")
        self.SecondGridlayout.addWidget(self.PositionEntry, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            288, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.SecondGridlayout.addItem(spacerItem2, 3, 0, 1, 2)
        self.gridLayout_3.addLayout(self.SecondGridlayout, 0, 2, 1, 1)
        self.gridLayout_5.addWidget(self.FilterWidget, 1, 0, 1, 1)

        self.applyRestGridLayout = QtWidgets.QGridLayout()
        self.applyRestGridLayout.setObjectName("applyRestGridLayout")

        self.ApplyButton = QtWidgets.QPushButton(self.FilterWidget)
        self.ApplyButton.setMinimumSize(QtCore.QSize(70, 30))

        self.ApplyButton.setObjectName("ApplyButton")
        self.applyRestGridLayout.addWidget(self.ApplyButton, 0, 1, 1, 1)

        self.ResetButton = QtWidgets.QPushButton(self.FilterWidget)
        self.ResetButton.setMinimumSize(QtCore.QSize(70, 30))
        self.ResetButton.setObjectName("ResetButton")

        self.applyRestGridLayout.addWidget(self.ResetButton, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.applyRestGridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.applyRestGridLayout.addItem(spacerItem4, 0, 3, 1, 1)
        self.gridLayout_5.addLayout(self.applyRestGridLayout, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidget, 3, 0, 1, 1)
        self.LowerGridLayout = QtWidgets.QGridLayout()
        self.LowerGridLayout.setObjectName("LowerGridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(
            536, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LowerGridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setObjectName("BackButton")
        self.LowerGridLayout.addWidget(self.BackButton, 0, 1, 1, 1)
        self.NewButton = QtWidgets.QPushButton(self.centralwidget)
        self.NewButton.setObjectName("NewButton")
        self.LowerGridLayout.addWidget(self.NewButton, 0, 2, 1, 1)
        self.ExportButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExportButton.setObjectName("ExportButton")
        self.LowerGridLayout.addWidget(self.ExportButton, 0, 3, 1, 1)
        self.gridLayout_5.addLayout(self.LowerGridLayout, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manage Employees"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.IdLabel.setText(_translate("MainWindow", "id"))
        self.FirstNameLabel.setText(_translate("MainWindow", "First name"))
        self.LastNameLabel.setText(_translate("MainWindow", "Last name"))
        self.BirthdayLabel.setText(_translate("MainWindow", "birthday"))
        self.DepartementLabel.setText(
            _translate("MainWindow", "departement name"))
        self.SalaryLabel.setText(_translate("MainWindow", "salary"))
        self.PositionLabel.setText(_translate("MainWindow", "position"))
        self.ApplyButton.setText(_translate("MainWindow", "Apply"))
        self.ResetButton.setText(_translate("MainWindow", "Reset"))
        self.BackButton.setText(_translate("MainWindow", "Back"))
        self.NewButton.setText(_translate("MainWindow", "New"))
        self.ExportButton.setText(_translate("MainWindow", "Export"))


class ManageEmployeeWindow(QtWidgets.QMainWindow):
    def __init__(self, MainMenu):
        super(ManageEmployeeWindow, self).__init__()
        self.MainMenu = MainMenu
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_field_map()

        self.insert_into_table()
        self.ui.BackButton.clicked.connect(self.GoBack)
        self.ui.NewButton.clicked.connect(self.show_NewEmployee)
        self.ui.ApplyButton.clicked.connect(self.applyfilter)
        self.ui.toolButton.clicked.connect(self.filters_button_clicked)
        self.ui.ResetButton.clicked.connect(self.restfilter)
        self.ui.ExportButton.clicked.connect(self.ExportCsv)

        #######installing  filter#################
        self.ui.tableWidget.viewport().installEventFilter(self)
########## this method already exists I will overwriting it ######################

    def ExportCsv(self):
        path = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save File', '', 'CSV(*.csv)')

        if path[0] != '':
            print(path[0])
            header_list = []
            for col in range(self.ui.tableWidget.columnCount()):
                header_list.append(
                    self.ui.tableWidget.horizontalHeaderItem(col).text())
            values_list = []
            for row in range(self.ui.tableWidget.rowCount()):
                sub_list = []
                for col in range(self.ui.tableWidget.columnCount()):
                    sub_list.append(self.ui.tableWidget.item(row, col).text())
                values_list.append(sub_list)
            df = pd.DataFrame(values_list,
                              columns=header_list)
            df.to_csv(path[0], index=False)

    def init_field_map(self):
        self.fieldMap = {}
        self.fieldMap[self.ui.IdEntry.objectName()] = "employee.id"
        self.fieldMap[self.ui.FirstNameEntry.objectName()
                      ] = "employee.First_name"
        self.fieldMap[self.ui.LastNameEntry.objectName()
                      ] = "employee.last_name"
        self.fieldMap[self.ui.BirthdayEntry.objectName()
                      ] = "employee.brithday_name"
        self.fieldMap[self.ui.DepartementEntry.objectName()
                      ] = "employee.department"

        self.fieldMap[self.ui.SalaryEntry.objectName()] = "salary"
        self.fieldMap[self.ui.PositionEntry.objectName()
                      ] = "position"

    def restfilter(self):
        self.ui.IdEntry.clear()
        self.ui.FirstNameEntry.clear()
        self.ui.LastNameEntry.clear()
        self.ui.BirthdayEntry.clear()
        self.ui.DepartementEntry.clear()
        self.ui.PositionEntry.clear()
        self.ui.SalaryEntry.clear()
        self.reload_table([])

    def applyfilter(self):

        conditions_list = []
        if self.ui.IdEntry.text() != '':
            conditions_list.append([
                self.fieldMap[self.ui.IdEntry.objectName()],  self.ui.IdEntry.text()])
        if self.ui.FirstNameEntry.text() != '':
            conditions_list.append([
                self.fieldMap[self.ui.FirstNameEntry.objectName()], "\"" + self.ui.FirstNameEntry.text()+"\""])
        if self.ui.LastNameEntry.text() != '':
            conditions_list.append([
                self.fieldMap[self.ui.LastNameEntry.objectName()], "\"" + self.ui.LastNameEntry.text()+"\""])
        if self.ui.BirthdayEntry.text() != '':
            conditions_list.append([
                self.fieldMap[self.ui.BirthdayEntry.objectName()], "\"" + self.ui.BirthdayEntry.text()+"\""])
        if self.ui.DepartementEntry.text() != '':
            conditions_list.append([
                self.fieldMap[self.ui.DepartementEntry.objectName()], "\"" + self.ui.DepartementEntry.text()+"\""])
        if self.ui.SalaryEntry.text() != '':
            conditions_list.append([
                self.fieldMap[self.ui.SalaryEntry.objectName()], "\"" + self.ui.SalaryEntry.text()+"\""])

        if self.ui.PositionEntry.text() != '':
            conditions_list.append([
                self.fieldMap[self.ui.PositionEntry.objectName()], "\"" + self.ui.PositionEntry.text()+"\""])

        self.reload_table(conditions_list)

    def filters_button_clicked(self):
        if self.ui.FilterWidget.isVisible():
            self.ui.FilterWidget.hide()
            self.ui.ApplyButton.hide()
            self.ui.ResetButton.hide()
            self.ui.toolButton.setIcon(QtGui.QIcon("resources/arrow_down.png"))
        else:
            self.ui.ResetButton.show()
            self.ui.ApplyButton.show()
            self.ui.FilterWidget.show()
            self.ui.toolButton.setIcon(QtGui.QIcon("resources/arrow_ap.png"))

    def eventFilter(self, obj, event):
        if (obj == self.ui.tableWidget.viewport() and event.type() == QEvent.MouseButtonPress):
            if (event.button() == Qt.RightButton):
                idx = self.ui.tableWidget.indexAt(event.pos())

                if idx.isValid():

                    deleteAction = QtWidgets.QAction("Delete", self)
                    deleteAction.setObjectName(str(idx.row()))
                    deleteAction.triggered.connect(
                        self.delete_action_triggered)

                    modifyAction = QtWidgets.QAction("Modify", self)
                    modifyAction.setObjectName(str(idx.row()))
                    modifyAction.triggered.connect(
                        self.modify_action_triggered)

                    contextMenu = QtWidgets.QMenu(self)
                    contextMenu.addAction(deleteAction)
                    contextMenu.addAction(modifyAction)
                    contextMenu.exec(event.globalPos())

        return QtWidgets.QMainWindow.eventFilter(self, obj, event)
###########################################################################

    def delete_action_triggered(self):
        replay = QtWidgets.QMessageBox.question(
            self, "Delete", " Are you sure you want to DELETE this employee?", QMessageBox.Yes | QMessageBox.No)
        if replay == QMessageBox.Yes:
            row = int(QObject.sender(self).objectName())
            self.db.delete_employee(self.ui.tableWidget.item(row, 0).text())
            self.ui.tableWidget.removeRow(row)

    def modify_action_triggered(self):
        # in order to access to the row of the object it self####
        row = int(QObject.sender(self).objectName())

        id = int(self.ui.tableWidget.item(row, 0).text())

        self.employeeInfoWindow = EmployeeInofWindow(self, id)

        self.employeeInfoWindow.show()

    def reload_table(self, conditions_list):
        self.ui.tableWidget.setColumnCount(0)

        employee_list = self.db.get_employe_full_info(conditions_list)
        header_list = employee_list[0]
        values_list = employee_list[1]

        no_columns = len(header_list)
        no_rows = len(values_list)

        self.ui.tableWidget.setRowCount(no_rows)
        self.ui.tableWidget.setColumnCount(no_columns)

        self.ui.tableWidget.setHorizontalHeaderLabels(tuple(header_list))

        self.ui.tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)

        self.ui.tableWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)  # to let the selection for all the row

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

        self.ui.tableWidget.verticalHeader().hide()
        for row in range(no_rows):
            for col in range(no_columns):
                self.ui.tableWidget.setItem(
                    row, col, QtWidgets.QTableWidgetItem(str(values_list[row][col])))

    def insert_into_table(self):
        self.db = Database()
        employee_list = self.db.get_employe_full_info([])
        header_list = employee_list[0]
        values_list = employee_list[1]

        no_columns = len(header_list)
        no_rows = len(values_list)

        self.ui.tableWidget.setRowCount(no_rows)
        self.ui.tableWidget.setColumnCount(no_columns)

        self.ui.tableWidget.setHorizontalHeaderLabels(tuple(header_list))

        self.ui.tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)

        self.ui.tableWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)  # to let the selection for all the row

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

        self.ui.tableWidget.verticalHeader().hide()
        for row in range(no_rows):
            for col in range(no_columns):
                self.ui.tableWidget.setItem(
                    row, col, QtWidgets.QTableWidgetItem(str(values_list[row][col])))
#### to switch between windows of the app #######################

    def show_NewEmployee(self):
        self.NewEmplyee = NewEmployeeDialog(self)
        result = self.NewEmplyee.exec()

        if result == QtWidgets.QDialog.Accepted:
            self.db.insert_employee(self.NewEmplyee.employeeInfo)
            self.reload_table([])

    def GoBack(self):
        self.hide()
        self.MainMenu.show()
####################################################################

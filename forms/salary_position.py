from PyQt5 import QtCore, QtGui, QtWidgets
from database import Database
from forms.change_postion_dialog import ChangePositionDialog
from forms.change_salary_dialog import ChangeSalaryDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 500))
        MainWindow.setWindowIcon(QtGui.QIcon('resources/customer-support.png'))
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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 0, 0, 1, 1)
        self.PositionLogLabel = QtWidgets.QLabel(self.centralwidget)
        self.PositionLogLabel.setObjectName("PositionLogLabel")
        self.gridLayout_2.addWidget(self.PositionLogLabel, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 0, 2, 1, 2)
        self.PositionTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.PositionTableWidget.setObjectName("PositionTableWidget")
        self.PositionTableWidget.setColumnCount(0)
        self.PositionTableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.PositionTableWidget, 1, 0, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.ChangeSalaryButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeSalaryButton_2.setObjectName("ChangeSalaryButton_2")
        self.gridLayout_2.addWidget(self.ChangeSalaryButton_2, 2, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.SalaryLogLabel = QtWidgets.QLabel(self.centralwidget)
        self.SalaryLogLabel.setObjectName("SalaryLogLabel")
        self.gridLayout.addWidget(self.SalaryLogLabel, 0, 2, 1, 1)
        self.SalaryTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.SalaryTableWidget.setObjectName("SalaryTableWidget")
        self.SalaryTableWidget.setColumnCount(0)
        self.SalaryTableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.SalaryTableWidget, 1, 0, 1, 5)
        self.ChangeSalaryButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeSalaryButton.setObjectName("ChangeSalaryButton")
        self.gridLayout.addWidget(self.ChangeSalaryButton, 2, 1, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 3, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "position & salary history"))
        self.PositionLogLabel.setText(_translate("MainWindow", "position log"))
        self.ChangeSalaryButton_2.setText(
            _translate("MainWindow", "change position"))
        self.SalaryLogLabel.setText(_translate("MainWindow", "salary log"))
        self.ChangeSalaryButton.setText(
            _translate("MainWindow", "change salary"))


class EmployeeInofWindow(QtWidgets.QMainWindow):
    def __init__(self, MainMenu, id):
        super(EmployeeInofWindow, self).__init__()
        self.MainMenu = MainMenu
        self.id = id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.insert_into_salarytable()
        self.insert_into_positiontable()
        self.ui.ChangeSalaryButton.clicked.connect(self.show_change_salary_diolog
                                                   )
        self.ui.ChangeSalaryButton_2.clicked.connect(self.show_change_position_diolog
                                                     )

    def insert_into_salarytable(self):
        self.db = Database()
        print(int(self.id))
        employee_list = self.db.get_employee_salary(self.id)
        header_list = employee_list[0]
        values_list = employee_list[1]
        print('here  I am how do you do?')

        no_columns = len(header_list)
        no_rows = len(values_list)

        self.ui.SalaryTableWidget.setRowCount(no_rows)
        self.ui.SalaryTableWidget.setColumnCount(no_columns)

        self.ui.SalaryTableWidget.setHorizontalHeaderLabels(tuple(header_list))

        self.ui.SalaryTableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)

        self.ui.SalaryTableWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)  # to let the selection for all the row

        self.ui.SalaryTableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

        self.ui.SalaryTableWidget.verticalHeader().hide()
        for row in range(no_rows):
            for col in range(no_columns):
                self.ui.SalaryTableWidget.setItem(
                    row, col, QtWidgets.QTableWidgetItem(str(values_list[row][col])))

    def insert_into_salarytable(self):
        self.db = Database()
        print(int(self.id))
        employee_list = self.db.get_employee_salary(self.id)
        header_list = employee_list[0]
        values_list = employee_list[1]
        print('here  I am how do you do?')

        no_columns = len(header_list)
        no_rows = len(values_list)

        self.ui.SalaryTableWidget.setRowCount(no_rows)
        self.ui.SalaryTableWidget.setColumnCount(no_columns)

        self.ui.SalaryTableWidget.setHorizontalHeaderLabels(tuple(header_list))

        self.ui.SalaryTableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)

        self.ui.SalaryTableWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)  # to let the selection for all the row

        self.ui.SalaryTableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

        self.ui.SalaryTableWidget.verticalHeader().hide()
        for row in range(no_rows):
            for col in range(no_columns):
                self.ui.SalaryTableWidget.setItem(
                    row, col, QtWidgets.QTableWidgetItem(str(values_list[row][col])))

    def insert_into_positiontable(self):
        self.db = Database()
        int(self.id)
        employee_list = self.db.get_employee_position(self.id)
        header_list = employee_list[0]
        values_list = employee_list[1]

        no_columns = len(header_list)
        no_rows = len(values_list)

        self.ui.PositionTableWidget.setRowCount(no_rows)
        self.ui.PositionTableWidget.setColumnCount(no_columns)

        self.ui.PositionTableWidget.setHorizontalHeaderLabels(
            tuple(header_list))

        self.ui.PositionTableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)

        self.ui.PositionTableWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)  # to let the selection for all the row

        self.ui.PositionTableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

        self.ui.PositionTableWidget.verticalHeader().hide()
        for row in range(no_rows):
            for col in range(no_columns):
                self.ui.PositionTableWidget.setItem(
                    row, col, QtWidgets.QTableWidgetItem(str(values_list[row][col])))

    def show_change_position_diolog(self):
        max_rows = self.ui.PositionTableWidget.rowCount()

        first_name = self.ui.PositionTableWidget.item(max_rows-1, 0).text()
        last_name = self.ui.PositionTableWidget.item(max_rows-1, 1).text()
        position = self.ui.PositionTableWidget.item(max_rows-1, 3).text()

        self.change_position_dialog = ChangePositionDialog(
            self, self.id, first_name, last_name, position)
        self.change_position_dialog.show()

    def show_change_salary_diolog(self):
        max_rows = int(self.ui.SalaryTableWidget.rowCount())

        first_name = self.ui.SalaryTableWidget.item(max_rows-1, 0).text()
        last_name = self.ui.SalaryTableWidget.item(max_rows-1, 1).text()
        salary = self.ui.SalaryTableWidget.item(max_rows-1, 3).text()

        self.change_salary_dialog = ChangeSalaryDialog(
            self, self.id, first_name, last_name, salary)
        self.change_salary_dialog.show()

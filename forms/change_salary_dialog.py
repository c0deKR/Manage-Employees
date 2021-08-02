from PyQt5 import QtCore, QtGui, QtWidgets
from database import Database
from forms.EmployeeFullInfo import SalaryRecord


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(387, 454)
        Dialog.setMaximumSize(QtCore.QSize(600, 500))
        Dialog.setWindowIcon(QtGui.QIcon('resources/customer-support.png'))
        Dialog.setStyleSheet("*{\n"
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
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LastNameCurrentData = QtWidgets.QLabel(Dialog)
        self.LastNameCurrentData.setObjectName("LastNameCurrentData")
        self.gridLayout_2.addWidget(self.LastNameCurrentData, 1, 1, 1, 1)
        self.RaisonLabel = QtWidgets.QLabel(Dialog)
        self.RaisonLabel.setObjectName("RaisonLabel")
        self.gridLayout_2.addWidget(self.RaisonLabel, 5, 0, 1, 1)
        self.SalaryCuerrentData = QtWidgets.QLabel(Dialog)
        self.SalaryCuerrentData.setObjectName("SalaryCuerrentData")
        self.gridLayout_2.addWidget(self.SalaryCuerrentData, 2, 1, 1, 1)
        self.NewSalaryLabel = QtWidgets.QLabel(Dialog)
        self.NewSalaryLabel.setObjectName("NewSalaryLabel")
        self.gridLayout_2.addWidget(self.NewSalaryLabel, 4, 0, 1, 1)
        self.LastNameLabel = QtWidgets.QLabel(Dialog)
        self.LastNameLabel.setObjectName("LastNameLabel")
        self.gridLayout_2.addWidget(self.LastNameLabel, 1, 0, 1, 1)
        self.FirstNameLabel = QtWidgets.QLabel(Dialog)
        self.FirstNameLabel.setObjectName("FirstNameLabel")
        self.gridLayout_2.addWidget(self.FirstNameLabel, 0, 0, 1, 1)
        self.NewSalaryLineEdit = QtWidgets.QLineEdit(Dialog)
        self.NewSalaryLineEdit.setObjectName("NewSalaryLineEdit")
        self.gridLayout_2.addWidget(self.NewSalaryLineEdit, 4, 1, 1, 1)
        self.RaisonLineEdit = QtWidgets.QLineEdit(Dialog)
        self.RaisonLineEdit.setObjectName("RaisonLineEdit")
        self.gridLayout_2.addWidget(self.RaisonLineEdit, 5, 1, 1, 1)
        self.FirstNameCurrentData = QtWidgets.QLabel(Dialog)
        self.FirstNameCurrentData.setObjectName("FirstNameCurrentData")
        self.gridLayout_2.addWidget(self.FirstNameCurrentData, 0, 1, 1, 1)
        self.SalaryLabel = QtWidgets.QLabel(Dialog)
        self.SalaryLabel.setObjectName("SalaryLabel")
        self.gridLayout_2.addWidget(self.SalaryLabel, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.SaveButton = QtWidgets.QPushButton(Dialog)
        self.SaveButton.setObjectName("SaveButton")
        self.gridLayout.addWidget(self.SaveButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            100, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Change Salary"))

        self.RaisonLabel.setText(_translate("Dialog", "raison"))
        self.NewSalaryLabel.setText(_translate("Dialog", "New salary"))
        self.LastNameLabel.setText(_translate("Dialog", "Last name"))
        self.FirstNameLabel.setText(_translate("Dialog", "First name"))
        self.SalaryLabel.setText(_translate("Dialog", "Current salary"))

        self.RaisonLineEdit.setPlaceholderText(
            _translate("Dialog", "(Optional)"))

        self.SaveButton.setText(_translate("Dialog", "save"))


class ChangeSalaryDialog(QtWidgets.QDialog):
    def __init__(self, EmployeeInfoWindow, id, first_name, last_name, salary):
        super(ChangeSalaryDialog, self).__init__()
        self.EmployeeInfoWindow = EmployeeInfoWindow
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = Database()
        self.ui.SaveButton.clicked.connect(self.addrecord)
        self.fill_histroy()

    def fill_histroy(self):
        self.ui.FirstNameCurrentData.setText(self.first_name)
        self.ui.LastNameCurrentData.setText(self.last_name)
        self.ui.SalaryCuerrentData.setText(self.salary)

    def addrecord(self):
        id = self.id
        print(id)
        salary_record = SalaryRecord(id,
                                     self.ui.NewSalaryLineEdit.text(), self.ui.RaisonLineEdit.text())
        self.db.insert_new_salary(salary_record)
        self.accept()

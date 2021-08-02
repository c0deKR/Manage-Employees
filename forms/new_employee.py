from PyQt5 import QtCore, QtGui, QtWidgets
from forms.calender import CalenderDialog
from forms.EmployeeFullInfo import EmployeeFullInfo


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 290)
        Dialog.setWindowIcon(QtGui.QIcon('resources/plus.png'))
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
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.FirstnameLabel = QtWidgets.QLabel(Dialog)
        self.FirstnameLabel.setObjectName("FirstnameLabel")
        self.gridLayout.addWidget(self.FirstnameLabel, 0, 0, 1, 1)
        self.FirstNameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.FirstNameLineEdit.setObjectName("FirstNameLineEdit")
        self.gridLayout.addWidget(self.FirstNameLineEdit, 0, 1, 1, 1)
        self.LastNameLabel = QtWidgets.QLabel(Dialog)
        self.LastNameLabel.setObjectName("LastNameLabel")
        self.gridLayout.addWidget(self.LastNameLabel, 1, 0, 1, 1)
        self.LastNameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.LastNameLineEdit.setObjectName("LastNameLineEdit")
        self.gridLayout.addWidget(self.LastNameLineEdit, 1, 1, 1, 1)
        self.BirthdayLabel = QtWidgets.QLabel(Dialog)
        self.BirthdayLabel.setObjectName("BirthdayLabel")
        self.gridLayout.addWidget(self.BirthdayLabel, 2, 0, 1, 1)
        self.BirthdayToolButton = QtWidgets.QToolButton(Dialog)
        self.BirthdayToolButton.setText("")
        self.BirthdayToolButton.setObjectName("BirthdayToolButton")
        self.gridLayout.addWidget(self.BirthdayToolButton, 2, 1, 1, 1)
        self.BirthdayToolButton.setIcon(
            QtGui.QIcon("resources/calendar.png"))
        self.BirthdayToolButton.setAutoRaise(True)
        self.DepartmentLabel = QtWidgets.QLabel(Dialog)
        self.DepartmentLabel.setObjectName("DepartmentLabel")
        self.gridLayout.addWidget(self.DepartmentLabel, 3, 0, 1, 1)
        self.DepartmentLineEdit = QtWidgets.QLineEdit(Dialog)
        self.DepartmentLineEdit.setObjectName("DepartmentLineEdit")
        self.gridLayout.addWidget(self.DepartmentLineEdit, 3, 1, 1, 1)
        self.SalaryLabel = QtWidgets.QLabel(Dialog)
        self.SalaryLabel.setObjectName("SalaryLabel")
        self.gridLayout.addWidget(self.SalaryLabel, 4, 0, 1, 1)
        self.SalaryLineEdit = QtWidgets.QLineEdit(Dialog)
        self.SalaryLineEdit.setObjectName("SalaryLineEdit")
        self.gridLayout.addWidget(self.SalaryLineEdit, 4, 1, 1, 1)
        self.PositionLabel = QtWidgets.QLabel(Dialog)
        self.PositionLabel.setObjectName("PositionLabel")
        self.gridLayout.addWidget(self.PositionLabel, 5, 0, 1, 1)
        self.PositionLineEdit = QtWidgets.QLineEdit(Dialog)
        self.PositionLineEdit.setObjectName("PositionLineEdit")
        self.gridLayout.addWidget(self.PositionLineEdit, 5, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.SaveButton = QtWidgets.QPushButton(Dialog)
        self.SaveButton.setObjectName("SaveButton")
        self.gridLayout_2.addWidget(self.SaveButton, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Employee"))
        self.FirstnameLabel.setText(_translate("Dialog", "First name"))
        self.LastNameLabel.setText(_translate("Dialog", "Last name"))
        self.BirthdayLabel.setText(_translate("Dialog", "birthday"))
        self.DepartmentLabel.setText(_translate("Dialog", "department"))
        self.SalaryLabel.setText(_translate("Dialog", "salary"))
        self.PositionLabel.setText(_translate("Dialog", "position"))
        self.SaveButton.setText(_translate("Dialog", "save"))


class NewEmployeeDialog(QtWidgets.QDialog):
    def __init__(self, ManageEmployeeWindow):
        super(NewEmployeeDialog, self).__init__()
        self.ManageEmployeeWindow = ManageEmployeeWindow
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.employeeInfo = None
        self.birthday = None

        self.ui.BirthdayToolButton.clicked.connect(self.show_calender)
        self.ui.SaveButton.clicked.connect(self.save_emplyee_info)

    def save_emplyee_info(self):
        # checking if each lineedit is empty!!!!!!
        print('did you come here or !')
        self.employeeInfo = EmployeeFullInfo(
            self.ui.FirstNameLineEdit.text(),
            self.ui.LastNameLineEdit.text(),
            self.birthday,
            self.ui.DepartmentLineEdit.text(),
            self.ui.SalaryLineEdit.text(),
            self.ui.PositionLineEdit.text())

        self.accept()

    def show_calender(self):
        self.calender = CalenderDialog()
        result = self.calender.exec()
        if result == QtWidgets.QDialog.Accepted:
            self.birthday = self.calender.date

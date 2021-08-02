
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.manage_employees import ManageEmployeeWindow
from forms.charts import ChartsWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

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

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ViewChartsButton = QtWidgets.QPushButton(self.centralwidget)
        self.ViewChartsButton.setMinimumSize(QtCore.QSize(200, 60))
        self.ViewChartsButton.setObjectName("ViewChartsButton")
        self.gridLayout.addWidget(self.ViewChartsButton, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.ManageEployeesButton = QtWidgets.QPushButton(self.centralwidget)
        self.ManageEployeesButton.setMinimumSize(QtCore.QSize(200, 60))
        self.ManageEployeesButton.setObjectName("ManageEployeesButton")
        self.gridLayout.addWidget(self.ManageEployeesButton, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main menu"))
        self.ViewChartsButton.setText(_translate("MainWindow", "View Charts"))
        self.ManageEployeesButton.setText(
            _translate("MainWindow", "Manage Employees"))

######################### I am working here ###################################


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ManageEployeesButton.clicked.connect(
            self.show_manageEmployeesPage)
        self.ui.ViewChartsButton.clicked.connect(self.show_charts)

    def show_manageEmployeesPage(self):
        self.hide()
        self.ManageEmployeeWindow = ManageEmployeeWindow(self)
        self.ManageEmployeeWindow.show()

    def show_charts(self):
        self.hide()
        self.ChartsWindow = ChartsWindow(self)
        self.ChartsWindow.show()
        # ############################################################################

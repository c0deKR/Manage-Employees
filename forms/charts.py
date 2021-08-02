from database import Database
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class Canvas1(FigureCanvas):
    def __init__(self, parent):

        fig, self.ax = plt.subplots(figsize=(4, 4), dpi=100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        self.db = Database()
        result_list = self.db.get_salary_stats()
        slices = ["Min. salary", "Avg. salary", "Max. salary"]
        plt.bar(slices, result_list, color=['red', 'green', 'blue'],
                width=0.4)

        plt.xlabel("")
        plt.ylabel("salary")

        plt.grid()


class Canvas2(FigureCanvas):
    def __init__(self, parent):

        fig, self.ax = plt.subplots(figsize=(4, 4), dpi=100)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        self.db = Database()
        departements = []
        salaryies_per_department = []
        result_list = self.db.get_total_department_salries()
        for row in result_list:
            departements.append(row[0])
            salaryies_per_department.append(row[1])
        plt.pie(salaryies_per_department, labels=departements)
        plt.grid()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        MainWindow.setWindowIcon(QtGui.QIcon('resources/pie-chart.png'))
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
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout2.setObjectName("gridLayout2")

        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout1 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout1.setObjectName("gridLayout1")

        self.gridLayout.addWidget(self.widget, 0, 1, 1, 2)

        spacerItem = QtWidgets.QSpacerItem(
            623, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setMinimumSize(QtCore.QSize(0, 35))
        self.BackButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.BackButton.setObjectName("BackButton")
        self.gridLayout.addWidget(self.BackButton, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Charts"))
        self.BackButton.setText(_translate("MainWindow", "Back"))


class ChartsWindow(QtWidgets.QMainWindow):
    def __init__(self, MainMenu):
        super(ChartsWindow, self).__init__()
        self.MainMenu = MainMenu
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.bar = Canvas1(self)
        self.ui.gridLayout2.addWidget(self.ui.bar, 1, 1, 1, 1)

        self.ui.pie = Canvas2(self)
        self.ui.gridLayout1.addWidget(self.ui.pie, 1, 1, 1, 1)

        self.ui.BackButton.clicked.connect(self.GoBack)

    def GoBack(self):

        self.hide()
        self.MainMenu.show()

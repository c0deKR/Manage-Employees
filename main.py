import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.mainwindow import MainWindow


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

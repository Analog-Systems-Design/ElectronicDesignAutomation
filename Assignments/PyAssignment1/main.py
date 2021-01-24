# ------------------------------------------------------
# --------------Windows and Math Dependencies ----------
# ------------------------------------------------------
import os
import sys
import numpy as np
# ------------------------------------------------------
# -----------------Pyside2 Dependencies ----------------
# ------------------------------------------------------
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
from PySide2.QtCore import *
from PySide2 import QtWidgets

# ------------------------------------------------------
# ------------- Front & Backend Libs -------------------
# ------------------------------------------------------
from plot import ploteqn
from plotwindow import Ui_MainWindow

# ------------------------------------------------------
# -------------------- MainProgram ---------------------
# ------------------------------------------------------
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.plot)

    def plot(self):
        # Get Input from FrontEnd
        eqn=self.textEdit.text()
        lowerlimit=self.lineEdit.text()
        upperlimit=self.lineEdit_3.text()

        # Process Input in BackEnd
        flag,x,y=ploteqn(eqn,lowerlimit,upperlimit)

        # Display Processeddata in FrontEnd
        if flag==0:
            self.displayplot(x,y)
        


if (__name__ == '__main__'):
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

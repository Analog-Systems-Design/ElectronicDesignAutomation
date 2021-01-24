# ------------------------------------------------------
# ------------- MatplotLib Dependencies ----------------
# ------------------------------------------------------
from PySide2 import QtWidgets # import PySide2 before matplotlib
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
matplotlib.use("Qt5Agg")


#-------------------------------------------------------
#------------------Additional Widgets-------------------
#-------------------------------------------------------
from mplcanvas import mplcanvas

#------------------------------------------------------
#------------------Main Program------------------------
#------------------------------------------------------
class Ui_MainWindow(object):
    # Adding Components
    def setupUi(self, MainWindow):
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 900)

        MainWindow.setMinimumSize(QSize(900, 900))
        MainWindow.setMaximumSize(QSize(900, 900))
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.textEdit = QLineEdit(self.centralwidget)
        self.textEdit.setObjectName(u"LineEdit")
        font = QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(18)
        self.label.setFont(font1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(16)
        self.pushButton.setFont(font2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        font3 = QFont()
        font3.setPointSize(18)
        self.lineEdit.setFont(font3)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.renameUi(MainWindow)

        self.genlayout()

    #Renaming Components
    def renameUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Function Plotter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"F(x)=", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Upper Limit=", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Lower Limit=", None))
    
    # Generating Layout
    def genlayout(self):
        layout2 = QtWidgets.QHBoxLayout()
        layout2.addWidget(self.label_4)
        layout2.addWidget(self.lineEdit_3)

        layout3 = QtWidgets.QHBoxLayout()
        layout3.addWidget(self.label_3)
        layout3.addWidget(self.lineEdit)

        layout4 = QtWidgets.QHBoxLayout()
        layout4.addWidget(self.label)
        layout4.addWidget(self.textEdit)
        
        layout = QtWidgets.QVBoxLayout()
        # Create toolbar, passing canvas as first parament, parent
        #(self, the MainWindow) as second.
        self.sc = mplcanvas(self, width=5, height=5, dpi=100)
        toolbar = NavigationToolbar(self.sc, self)
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)
        layout.addWidget(self.pushButton)
        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

    def displayplot(self,x,y):
        self.sc.axes.cla()
        self.sc.axes.plot(x, y)
        self.sc.draw()
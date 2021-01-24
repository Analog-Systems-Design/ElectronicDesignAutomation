import pytest
from PySide2 import QtCore
import main
import matplotlib.pyplot as plt
import time
@pytest.fixture
def app(qtbot):
    window = main.MainWindow()
    qtbot.addWidget(window)
    return window

def test_plot_click(app, qtbot):
    app.lineEdit_3.clear()
    #enter lowerlimit
    qtbot.keyClicks(app.lineEdit_3, '-1')
    assert app.lineEdit_3.text()=='-1'
    
    app.lineEdit.clear()
    #enter upperlimit
    qtbot.keyClicks(app.lineEdit, '1')
    assert app.lineEdit.text()=='1'
    
    app.textEdit.clear()
    #enter eqn
    qtbot.keyClicks(app.textEdit, 'cos(x)')
    assert app.textEdit.text()=='cos(x)'
    
    #click plot
    qtbot.mouseClick(app.pushButton, QtCore.Qt.LeftButton)
    
    #save Plot
    app.sc.fog.savefig('testcosine.png')
    
    #read baseline img and check whether they are equal or not
    from PIL import Image

    baseline = Image.open('cosine.png')
    test = Image.open('testcosine.png')

    assert list(test.getdata()) == list(baseline.getdata())
    
    
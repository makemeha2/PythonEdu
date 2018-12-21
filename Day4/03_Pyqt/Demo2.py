import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(r"C:\examples\Day4\03_Pyqt\DemoForm2.ui")[0]
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 PyQt데모")
    
    def firstClick(self):
        self.label.setText("첫번째 버튼을 글릭")

    def secondClick(self):
        self.label.setText("두번째 버튼을 글릭")

    def thirdClick(self):
        self.label.setText("세번째 버튼을 글릭")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()
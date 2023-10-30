#PyQt6

import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt6.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('First Application')
        self.setGeometry(400,400,400,400)
        self.setWindowIcon(QIcon('PyQt6/cookie.png'))
        self.setToolTip('My Application')
        self.initUI()
    
    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText('ADINIZ: ')
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText('SOYADINIZ: ')
        self.lbl_surname.move(50,70)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(120, 30)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(120, 70)

        self.txt_window = QtWidgets.QTextBrowser(self)
        self.txt_window.setGeometry(200,200,200,100)
        self.txt_window.move(100,150)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.move(175,260)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText('SAVE')
        self.btn_save.move(120,110)
        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
        self.txt_window.setText("ADINIZ: " + self.txt_name.text() + "\n" + "SOYADINIZ:" + self.txt_surname.text())
        
        self.lbl_result.setText(self.txt_name.text()+" "+self.txt_surname.text())

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())

window()
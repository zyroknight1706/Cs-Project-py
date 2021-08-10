import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("test.... Again")
uic.loadUi("LoginScreen.ui", win)
win.show()
sys.exit(app.exec_())
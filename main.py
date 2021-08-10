from test import Window
import sys
from PyQt5.QtWidgets import QApplication
import test

app = QApplication(sys.argv)
win = test.Window()
sys.exit(app.exec_())

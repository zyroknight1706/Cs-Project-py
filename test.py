from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.startLoginUI()
        self.show()
    def startLoginUI(self):
        uic.loadUi("LoginScreen.ui", self)
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

app = QApplication(sys.argv)
win = QMainWindow()
win2 = QMainWindow()

win.setGeometry(0, 0, 1920, 1080)
win.setStyleSheet("background-image: url(C:/Users/Hp/Downloads/sci-fi_back.jpg);")
win.setWindowTitle('Midark!')
# win2.setGeometry(0, 0, 1920, 1080)
# win2.setStyleSheet("background-image: url(C:/Users/Hp/Downloads/newspaper_back_4k.jpg);")
# win2.setWindowTitle('Midark!!')
app.setActiveWindow(win)
win.show()

#QTimer.start(app, 5000)
#win2.show()
#app.setStyleSheet("background-image: url(newspaper_back.jpg);")
'''
lbl = QLabel('lmaoooooooooooooooooo')
lbl.setStyleSheet('background-image: url(C:/Users/Hp/Downloads/newspaper_back.jpg);')
lbl.show()
'''
sys.exit(app.exec_())
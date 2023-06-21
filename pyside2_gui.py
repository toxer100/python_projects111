# PySide 2 
from PySide2.QtWidgets import *
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import *
import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()


window.show()   # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()
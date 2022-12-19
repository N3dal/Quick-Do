#!/usr/bin/python3
# -----------------------------------------------------------------
# Simple to-do app using pyqt5.
#
#
#
# Author:N84.
#
# Create Date:Mon Dec 19 22:28:30 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import tools


class MainWindow(QMainWindow):
    """
        the app main-window;
    """

    WIDTH = 350
    HEIGHT = 550
    STYLESHEET = """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)

        self.setStyleSheet(MainWindow.STYLESHEET)


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

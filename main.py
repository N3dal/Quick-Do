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


class TitleBar(QFrame):
    """
        Custom Title bar for the Main window;
    """

    HEIGHT = 31

    STYLESHEET = """
        background-color: #8b949e;
        
        border-top-left-radius: 10px;
        border-top-right-radius:10px;
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 0px;

    """

    TITLE = "Quick-Do"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(self.parent().width(), TitleBar.HEIGHT)

        self.setStyleSheet(TitleBar.STYLESHEET)


class MainFrame(QFrame):
    """
        The main Frame;
    """
    STYLESHEET = """
        background: QLinearGradient(x1 :0, y1:0,
                                    x2: 1, y2: 0,
                                    stop: 0 #005C97,
                                    stop: 1 #363795);
                                    
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
        border-bottom-left-radius: 15px;
        border-bottom-right-radius: 15px;
            
        
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(self.parent().width(), self.parent().height() - 50)

        self.setStyleSheet(MainFrame.STYLESHEET)


class MainWindow(QMainWindow):
    """
        the app main-window;
    """

    WIDTH = 350
    HEIGHT = 550

    STYLESHEET = """"""

    OPACITY = 0.98

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)

        self.setStyleSheet(MainWindow.STYLESHEET)

        self.setWindowOpacity(MainWindow.OPACITY)

        self.setAttribute(Qt.WA_TranslucentBackground)

        # to remove the title bar and the frame;
        self.setWindowFlags(Qt.FramelessWindowHint)

        # create the title bar;
        self.title_bar = TitleBar(parent=self)
        self.title_bar.move(0, 0)

        # create the main Frame;
        self.main_frame = MainFrame(parent=self)
        self.main_frame.move(0, TitleBar.HEIGHT-5)


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

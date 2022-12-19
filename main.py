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

# wipe terminal screen;
tools.clear()


class TitleBar(QFrame):
    """
        Custom Title bar for the Main window;
    """

    HEIGHT = 34

    STYLESHEET = """
        background-color: #8b949e;
        
        border-top-left-radius: 10px;
        border-top-right-radius:10px;
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 0px;

    """

    LABEL_STYLESHEET = """
        color: black;
        font-weight: bold;
        font-family: Mono;
    """

    TITLE = "Quick-Do"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(self.parent().width(), TitleBar.HEIGHT)

        self.setStyleSheet(TitleBar.STYLESHEET)

        self.title_label = QLabel(
            parent=self, text=f"<h3>{TitleBar.TITLE}</h3>")

        # create the title label;
        self.title_label.setStyleSheet(TitleBar.LABEL_STYLESHEET)

        self.title_label.move(20, 5)

        # create the close button;
        self.close_btn = QPushButton(parent=self)

        self.close_btn.setIcon(QIcon("./assets/close.png"))

        self.close_btn.setIconSize(QSize(24, 24))

        self.close_btn.clicked.connect(sys.exit)

        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.close_btn.move(318, 3)

        # create the minimize button;

        self.minimize_btn = QPushButton(parent=self)

        self.minimize_btn.setIcon(QIcon("./assets/minimize.png"))

        self.minimize_btn.setIconSize(QSize(24, 24))

        self.minimize_btn.clicked.connect(self.parent().showMinimized)

        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.minimize_btn.move(280, 3)


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

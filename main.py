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

# TODO: add the ability to delete some tasks;


class Signals(QObject):
    """
            contain all the signals for NewTaskBox;
        """

    new_task = pyqtSignal(str)


class NewTaskBox(QMainWindow):
    """
        Custom window to add new tasks;
    """

    WIDTH = 400
    HEIGHT = 105

    STYLESHEET = """
        border-radius: 0px;
        
    """

    TITLE = "Add new Task"

    LINE_EDIT_STYLESHEET = """
        background-color: white;
        border-radius: 5px;
        color: black;
        font-size: 18px;
    """

    BUTTON_STYLESHEET = """
        QPushButton:hover{
            background-color: #4285f4;
            }
        QPushButton{
            color: black;
            background-color: #4169e1;
            font-size: 18px;
            border-radius: 5px;
            }
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(NewTaskBox.WIDTH, NewTaskBox.HEIGHT)

        self.setWindowTitle(NewTaskBox.TITLE)

        self.setStyleSheet(NewTaskBox.STYLESHEET)

        self.signals = Signals()

        # create text edit;
        self.line_edit_box = QLineEdit(parent=self)

        self.line_edit_box.setFixedSize(self.width()-10, 60)

        self.line_edit_box.setStyleSheet(NewTaskBox.LINE_EDIT_STYLESHEET)

        self.line_edit_box.move(5, 5)

        # create add button;
        self.add_btn = QPushButton(parent=self, text="Add")

        self.add_btn.setFixedSize(90, 30)

        self.add_btn.setStyleSheet(NewTaskBox.BUTTON_STYLESHEET)

        self.add_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.add_btn.clicked.connect(self.add_btn_event)

        self.add_btn.move(305, 70)

    def add_btn_event(self):
        """
            add button click event;

            return None;
        """
        new_task_text = self.line_edit_box.text()

        self.signals.new_task.emit(new_task_text)

        self.close()

        return None


class Task(QWidget):
    """
        custom label with checkbox beside it;
    """

    STYLESHEET = """
        background: transparent;
    """

    LABEL_STYLESHEET = """
        color: white;
        font-size: 20px;
        font-weight: bold;
    """

    CHECKBOX_STYLESHEET = """

    QCheckBox::indicator{
        background-transparent;
        border: 2px solid black;
        width: 15px;
        height: 15px;
    }

    QCheckBox::indicator:pressed{
        background-color: #5eba7d;
    }

    QCheckBox::indicator:checked{
        background-color: #5eba7d;
    }

    QCheckBox::indicator:hover{
        border: 2px groove black;

    }

    QCheckBox{
        background: transparent;
        background-color: transparent;
        border: none;
        }
    """

    def __init__(self, task_name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.task_value = task_name

        self.__task_name = task_name[:22] + \
            ("...." if len(task_name) > 22 else "")

        self.setFixedSize(self.parent().width(), 70)

        self.label = QLabel(parent=self, text=self.__task_name)

        self.label.setStyleSheet(Task.LABEL_STYLESHEET)

        self.label.move(25, 0)

        self.checkbox = QCheckBox(parent=self)

        self.setStyleSheet(Task.STYLESHEET)

        self.checkbox.setStyleSheet(Task.CHECKBOX_STYLESHEET)

        self.checkbox.setCursor(QCursor(Qt.PointingHandCursor))

        self.checkbox.toggled.connect(self.checkbox_click_event)

        self.checkbox.move(0, 0)

        # and the last step is to show everything;
        self.show()

    def stroke_out(self):
        """
            add Stroke out line to check box text;

            return None;
        """
        font = self.label.font()
        font.setStrikeOut(True)
        self.label.setFont(font)

        return None

    def remove_stroke_out(self):
        """
            remove the Stroke out line from the check box text;

            return None;
        """

        font = self.label.font()
        font.setStrikeOut(False)
        self.label.setFont(font)

        return None

    def checkbox_click_event(self):
        """
            checkbox event when we change the status;

            return None
        """

        font = self.label.font()

        task_stroke_out = font.strikeOut()

        if task_stroke_out:
            # if there's line stroke the label,
            # then remove it;
            self.remove_stroke_out()

        else:
            # if there's no line stroke the label,
            # then add one simply out Strike out the label;
            self.stroke_out()

        return None

    def mousePressEvent(self, e):
        # print(dir(e))

        if e.button() == 4:
            # mouse middle click
            # then remove the task;
            pass


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

        for item in dir(Qt):
            if "cursor" in str(item).lower():
                print(item)

        self.close_btn.move(318, 3)

        # create the minimize button;

        self.minimize_btn = QPushButton(parent=self)

        self.minimize_btn.setIcon(QIcon("./assets/minimize.png"))

        self.minimize_btn.setIconSize(QSize(24, 24))

        self.minimize_btn.clicked.connect(self.parent().showMinimized)

        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.minimize_btn.move(280, 3)

    def mousePressEvent(self, e):

        self.old_mouse_position = e.globalPos()

        self.setCursor(QCursor(Qt.DragMoveCursor))

        return None

    def mouseReleaseEvent(self, e):

        self.setCursor(QCursor(Qt.ArrowCursor))

        return None

    def mouseMoveEvent(self, e):

        delta = QPoint(e.globalPos() - self.old_mouse_position)

        self.parent().move(self.parent().x() + delta.x(), self.parent().y() + delta.y())
        self.old_mouse_position = e.globalPos()

        return None


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

    MAX_TASKS = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(self.parent().width(), self.parent().height() - 50)

        self.setStyleSheet(MainFrame.STYLESHEET)

        self.tasks = []

        self.add_new_task_btn = QPushButton(parent=self, text="")

        self.add_new_task_btn.setIcon(QIcon("./assets/add.png"))

        self.add_new_task_btn.setIconSize(QSize(48, 48))

        self.add_new_task_btn.setStyleSheet("""
                                            background: transparent;
                                            """)

        self.add_new_task_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.add_new_task_btn.clicked.connect(self.add_new_task_btn_event)

        self.add_new_task_btn.move(280, 435)

        # create add new task box;
        self.new_task_box = NewTaskBox(parent=self)

        self.new_task_box.signals.new_task.connect(self.create_new_task)

        # create the tasks;

        # the space b/w tasks in y is 35;

    def add_new_task_btn_event(self):
        """
            add new task button click event;

            return None;
        """

        self.new_task_box.line_edit_box.setText("")
        self.new_task_box.line_edit_box.setFocus(True)
        self.new_task_box.show()

        return None

    def create_new_task(self, task_name):
        """
            create new task and place it in the main frame;

            return None;
        """

        # Guard conditions;
        if not task_name:
            # if the task name is empty;
            return None

        if len(self.tasks) > MainFrame.MAX_TASKS:

            raise Exception("Max tasks Limit!!!")
            return None

        VERTICAL_SHIFT = 35

        task = Task(task_name, parent=self)

        if not self.tasks:
            # if we don't have any task then use the init values of y;
            y = 25

        else:
            # if we have tasks;
            y = self.tasks[-1].y() + VERTICAL_SHIFT

        self.tasks.append(task)

        task.move(15, y)

        return None


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

        # hide the main window;
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

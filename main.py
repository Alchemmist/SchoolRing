import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.number = ''
        uic.loadUi('mu_ui_test.ui', self)
        self.login_button_cerkle.clicked.connect(self.operation)

    def operation(self):
        print(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

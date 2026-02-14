from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow

class App(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("shYori")
        self.setMinimumSize(1600, 850)
        self.showMaximized()

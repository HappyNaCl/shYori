from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget
from view.pages import MainPage, OverlayPage
from view.navigator import Navigator
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()
        self.navigator = Navigator(self.stack)

        self.main_page = MainPage(self.navigator)

        self.overlay_page = OverlayPage(self.navigator)
        self.navigator.register_overlay(self.overlay_page)

        self.stack.addWidget(self.main_page)  # index 0

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack)

        self.setLayout(main_layout)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setWindowTitle("shYori")

        (width, height) = self.getScreenDimension()
        self.setMinimumSize(width, height)
        
        self.showMaximized()

    def getScreenDimension(self) -> tuple[int, int]:
        screen = self.screen()
        if screen != None:
            geometry = screen.availableGeometry()
            return (int(geometry.width() * 0.8), int(geometry.height() * 0.8))

        return (1600, 850)
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

from view.navigator import Navigator, Page

class MainPage(QWidget):
    def __init__(self, navigator: Navigator):
        super().__init__()
        self.navigator = navigator

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.scan_button = QPushButton("Scan")
        self.scan_button.setFixedSize(120, 40)
        self.scan_button.clicked.connect(lambda: self.navigator.go(Page.SCAN))

        layout.addWidget(self.scan_button)

        self.setLayout(layout)
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

from views.navigator import Navigator, Page
from views.components import Navbar

class MainPage(QWidget):
    def __init__(self, navigator: Navigator):
        super().__init__()
        self.navigator = navigator

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        navbar = Navbar()
        main_layout.addWidget(navbar)

        self.label = QLabel("")
        self.label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                color: #efefef;
            }
        """)

        self.scan_button = QPushButton("Scan")
        self.scan_button.setFixedSize(120, 40)
        self.scan_button.clicked.connect(lambda: self.navigator.go(Page.SCAN))

        main_layout.addWidget(self.scan_button)
        main_layout.addWidget(self.label)

        self.setLayout(main_layout)

    def setData(self, data):
        print(f"MainPage received data: {data}")
        self.label.setText(data)
        pass
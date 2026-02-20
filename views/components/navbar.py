from PyQt6.QtWidgets import QFrame, QPushButton, QHBoxLayout

class Navbar(QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(60)
        self.setStyleSheet("""
            QFrame {
                background-color: #3a3a3a;
                border-radius: 15px;
            }
        """)

        layout = QHBoxLayout(self)

        home_button = QPushButton("Home")
        settings_button = QPushButton("Settings")

        layout.addWidget(home_button)
        layout.addWidget(settings_button)
        layout.addStretch()

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMovie

class LoadingPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.spinner_label = QLabel()
        self.spinner_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.movie = QMovie("assets/loading.gif")
        self.spinner_label.setMovie(self.movie)
        self.movie.start()

        self.text_label = QLabel("Initializing, please wait...")
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.spinner_label)
        layout.addSpacing(20)
        layout.addWidget(self.text_label)

        self.setLayout(layout)
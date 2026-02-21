from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QMovie, QRegion, QPainterPath

class LoadingPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        self.spinner_label = QLabel()
        self.spinner_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinner_label.setFixedSize(400, 400)

        self.movie = QMovie("assets/loading.gif")
        self.movie.setScaledSize(QSize(400, 400))
        self.spinner_label.setMovie(self.movie)
        self.movie.start()
        
        path = QPainterPath()
        path.addEllipse(0, 0, 400, 400)
        region = QRegion(path.toFillPolygon().toPolygon())
        self.spinner_label.setMask(region)

        self.text_label = QLabel("Initializing, please wait.")
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label.setStyleSheet("""
            QLabel {
                font-size: 40px;
                color: #efefef;
            }
        """)

        layout.addWidget(self.spinner_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(30)
        layout.addWidget(self.text_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
        
        # Dot animation
        self.dot_count = 1
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDots)
        self.timer.start(500)  # Update every 500ms
    
    def updateDots(self):
        """Update the dots in the loading text"""
        self.dot_count = (self.dot_count % 3) + 1
        dots = "." * self.dot_count
        self.text_label.setText(f"Initializing, please wait{dots}")
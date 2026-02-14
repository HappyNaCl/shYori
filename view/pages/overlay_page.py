from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QPoint, QRect
from PyQt6.QtGui import QKeyEvent, QMouseEvent, QPainter, QColor, QGuiApplication

from view.navigator import Navigator, Page

class OverlayPage(QWidget):
    def __init__(self, navigator: Navigator):
        super().__init__()
        self.navigator = navigator

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setCursor(Qt.CursorShape.CrossCursor)

        self.start_point = QPoint()
        self.end_point = QPoint()
        self.selecting = False
    
    def mousePressEvent(self, a0: QMouseEvent | None) -> None:
        if a0 != None and a0.button() == Qt.MouseButton.LeftButton:
            self.start_point = a0.position().toPoint()
            self.end_point = self.start_point
            self.selecting = True
            self.update()

    def mouseMoveEvent(self, a0: QMouseEvent | None):
        if a0 != None and self.selecting:
            self.end_point = a0.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, a0: QMouseEvent | None):
        if a0 != None and a0.button() == Qt.MouseButton.LeftButton:
            self.selecting = False
            rect = QRect(self.start_point, self.end_point).normalized()

            self.capture_region(rect)

    def capture_region(self, rect: QRect):
        screen = QGuiApplication.primaryScreen()
        if screen != None:
            screenshot = screen.grabWindow(
                0, # type: ignore
                rect.x(),
                rect.y(),
                rect.width(),
                rect.height()
            )

            screenshot.save("capture.png")
            print("Captured region saved.")

    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        if a0 != None and (a0.key() == Qt.Key.Key_Q or a0.key() == Qt.Key.Key_Escape):
            self.navigator.go(Page.MAIN)

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.fillRect(self.rect(), QColor(0, 0, 0, 120))

        painter.setPen(QColor(255, 0, 0))
        painter.drawText(100, 100, "Overlay Active")

    def showOverlay(self):
        self.showFullScreen()
        self.show()
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QPoint, QRect
from PyQt6.QtGui import (
    QKeyEvent,
    QMouseEvent,
    QPainter,
    QColor,
    QGuiApplication
)

from controller import translator_controller
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

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setCursor(Qt.CursorShape.CrossCursor)

        self.start_point = QPoint()
        self.end_point = QPoint()
        self.selecting = False

    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        if a0 and a0.key() in (Qt.Key.Key_Q, Qt.Key.Key_Escape):
            self.exitOverlay()

    def mousePressEvent(self, a0: QMouseEvent | None) -> None:
        if a0 and a0.button() == Qt.MouseButton.LeftButton:
            self.start_point = a0.position().toPoint()
            self.end_point = self.start_point
            self.selecting = True
            self.update()
        elif a0 and a0.button() == Qt.MouseButton.RightButton:
            self.exitOverlay()

    def mouseMoveEvent(self, a0: QMouseEvent | None) -> None:
        if a0 and self.selecting:
            self.end_point = a0.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, a0: QMouseEvent | None) -> None:
        if a0 and a0.button() == Qt.MouseButton.LeftButton:
            self.selecting = False
            rect = QRect(self.start_point, self.end_point).normalized()

            self.hide()
            QGuiApplication.processEvents()

            self.captureRegion(rect)

            self.start_point = QPoint()
            self.end_point = QPoint()
            self.showFullScreen()
            self.update()

    def captureRegion(self, rect: QRect):
        screen = QGuiApplication.primaryScreen()
        if screen:
            screenshot = screen.grabWindow(
                0,  # type: ignore
                rect.x(),
                rect.y(),
                rect.width(),
                rect.height()
            )
            translator_controller.translate(screenshot)

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Dim whole screen
        painter.fillRect(self.rect(), QColor(0, 0, 0, 120))

        painter.setPen(QColor(255, 255, 255))
        painter.drawText(40, 60, "Capture Mode (ESC to exit)")

        if self.selecting:
            rect = QRect(self.start_point, self.end_point).normalized()

            painter.setCompositionMode(
                QPainter.CompositionMode.CompositionMode_Clear
            )
            painter.fillRect(rect, Qt.GlobalColor.transparent)

            painter.setCompositionMode(
                QPainter.CompositionMode.CompositionMode_SourceOver
            )
            painter.setPen(QColor(255, 0, 0))
            painter.drawRect(rect)

    def showOverlay(self):
        main_window = self.navigator.stack.window()
        if main_window:
            main_window.hide()

        self.showFullScreen()
        self.setFocus()
        self.show()

    def exitOverlay(self):
        self.navigator.go(Page.MAIN)

        main_window = self.navigator.stack.window()
        if main_window:
            main_window.show()
            main_window.raise_()
            main_window.activateWindow()

        self.close()

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QPoint, QRect
from PyQt6.QtGui import (
    QKeyEvent,
    QMouseEvent,
    QPainter,
    QColor,
    QGuiApplication
)

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

        self.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents,
            True
        )

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.start_point = QPoint()
        self.end_point = QPoint()
        self.selecting = False
        self.capture_mode = False

    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        if a0 is None:
            return

        if a0.key() == Qt.Key.Key_Shift:
            self.capture_mode = True
            self.setAttribute(
                Qt.WidgetAttribute.WA_TransparentForMouseEvents,
                False
            )

            self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
            self.setFocus()

            self.setCursor(Qt.CursorShape.CrossCursor)
            self.update()
        elif a0.key() in (Qt.Key.Key_Q, Qt.Key.Key_Escape):
            self.exit_overlay()

    def keyReleaseEvent(self, a0: QKeyEvent | None) -> None:
        if a0 and a0.key() == Qt.Key.Key_Shift:
            self.capture_mode = False
            self.setAttribute(
                Qt.WidgetAttribute.WA_TransparentForMouseEvents,
                True
            )
            self.setCursor(Qt.CursorShape.ArrowCursor)
            self.update()

    def mousePressEvent(self, a0: QMouseEvent | None) -> None:
        if (
            a0
            and self.capture_mode
            and a0.button() == Qt.MouseButton.LeftButton
        ):
            self.start_point = a0.position().toPoint()
            self.end_point = self.start_point
            self.selecting = True
            self.update()

    def mouseMoveEvent(self, a0: QMouseEvent | None) -> None:
        if a0 and self.capture_mode and self.selecting:
            self.end_point = a0.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, a0: QMouseEvent | None) -> None:
        if (
            a0
            and self.capture_mode
            and a0.button() == Qt.MouseButton.LeftButton
        ):
            self.selecting = False
            rect = QRect(self.start_point, self.end_point).normalized()

            self.capture_region(rect)

            self.start_point = QPoint()
            self.end_point = QPoint()

            self.update()

    def capture_region(self, rect: QRect):
        screen = QGuiApplication.primaryScreen()
        if screen:
            screenshot = screen.grabWindow(
                0,  # type: ignore
                rect.x(),
                rect.y(),
                rect.width(),
                rect.height()
            )

            screenshot.save("capture.png")
            print("Captured region saved.")

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Dim whole screen
        painter.fillRect(self.rect(), QColor(0, 0, 0, 120))

        # Mode indicator
        if not self.capture_mode:
            painter.setPen(QColor(255, 255, 255))
            painter.drawText(
                40, 60,
                "Passive Mode (Hold SHIFT to capture)"
            )
            return

        painter.setPen(QColor(255, 255, 255))
        painter.drawText(40, 60, "Capture Mode")

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

        self.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents,
            True
        )

        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def exit_overlay(self):
        self.navigator.go(Page.MAIN)

        main_window = self.navigator.stack.window()
        if main_window:
            main_window.show()
            main_window.raise_()
            main_window.activateWindow()

        self.close()

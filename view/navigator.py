from PyQt6.QtWidgets import QStackedWidget
from enum import Enum

class Page(Enum):
    MAIN = 0
    SCAN = 1

class Navigator:
    def __init__(self, stack: QStackedWidget):
        self.stack = stack
        self.overlay = None

    def register_overlay(self, overlay):
        self.overlay = overlay

    def go(self, page: Page):
        if page != Page.SCAN:
            if self.overlay:
                self.overlay.hide()
            self.stack.setCurrentIndex(page.value)
        else:
            if self.overlay:
                self.overlay.showOverlay()
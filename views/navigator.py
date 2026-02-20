from PyQt6.QtWidgets import QStackedWidget
from enum import Enum

class Page(Enum):
    MAIN = 1
    SCAN = 2

class Navigator:
    def __init__(self, stack: QStackedWidget):
        self.stack = stack
        self.overlay = None
        self.pages = []

    def registerPage(self, page):
        self.pages.append(page)

    def registerOverlay(self, overlay):
        self.overlay = overlay

    def go(self, page: Page, data=None):
        if page != Page.SCAN:
            if self.overlay:
                self.overlay.hide()

            widget = self.pages[page.value - 1] # -1 because enum starts at 1 but list index starts at 0

            if data is not None and hasattr(widget, "setData"):
                widget.setData(data)

            self.stack.setCurrentIndex(page.value)
        else:
            if self.overlay:
                self.overlay.showOverlay()
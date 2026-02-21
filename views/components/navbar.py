from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui import QAction
from views.colors import (
    MENUBAR_BG, MENUBAR_ITEM_HOVER, MENUBAR_ITEM_PRESSED,
    MENU_BG, MENU_BORDER, MENU_ITEM_HOVER, MENU_SEPARATOR,
    TEXT_PRIMARY
)

class Navbar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet(f"""
            QMenuBar {{
                background-color: {MENUBAR_BG};
                color: {TEXT_PRIMARY};
                font-size: 11px;
                padding: 0px;
                spacing: 0px;
            }}
            QMenuBar::item {{
                background: transparent;
                padding: 4px 8px;
            }}
            QMenuBar::item:selected {{
                background-color: {MENUBAR_ITEM_HOVER};
            }}
            QMenuBar::item:pressed {{
                background-color: {MENUBAR_ITEM_PRESSED};
            }}
            QMenu {{
                background-color: {MENU_BG};
                color: {TEXT_PRIMARY};
                border: 1px solid {MENU_BORDER};
                padding: 2px;
            }}
            QMenu::item {{
                padding: 4px 25px 4px 8px;
                background: transparent;
            }}
            QMenu::item:selected {{
                background-color: {MENU_ITEM_HOVER};
            }}
            QMenu::separator {{
                height: 1px;
                background: {MENU_SEPARATOR};
                margin: 2px 0px;
            }}
        """)

        # Home menu
        home_menu = QMenu("Home", self)
        self.addMenu(home_menu)

        # Settings menu
        settings_menu = QMenu("Settings", self)

        theme_action = QAction("Theme", self)
        language_action = QAction("Language", self)
        about_action = QAction("About", self)

        settings_menu.addAction(theme_action)
        settings_menu.addAction(language_action)
        settings_menu.addSeparator()
        settings_menu.addAction(about_action)

        self.addMenu(settings_menu)
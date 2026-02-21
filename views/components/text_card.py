from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel, QScrollArea, QWidget
from PyQt6.QtCore import Qt
from views.colors import (
    BG_MEDIUM, BORDER_MEDIUM, TEXT_PRIMARY, 
    TEXT_SECONDARY, ACCENT_HOVER
)

class TextCard(QFrame):
    """A text display card with title and scrollable content"""
    
    def __init__(self, title: str, placeholder: str = ""):
        super().__init__()
        self.setMinimumHeight(180)
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {BG_MEDIUM};
                border: 1px solid {BORDER_MEDIUM};
                border-radius: 12px;
            }}
        """)

        card_layout = QVBoxLayout(self)
        card_layout.setContentsMargins(0, 0, 0, 0)
        card_layout.setSpacing(0)

        # Title section
        title_container = QFrame()
        title_container.setStyleSheet(f"""
            QFrame {{
                background-color: transparent;
                border: none;
                border-bottom: 1px solid {BORDER_MEDIUM};
                padding: 12px 20px;
            }}
        """)
        title_layout = QVBoxLayout(title_container)
        title_layout.setContentsMargins(0, 0, 0, 0)
        
        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            QLabel {{
                font-size: 12px;
                font-weight: 600;
                color: {TEXT_SECONDARY};
                background: transparent;
                border: none;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }}
        """)
        title_layout.addWidget(title_label)
        card_layout.addWidget(title_container)

        # Content section with scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(f"""
            QScrollArea {{
                border: none;
                background: transparent;
            }}
            QScrollBar:vertical {{
                background: {BG_MEDIUM};
                width: 8px;
                border-radius: 4px;
            }}
            QScrollBar::handle:vertical {{
                background: {BORDER_MEDIUM};
                border-radius: 4px;
                min-height: 20px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {ACCENT_HOVER};
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
        """)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 16, 20, 16)
        
        self.content_label = QLabel(placeholder)
        self.content_label.setWordWrap(True)
        self.content_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.content_label.setStyleSheet(f"""
            QLabel {{
                font-size: 15px;
                line-height: 1.6;
                color: {TEXT_PRIMARY};
                background: transparent;
                border: none;
            }}
        """)
        content_layout.addWidget(self.content_label)
        content_layout.addStretch()
        
        scroll_area.setWidget(content_widget)
        card_layout.addWidget(scroll_area)

    def setText(self, text: str):
        """Update the card's content text"""
        self.content_label.setText(text)

    def getText(self) -> str:
        """Get the current card content text"""
        return self.content_label.text()

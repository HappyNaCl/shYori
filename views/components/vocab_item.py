from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, pyqtSignal
from views.colors import (
    BG_LIGHT, BORDER_MEDIUM, TEXT_PRIMARY, 
    TEXT_SECONDARY, ACCENT_HOVER
)

class VocabItem(QFrame):
    """A clickable vocabulary item displaying word, reading, and meaning"""
    
    clicked = pyqtSignal(dict)  # Emits the vocab item data when clicked
    
    def __init__(self, item: dict):
        super().__init__()
        self.item = item
        
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(85)
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {BG_LIGHT};
                border: 1px solid {BORDER_MEDIUM};
            }}
            QFrame:hover {{
                background-color: {ACCENT_HOVER};
                border: 1px solid {ACCENT_HOVER};
            }}
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(3)
        
        # Word (kanji)
        word_label = QLabel(item['word'])
        word_label.setStyleSheet(f"""
            QLabel {{
                font-size: 17px;
                font-weight: 600;
                color: {TEXT_PRIMARY};
                background: transparent;
                border: none;
            }}
        """)
        layout.addWidget(word_label)
        
        # Reading (hiragana)
        reading_label = QLabel(item['reading'])
        reading_label.setStyleSheet(f"""
            QLabel {{
                font-size: 11px;
                color: {TEXT_SECONDARY};
                background: transparent;
                border: none;
            }}
        """)
        layout.addWidget(reading_label)
        
        # Meaning (English)
        meaning_label = QLabel(item['meaning'])
        meaning_label.setStyleSheet(f"""
            QLabel {{
                font-size: 12px;
                color: {TEXT_PRIMARY};
                background: transparent;
                border: none;
                margin-top: 2px;
            }}
        """)
        layout.addWidget(meaning_label)
    
    def mousePressEvent(self, a0):
        """Handle mouse press to emit clicked signal"""
        self.clicked.emit(self.item)
        super().mousePressEvent(a0)

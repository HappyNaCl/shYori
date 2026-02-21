from PyQt6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QHBoxLayout, 
    QSizePolicy
)
from PyQt6.QtCore import Qt
from views.navigator import Navigator, Page
from views.components import Navbar, TextCard, VocabularyCard
from views.colors import (
    BG_LIGHT, TEXT_PRIMARY, ACCENT_HOVER, ACCENT_PRESSED
)

class MainPage(QWidget):
    def __init__(self, navigator: Navigator):
        super().__init__()
        self.navigator = navigator

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        navbar = Navbar()
        main_layout.addWidget(navbar)

        # Main content area with horizontal layout
        content_layout = QHBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)

        # Left section - Original and Translated text (70% width)
        left_section = QVBoxLayout()
        left_section.setSpacing(20)

        # Original text card
        self.original_card = TextCard("Original Text", "これは日本語のテキストです。\nここに原文が表示されます。")
        left_section.addWidget(self.original_card)

        # Translated text card
        self.translated_card = TextCard("Translated Text", "This is Japanese text.\nThe translation will be displayed here.")
        left_section.addWidget(self.translated_card)

        # Scan button
        self.scan_button = QPushButton("Scan")
        self.scan_button.setFixedSize(140, 44)
        self.scan_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.scan_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {BG_LIGHT};
                color: {TEXT_PRIMARY};
                font-size: 14px;
                font-weight: 600;
                border: none;
                border-radius: 8px;
            }}
            QPushButton:hover {{
                background-color: {ACCENT_HOVER};
            }}
            QPushButton:pressed {{
                background-color: {ACCENT_PRESSED};
            }}
        """)
        self.scan_button.clicked.connect(lambda: self.navigator.go(Page.SCAN))
        left_section.addWidget(self.scan_button, alignment=Qt.AlignmentFlag.AlignCenter)

        left_section.addStretch()

        # Right section - Vocabulary sidebar (30% width)
        self.vocabulary_card = VocabularyCard()
        
        # Connect vocabulary item clicks
        for i in range(self.vocabulary_card.vocab_layout.count() - 1):
            item = self.vocabulary_card.vocab_layout.itemAt(i)
            if item and item.widget():
                item.widget().clicked.connect(self.onVocabClick) # type: ignore

        # Add sections to main content layout
        left_container = QWidget()
        left_container.setLayout(left_section)
        left_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        content_layout.addWidget(left_container, stretch=7)
        content_layout.addWidget(self.vocabulary_card, stretch=3)

        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)

    def onVocabClick(self, item: dict):
        """Handle vocabulary item click"""
        print(f"Clicked: {item['word']} - {item['meaning']}")

    def setData(self, data: str):
        """Update original text card with new data"""
        original_text = data.strip()
        if original_text:
            self.original_card.setText(original_text)
        else:
            self.original_card.setText("No text scanned yet.")
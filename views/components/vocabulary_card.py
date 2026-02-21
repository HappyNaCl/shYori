from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel, QScrollArea, QWidget
from views.colors import (
    BG_MEDIUM, BORDER_MEDIUM, TEXT_SECONDARY, 
    ACCENT_HOVER
)
from views.components.vocab_item import VocabItem

class VocabularyCard(QFrame):
    """A vocabulary sidebar displaying a list of clickable vocabulary items"""
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {BG_MEDIUM};
                border: 1px solid {BORDER_MEDIUM};
            }}
        """)

        card_layout = QVBoxLayout(self)
        card_layout.setContentsMargins(20, 16, 20, 20)
        card_layout.setSpacing(12)

        # Title
        title_label = QLabel("Vocabulary")
        title_label.setStyleSheet(f"""
            QLabel {{
                font-size: 13px;
                font-weight: 600;
                color: {TEXT_SECONDARY};
                background: transparent;
                border: none;
            }}
        """)
        card_layout.addWidget(title_label)

        # Scroll area for vocabulary items
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

        vocab_container = QWidget()
        self.vocab_layout = QVBoxLayout(vocab_container)
        self.vocab_layout.setContentsMargins(0, 0, 0, 0)
        self.vocab_layout.setSpacing(8)

        # Dummy vocabulary items
        vocab_items = [
            {"word": "日本語", "reading": "にほんご", "meaning": "Japanese language"},
            {"word": "テキスト", "reading": "てきすと", "meaning": "text"},
            {"word": "表示", "reading": "ひょうじ", "meaning": "display, show"},
            {"word": "翻訳", "reading": "ほんやく", "meaning": "translation"},
            {"word": "単語", "reading": "たんご", "meaning": "word, vocabulary"},
            {"word": "学習", "reading": "がくしゅう", "meaning": "learning, study"},
        ]

        for item in vocab_items:
            self.addVocabItem(item)

        self.vocab_layout.addStretch()
        scroll_area.setWidget(vocab_container)
        card_layout.addWidget(scroll_area)

    def addVocabItem(self, item: dict, on_click_callback=None):
        """Add a vocabulary item to the list"""
        vocab_item = VocabItem(item)
        if on_click_callback:
            vocab_item.clicked.connect(on_click_callback)
        self.vocab_layout.insertWidget(self.vocab_layout.count() - 1, vocab_item)
        return vocab_item

    def clearVocabItems(self):
        """Remove all vocabulary items from the list"""
        while self.vocab_layout.count() > 1:
            item = self.vocab_layout.takeAt(0)
            if item and item.widget() is not None:
                item.widget().deleteLater() # type: ignore

    def setVocabItems(self, items: list[dict], on_click_callback=None):
        """Replace all vocabulary items with a new list"""
        self.clearVocabItems()
        for item in items:
            self.addVocabItem(item, on_click_callback)

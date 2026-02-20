from manga_ocr import MangaOcr
from PyQt6.QtGui import QPixmap
from uuid import uuid4
import tempfile

class TranslatorController:
    def __init__(self) -> None:
        self.ocr = None
        self._temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = self._temp_dir.name

        pass

    def initialize(self):
        self.ocr = MangaOcr()

    def translate(self, image: QPixmap) -> str:
        uuid_str = str(uuid4())
        image.save(f"{self.temp_path}/{uuid_str}.png")
        if self.ocr:
            text = self.ocr(f"{self.temp_path}/{uuid_str}.png")
            print(text)
            return text
        return ""

    def cleanup(self):
        self._temp_dir.cleanup()

translator_controller = TranslatorController()
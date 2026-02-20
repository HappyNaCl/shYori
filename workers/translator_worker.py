from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QPixmap

class TranslatorWorker(QObject):
    finished = pyqtSignal()
    result = pyqtSignal(str)

    def run(self, image: QPixmap):
        from controller import translator_controller
        text = translator_controller.translate(image)
        self.result.emit(text)
        self.finished.emit()
from PyQt6.QtCore import QObject, pyqtSignal

class InitWorker(QObject):
    finished = pyqtSignal()

    def run(self):
        from controller import translator_controller
        translator_controller.initialize()
        self.finished.emit()
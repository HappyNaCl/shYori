from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget
from controller import translator_controller
from workers import InitWorker
from views.pages import MainPage, ScanPage, LoadingPage
from views.navigator import Navigator
from PyQt6.QtCore import Qt, QThread

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()
        self.navigator = Navigator(self.stack)

        self.loading_page = LoadingPage()
        self.main_page = MainPage(self.navigator)
        self.overlay_page = ScanPage(self.navigator)

        self.navigator.registerPage(self.main_page)
        self.navigator.registerPage(self.overlay_page)

        self.navigator.registerOverlay(self.overlay_page)

        self.stack.addWidget(self.loading_page)  # index 0
        self.stack.addWidget(self.main_page)  # index 1

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack)
        self.setLayout(main_layout)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setWindowTitle("shYori")

        (width, height) = self.getScreenDimension()
        self.setMinimumSize(width, height)
        
        self.showMaximized()

        self.startInitialization()

    def startInitialization(self):
        self.worker_thread = QThread()

        self.worker = InitWorker()

        self.worker.moveToThread(self.worker_thread)

        self.worker_thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.onInitializationFinished)

        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)

        self.worker_thread.start()

    def onInitializationFinished(self):
        self.stack.setCurrentWidget(self.main_page)

    def closeEvent(self, a0: QCloseEvent | None) -> None:
        if translator_controller != None:
            translator_controller.cleanup()
        
        return super().closeEvent(a0)

    def getScreenDimension(self) -> tuple[int, int]:
        screen = self.screen()
        if screen != None:
            geometry = screen.availableGeometry()
            return (int(geometry.width() * 0.8), int(geometry.height() * 0.8))

        return (1600, 850)
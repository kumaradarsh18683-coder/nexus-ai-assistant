from PySide6.QtCore import QThread, Signal
from ai import speak


class SpeechWorker(QThread):

    finished = Signal()

    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):
        speak(self.text)
        self.finished.emit()
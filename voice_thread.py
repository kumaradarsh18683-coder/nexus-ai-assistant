from PySide6.QtCore import QThread, Signal
from voice import listen


class VoiceThread(QThread):

    heard = Signal(str)

    def run(self):

        while not self.isInterruptionRequested():

            text = listen()

            if text:
                self.heard.emit(text)
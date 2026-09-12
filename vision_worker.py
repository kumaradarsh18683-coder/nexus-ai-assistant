from PySide6.QtCore import QThread, Signal

from gemini import ask_gemini_image


class VisionWorker(QThread):

    finished = Signal(str)

    def __init__(self, image, prompt):
        super().__init__()
        self.image = image
        self.prompt = prompt

    def run(self):
        answer = ask_gemini_image(self.image, self.prompt)
        self.finished.emit(answer)
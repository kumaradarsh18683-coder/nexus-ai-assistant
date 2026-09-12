from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QTimer


class Waveform(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(180, 220)

        self.values = [20, 40, 60, 30, 70, 90, 50, 80, 40, 60]

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)

        self.set_status("READY")

    # ================= STATUS =================

    def set_status(self, status):

        status = status.upper()

        if status == "READY":
            self.timer.start(120)

        elif status == "LISTENING":
            self.timer.start(35)

        elif status == "THINKING":
            self.timer.start(70)

        elif status == "SPEAKING":
            self.timer.start(20)

        else:
            self.timer.start(120)

    # ================= ANIMATION =================

    def animate(self):

        self.values = self.values[1:] + [self.values[0]]

        self.update()

    # ================= DRAW =================

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(QColor("#1FD8FF"))
        pen.setWidth(4)

        painter.setPen(pen)

        x = 20

        for h in self.values:

            painter.drawLine(
                x,
                110 - h // 2,
                x,
                110 + h // 2
            )

            x += 15
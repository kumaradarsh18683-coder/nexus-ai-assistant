from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QRadialGradient
)
from PySide6.QtCore import Qt, QTimer

class AICore(QWidget):

    def __init__(self):
        super().__init__()
        self.status = "READY"

        self.setFixedSize(360, 360)

        self.ring_color = QColor("#00D9FF")
        self.glow_color = QColor("#00CFFF")

        self.pulse = 0
        self.direction = 1

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(30)

                
    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        gradient = QRadialGradient(180, 180, 120)

        gradient.setColorAt(0, QColor(80,255,255,255))
        gradient.setColorAt(0.6, QColor(0,180,255,80))
        gradient.setColorAt(1, QColor(0,0,0,0))

        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(60, 60, 240, 240)

    
        if self.status == "READY":
            color = QColor("#00D9FF")

        elif self.status == "LISTENING":
            color = QColor("#00FF99")

        elif self.status == "THINKING":
            color = QColor("#FFD93D")

        else:
            color = QColor("#00FFFF")
        pen = QPen(color)
        pen.setCapStyle(Qt.RoundCap)
        pen.setWidth(4)

        

        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)

        # Outer Ring
        p = self.pulse

        painter.drawEllipse(
            30-p,
            30-p,
            300+p*2,
            300+p*2
        ) 
        # Middle Ring
        painter.drawEllipse(
            60-p//2,
            60-p//2,
            240+p,
            240+p
        )
        # Inner Ring
        painter.drawEllipse(
            90-p//3,
            90-p//3,
            180+p//2,
            180+p//2
        )

        # Center Bright Core
        gradient2 = QRadialGradient(180, 180, 45)

        gradient2.setColorAt(0, color.lighter(150))
        gradient2.setColorAt(1, color)

        painter.setBrush(gradient2)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(145, 145, 70, 70)

        # -------- MIC BODY --------

       # pen = QPen(QColor("white"))
        #pen.setWidth(3)

       # painter.setPen(pen)
        #painter.setBrush(Qt.NoBrush)

        # Mic Head
       # painter.drawRoundedRect(170, 155, 20, 35, 10, 10)

        # Mic Stem
       # painter.drawLine(180, 190, 180, 205)

        # Mic Base
       # painter.drawArc(165, 185, 30, 30, 0 * 16, 180 * 16)

        # Bottom Line
      #  painter.drawLine(170, 215, 190, 215)

        # Extra Inner Glow
        gradient3 = QRadialGradient(180, 180, 25)

        gradient3.setColorAt(0, QColor("#FFFFFF"))
        gradient3.setColorAt(0.3, QColor("#6CF8FF"))
        gradient3.setColorAt(1, QColor("#24CFFF"))

        painter.setBrush(gradient3)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(160, 160, 40, 40)
                        

    def animate(self):

        if self.status == "READY":
            speed = 1
            limit = 8

        elif self.status == "LISTENING":
            speed = 2
            limit = 12

        elif self.status == "THINKING":
            speed = 2
            limit = 16

        elif self.status == "SPEAKING":
            speed = 3
            limit = 20

        self.pulse += self.direction * speed

        if self.pulse >= limit:
            self.direction = -1

        elif self.pulse <= 0:
            self.direction = 1

        self.update()

    def set_status(self, status):
        self.status = status
        self.update()
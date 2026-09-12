from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class StatusLabel(QLabel):

    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setFixedWidth(280)
        self.set_status("READY")

    def set_status(self, status):

        colors = {
            "READY": "#43D9FF",
            "LISTENING": "#00FF99",
            "THINKING": "#FFD93D",
            "SPEAKING": "#FF6B6B"
        }

        icons = {
            "READY": "🟢",
            "LISTENING": "🎤",
            "THINKING": "🧠",
            "SPEAKING": "🔊"
        }

        color = colors.get(status, "#43D9FF")
        icon = icons.get(status, "🟢")

        self.setText(f"{icon} {status}")

        self.setStyleSheet(f"""
        QLabel{{
            color:{color};
            font-size:18px;
            font-weight:bold;
            padding:10px;
            border:2px solid #00D9FF;
            border-radius:12px;
            background:#0B1220;
        }}
        """)


def create_status():
    return StatusLabel()
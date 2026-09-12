from PySide6.QtWidgets import QLabel, QFrame, QVBoxLayout
from PySide6.QtCore import Qt


def create_header():

    frame = QFrame()

    layout = QVBoxLayout(frame)

    layout.setContentsMargins(0, 5, 0, 5)
    layout.setSpacing(2)

    layout.setAlignment(Qt.AlignCenter)

    title = QLabel("NEXUS AI")

    title.setAlignment(Qt.AlignCenter)

    title.setStyleSheet("""
        color:#43D9FF;
        font-size:48px;
        font-weight:bold;
    """)

    subtitle = QLabel("Your Personal AI Assistant")

    subtitle.setAlignment(Qt.AlignCenter)

    subtitle.setStyleSheet("""
        color:#9FB8D6;
        font-size:18px;
    """)

    layout.addWidget(title)
    layout.addWidget(subtitle)

    return frame
import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)
from assistant_thread import AssistantThread
from vision_worker import VisionWorker
from speech_worker import SpeechWorker
from ui.chat import add_message
from PySide6.QtCore import Qt, QTimer
from PySide6.QtCore import Qt
from ui.status import create_status
from ui.header import create_header
from ui.dashboard import create_dashboard
from ui.core import AICore
from ui.chat import create_chat
from ui.waveform import Waveform
from PySide6.QtGui import QCloseEvent


class NexusUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nexus AI")
        self.setWindowFlags(Qt.Window)
        self.resize(1600, 900)
        self.setMinimumSize(1200, 700)

        self.setStyleSheet("""
            QWidget{
                background:#050816;
            }
        """)

        # ================= MAIN LAYOUT =================

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(20,20,20,20)
        main_layout.setSpacing(20)

        # Header
        main_layout.addWidget(create_header())

        # Dashboard
        self.dashboard = create_dashboard()
        main_layout.addWidget(self.dashboard)

        # ================= CENTER =================

        center = QHBoxLayout()
        center.setSpacing(40)

        # ---------- Left Wave ----------

        self.left_wave = Waveform()

        # ---------- AI Core ----------

        core_layout = QVBoxLayout()
        core_layout.setAlignment(Qt.AlignCenter)

        self.core = AICore()
        self.status = create_status()

        core_layout.addWidget(self.core)
        core_layout.addSpacing(10)
        core_layout.addWidget(self.status)

        # ---------- Right Wave ----------

        self.right_wave = Waveform()

        # ---------- Chat ----------

        self.chat = create_chat()
        self._vision_question = ""

        # AI Section

        ai_section = QHBoxLayout()

        ai_section.addWidget(self.left_wave)

        ai_section.addLayout(core_layout)

        ai_section.addWidget(self.right_wave)

        center.addLayout(ai_section,1)

        center.addWidget(self.chat,2)

        main_layout.addLayout(center)

        self.setLayout(main_layout)

        # ---------------- Assistant Thread ----------------

        self.assistant = AssistantThread()

        self.assistant.status_changed.connect(
    lambda status: (
        self.status.set_status(status),
        self.core.set_status(status),
        self.left_wave.set_status(status),
        self.right_wave.set_status(status),
        self.dashboard.set_status(status)
    )
        )

        self.assistant.user_message.connect(
            lambda msg: add_message(self.chat, "user", msg)
        )

        self.assistant.ai_message.connect(
            lambda msg: add_message(self.chat, "ai", msg)
        )

        self.assistant.start()
        self.assistant.vision_request.connect(self.handle_vision)
        self.assistant.status_changed.emit("READY")
        self._vision_question = ""  
        
    
    def handle_vision(self, question):

        self._vision_question = question

        self.status.set_status("THINKING")
        self.core.set_status("THINKING")
        self.left_wave.set_status("THINKING")
        self.right_wave.set_status("THINKING")
        self.dashboard.set_status("THINKING")

        self.hide()

        QTimer.singleShot(700, self.capture_and_restore)


    def capture_and_restore(self):

        from vision import capture_screen
        from gemini import ask_gemini_image
        from ai import speak

        image = capture_screen()

        self.show()
        self.raise_()
        self.activateWindow()

        if (
            "error" in self._vision_question
            or "bug" in self._vision_question
            or "code" in self._vision_question
        ):

            prompt = """
Screen me agar terminal ya VS Code me koi Python error hai to:

1. Error ka naam batao.
2. Error kis wajah se aaya.
3. Exact solution batao.
4. Agar code me bug hai to us line ko explain karo.

Simple Hinglish me jawab do.
"""

        else:

            prompt = """
    Screen me jo bhi dikh raha hai usko simple Hinglish me explain karo.
    """

        self.worker = VisionWorker(image, prompt)

        self.worker.finished.connect(self.on_vision_finished)

        self.worker.start()
   
    def on_vision_finished(self, answer):

        add_message(self.chat, "ai", answer)

        self.status.set_status("SPEAKING")
        self.core.set_status("SPEAKING")
        self.left_wave.set_status("SPEAKING")
        self.right_wave.set_status("SPEAKING")
        self.dashboard.set_status("SPEAKING")

        self.speech_worker = SpeechWorker(answer)
        self.speech_worker.finished.connect(self.on_speech_finished)
        self.speech_worker.start()
   
    def on_speech_finished(self):

        self.assistant.listening_enabled = True

        self.status.set_status("READY")
        self.core.set_status("READY")
        self.left_wave.set_status("READY")
        self.right_wave.set_status("READY")
        self.dashboard.set_status("READY")

    def closeEvent(self, event):

        self.assistant.stop()

        self.assistant.wait(7000)

        event.accept()

               
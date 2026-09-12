from PySide6.QtCore import QThread, Signal

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.append(str(ROOT))

from ai import speak
from commands import execute_command
from gemini import ask_gemini
from voice import listen


class AssistantThread(QThread):

    user_message = Signal(str)
    ai_message = Signal(str)
    status_changed = Signal(str)
    vision_request = Signal(str)

    def __init__(self):
        super().__init__()
        self.awake = False
        self.listening_enabled = True

    def stop(self):
        self.requestInterruption()

    def process_question(self, question):

        question = question.lower().strip()

        self.user_message.emit(question)

        # ---------------- Wake Up ----------------

        if not self.awake:

            if "wake up nexus" in question:

                self.awake = True

                self.status_changed.emit("SPEAKING")

                reply = (
                    "Welcome back, Boss. "
                    "All systems are online. "
                    "How may I assist you?"
                )

                self.ai_message.emit(reply)

                speak(reply)

                self.status_changed.emit("READY")

            return

        # ---------------- Sleep ----------------

        if "go to sleep" in question:

            self.awake = False

            self.status_changed.emit("SPEAKING")

            reply = "Entering sleep mode."

            self.ai_message.emit(reply)

            speak(reply)

            self.status_changed.emit("READY")

            return

        # ---------------- Vision ----------------

        if (
            "screen me kya hai" in question
            or "code ko fix" in question
            or "fix code" in question
            or "error fix" in question
            or "bug fix" in question
            or "debug" in question
            or "screen mein kya hai" in question
            or "screen dekho" in question
            or "code ko fix karo" in question
            or "code fix karo" in question
            or "fix code" in question
            or "fix this code" in question
            or "screen check karo" in question
            or "analyze screen" in question
            or "is code ko fix karo" in question
            or "is error ko fix karo" in question
            or "is error ko solve karo" in question
            or "error ko fix karo" in question
            or "bug dhoondo" in question
            or "code check karo" in question
        ):

            

            self.listening_enabled = False

            self.status_changed.emit("THINKING")

            self.vision_request.emit(question)

            return

        # ---------------- Normal Commands ----------------

        self.status_changed.emit("THINKING")

        answer = execute_command(question)

        if answer is None:
            answer = "Mujhe samajh nahi aaya."

        if "samajh nahi aayi" in answer:
            answer = ask_gemini(question)
            

        if not answer:
            answer = "Sorry, abhi jawab generate nahi kar pa raha."

        answer = answer[:250]

        self.status_changed.emit("SPEAKING")

        self.ai_message.emit(answer)

        speak(answer)

        self.status_changed.emit("READY")

    def run(self):

     while not self.isInterruptionRequested():

        if not self.listening_enabled:
            self.msleep(100)
            continue

        self.status_changed.emit("READY")

        question = listen()

        if not question:
            continue

        self.process_question(question)
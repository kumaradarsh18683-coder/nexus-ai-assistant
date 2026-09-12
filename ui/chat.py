from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QTextEdit
)

from PySide6.QtCore import Qt


def create_chat():

    frame = QFrame()

    frame.setMinimumWidth(700)
    frame.setMinimumHeight(450)

    frame.setStyleSheet("""
    QFrame{
        background:#0B1220;
        border:2px solid #00D9FF;
        border-radius:18px;
    }
    """)

    layout = QVBoxLayout(frame)
    layout.setContentsMargins(18,18,18,18)
    layout.setSpacing(12)

    # ---------------- TITLE ----------------

    title = QLabel("💬 LIVE CONVERSATION")
    subtitle = QLabel("Nexus is ready to help you.")

    subtitle.setAlignment(Qt.AlignCenter)

    subtitle.setStyleSheet("""
    QLabel{
        color:#9AB9D7;
        font-size:14px;
        border:none;
        padding-bottom:8px;
    }
    """)
    title.setAlignment(Qt.AlignCenter)

    title.setStyleSheet("""
    QLabel{
        color:#43D9FF;
        font-size:24px;
        font-weight:bold;
        border:none;
    }
    """)

    # ---------------- CHAT AREA ----------------

    chat = QTextEdit()
    frame.chat = chat

    chat.setObjectName("chatBox")
    chat.setReadOnly(True)

    chat.setStyleSheet("""
    QTextEdit#chatBox{

        background:#0B1220;
        color:white;

        border:none;

        font-size:18px;
        line-height:1.6;

        padding:20px;

        selection-background-color:#00D9FF;
    }

    QScrollBar:vertical{
        background:#0B1220;
        width:8px;
        border:none;
    }

    QScrollBar::handle:vertical{
    background:#27DFFF;
    border-radius:4px;
    min-height:40px;
    }

    QScrollBar::add-line:vertical,
    QScrollBar::sub-line:vertical{
        height:0px;
    }
    """)

    # ---------------- DEMO MESSAGES ----------------

    chat.append("<span style='color:#44D9FF;font-size:18px;'>🤖 <b>Nexus</b></span>")
    chat.append("<span style='color:white;'>Nexus AI is Online.</span><br>")

    chat.append("<span style='color:#B785FF;font-size:18px;'>👤 <b>You</b></span>")
    chat.append("<span style='color:white;'>Hello Nexus</span><br>")

    chat.append("<span style='color:#44D9FF;font-size:18px;'>🤖 <b>Nexus</b></span>")
    chat.append("<span style='color:white;'>Hello Adarsh! How can I help you today?</span><br>")

    layout.addWidget(title)
    layout.addWidget(subtitle)
    layout.addWidget(chat)


    return frame

def add_message(frame, sender, message):

    chat = frame.chat

    if sender == "user":

        chat.append(f"""
<span style='color:#B785FF;font-size:18px;'>
👤 <b>You</b>
</span>

<span style='color:white;'>
{message}
</span><br>
""")

    else:

        chat.append(f"""
<span style='color:#44D9FF;font-size:18px;'>
🤖 <b>Nexus</b>
</span>

<span style='color:white;'>
{message}
</span><br>
""")

    chat.verticalScrollBar().setValue(
        chat.verticalScrollBar().maximum()
    )
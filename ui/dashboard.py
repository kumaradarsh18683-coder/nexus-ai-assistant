from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)
import psutil
from datetime import datetime

from PySide6.QtCore import Qt, QTimer



def create_dashboard():

    frame = QFrame()

    # Height kam rakhi hai taki AI Core aur Chat ke liye space bache
    frame.setMinimumHeight(170)
    frame.setMaximumHeight(220)

    frame.setStyleSheet("""
    QFrame{
        background:#0B1220;
        border:2px solid #00D9FF;
        border-radius:18px;
    }

    QLabel{
        border:none;
    }
    """)

    main = QVBoxLayout(frame)
    content = QHBoxLayout()
    content.setSpacing(80)

    left_layout = QVBoxLayout()
    right_layout = QVBoxLayout()

    content.addLayout(left_layout, 2)
    content.addLayout(right_layout, 1)

    main.setContentsMargins(20,20,20,20)
    main.setSpacing(12)

    # ---------------- TOP ----------------

    top = QHBoxLayout()

    title = QLabel("🤖 NEXUS AI ONLINE")

    title.setStyleSheet("""
    color:#43D9FF;
    font-size:22px;
    font-weight:bold;
    """)

    session = QLabel("SESSION : NX-3006")

    session.setStyleSheet("""
    color:#7EDFFF;
    font-size:16px;
    """)

    top.addWidget(title)
    top.addStretch()
    top.addWidget(session)

    # ---------------- INFO ----------------

    welcome = QLabel()
    current_status = "READY"

    def update_dashboard():

            current_time = datetime.now().strftime("%I:%M:%S %p")
            current_date = datetime.now().strftime("%d-%m-%Y")

            cpu = psutil.cpu_percent()

            ram = psutil.virtual_memory().percent

            disk = psutil.disk_usage("/").percent

            battery = psutil.sensors_battery()

            if battery:
                battery_text = f"{battery.percent}%"
            else:
                battery_text = "N/A"

            welcome.setText(f"""👋 Welcome Back, Boss

            🟢 Status            {current_status}
            🎤 Voice Engine      ONLINE
            🧠 AI Engine         CONNECTED
            💾 Memory            LOADED
            """)

            live_info.setText(f"""🕒 Time      {current_time}

            💻 CPU       {cpu}%
            🧠 RAM       {ram}%
            💾 Disk      {disk}%
            🔋 Battery   {battery_text}
            🌐 Internet  Online
            """)


    welcome.setStyleSheet("""
        color:white;
        font-size:15px;
        line-height:1.6;
        """)

    welcome.setAlignment(Qt.AlignLeft | Qt.AlignTop)

    main.addLayout(top)
    left_layout.addWidget(welcome)
    main.addLayout(content)

    live_info = QLabel()

    live_info.setStyleSheet("""
        color:#7EDFFF;
        font-size:15px;
        line-height:1.7;
        border:none;
        """)

    live_info.setAlignment(Qt.AlignTop)
    live_info.setMinimumWidth(280)

    right_layout.addWidget(live_info)

    timer = QTimer(frame)

    timer.timeout.connect(update_dashboard)

    timer.start(1000)
    update_dashboard()

    def set_status(status):
        nonlocal current_status
        current_status = status
        update_dashboard()

    frame.set_status = set_status

    return frame
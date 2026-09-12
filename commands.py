import webbrowser
import os
import re
import psutil
import time
import pyautogui
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from datetime import datetime

from whatsapp import (
    send_whatsapp,
    whatsapp_call,
    whatsapp_video_call
)

from memory import remember, recall
from memory_commands import handle_memory

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "github": "https://github.com",
    "chatgpt": "https://chatgpt.com",
    "amazon": "https://www.amazon.in",
    "flipkart": "https://www.flipkart.com",
    "reddit": "https://www.reddit.com",
    "netflix": "https://www.netflix.com"
}

FOLDERS = {
    "desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
    "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
    "documents": os.path.join(os.path.expanduser("~"), "Documents"),
    "pictures": os.path.join(os.path.expanduser("~"), "Pictures"),
    "videos": os.path.join(os.path.expanduser("~"), "Videos"),
    "music": os.path.join(os.path.expanduser("~"), "Music")
}


def get_volume():
    devices = AudioUtilities.GetSpeakers()

    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )

    return cast(interface, POINTER(IAudioEndpointVolume))


def execute_command(command):

    command = command.lower().strip()

    memory_response = handle_memory(command)

    if memory_response:
        return memory_response

    
    # ==========================
    # Maths
    # ==========================


    match = re.search(r'(\d+)\s*([\+\-\*/])\s*(\d+)', command)

    if match:

        a = int(match.group(1))
        op = match.group(2)
        b = int(match.group(3))

        if op == "+":
            return f"Answer is {a+b}"

        elif op == "-":
            return f"Answer is {a-b}"

        elif op == "*":
            return f"Answer is {a*b}"

        elif op == "/":

            if b == 0:
                return "Zero se divide nahi kar sakte."

            return f"Answer is {a/b}"

    # ==========================
    # Open Apps
    # ==========================

    elif command.startswith("open chrome"):

        os.system("start chrome")

        return "Chrome khol raha hoon."

    elif "open notepad" in command:

        os.system("start notepad")

        return "Notepad khol raha hoon."

    elif "open calculator" in command:

        os.system("start calc")

        return "Calculator khol raha hoon."

    elif "open explorer" in command:

        os.system("start explorer")

        return "File Explorer khol raha hoon."

    elif "open vscode" in command or "open vs code" in command:

        os.system("code")

        return "VS Code khol raha hoon."

    elif "whatsapp" in command:

        os.system(
            r"start shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"
        )

        return "WhatsApp khol raha hoon."
    
    # ==========================
    # Close Apps
    # ==========================

    elif "close chrome" in command:

        os.system("taskkill /f /im chrome.exe >nul 2>&1")

        return "Chrome band kar diya."

    elif "close vscode" in command or "close vs code" in command:

        os.system("taskkill /f /im Code.exe >nul 2>&1")

        return "VS Code band kar diya."

    elif "close notepad" in command:

        os.system("taskkill /f /im notepad.exe >nul 2>&1")

        return "Notepad band kar diya."

    elif "close calculator" in command:

        os.system("taskkill /f /im CalculatorApp.exe >nul 2>&1")
        os.system("taskkill /f /im calc.exe >nul 2>&1")

        return "Calculator band kar diya."

    elif "close explorer" in command:

        os.system("taskkill /f /im explorer.exe")

        os.system("start explorer")

        return "Explorer restart kar diya."
    
    elif "close youtube" in command:

        pyautogui.hotkey("ctrl", "w")
        time.sleep(0.3)

        return "YouTube ka active tab band kar diya."
    
    elif "close current tab" in command or "close tab" in command:

        pyautogui.hotkey("ctrl", "w")
        time.sleep(0.3)

        return "Current tab band kar diya."
    
    elif "close edge" in command or "close browser" in command:

        os.system("taskkill /f /im msedge.exe >nul 2>&1")

        return "Microsoft Edge band kar diya."
        
    elif "close github" in command:

        pyautogui.hotkey("ctrl", "w")
        time.sleep(0.3)

        return "GitHub ka active tab band kar diya."
    # ==========================
    # Browser
    # ==========================

    elif command.startswith("open "):

        website = command.replace("open", "").strip().lower()

        website = website.replace("chat gpt", "chatgpt")
        website = website.replace("git hub", "github")
        website = website.replace("linked in", "linkedin")
        website = website.replace("you tube", "youtube")
        website = website.replace("face book", "facebook")

        if website in WEBSITES:

           webbrowser.open(WEBSITES[website])

           return f"{website.title()} khol raha hoon." 

    

   
    elif (
        "search" in command
        or "google par search karo" in command
        or "google per search karo" in command
    ):
        


        query = command

        query = query.replace(
            "google par search karo", ""
        )

        query = query.replace(
            "google per search karo", ""
        )

        query = query.replace(
            "search", ""
        )

        query = query.replace(
            "google", ""
        )

        query = query.strip()

        if query:

            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )

            return f"{query} Google par search kar raha hoon."

    elif command == "google":

        webbrowser.open("https://www.google.com")

        return "Google khol raha hoon."

    elif "play" in command:

        song = command.replace("play", "")
        song = song.replace("on youtube", "")
        song = song.strip()

        if not song:
            return "Kaunsa gaana play karna hai?"

        try:
            import pywhatkit
            pywhatkit.playonyt(song)
            return f"{song} YouTube par play kar raha hoon."

        except Exception as e:
            print("PyWhatKit Error:", e)
            return "YouTube play nahi ho paaya. Internet ya connection me problem lag rahi hai."

    elif "youtube" in command:

            webbrowser.open("https://www.youtube.com")

            return "YouTube khol raha hoon."
    
        # ==========================
    # Vision AI
    # ==========================

    

    
    
    # ==========================
    # Screenshot
    # ==========================

    elif "screenshot" in command:

        image = pyautogui.screenshot()

        image.save("screenshot.png")

        return "Screenshot le liya hai."

    # ==========================
    # Volume
    # ==========================

    elif "volume up" in command:

        volume = get_volume()

        current = volume.GetMasterVolumeLevelScalar()

        volume.SetMasterVolumeLevelScalar(
            min(current + 0.1, 1.0),
            None
        )

        return "Volume badha diya."

    elif "volume down" in command:

        volume = get_volume()

        current = volume.GetMasterVolumeLevelScalar()

        volume.SetMasterVolumeLevelScalar(
            max(current - 0.1, 0.0),
            None
        )

        return "Volume kam kar diya."

    elif "unmute" in command or "un mute" in command:

        volume = get_volume()

        volume.SetMute(0, None)

        return "Volume unmute kar diya."

    elif "mute" in command:

        volume = get_volume()

        volume.SetMute(1, None)

        return "Volume mute kar diya."

    # ==========================
    # WhatsApp
    # ==========================

    elif command.startswith("video call "):

        contact = command.replace(
            "video call ",
            ""
        ).strip()

        whatsapp_video_call(contact)

        return f"{contact} ko video call kar raha hoon."

    elif command.startswith("call "):

        contact = command.replace(
            "call ",
            ""
        ).strip()

        whatsapp_call(contact)

        return f"{contact} ko call kar raha hoon."

    elif command.startswith("message "):

        text = command.replace(
            "message ",
            "",
            1
        )

        parts = text.split(" ", 1)

        if len(parts) < 2:
            return "Contact aur message bolo."

        contact = parts[0].strip()

        message = parts[1].strip()

        send_whatsapp(
            contact,
            message
        )

        return f"{contact} ko message bhej diya."
    
    # ==========================
# Battery
# ==========================

    elif (
        "battery" in command
        or "battery percentage" in command
        or "battery status" in command
    ):

        battery = psutil.sensors_battery()

        if battery is None:
            return "Battery information available nahi hai."

        percent = battery.percent

        if battery.power_plugged:
            status = "Charging ho rahi hai."
        else:
            status = "Charging nahi ho rahi."

        return f"Battery {percent}% hai. {status}"
    
    # ==========================
# System Information
# ==========================

    elif "system info" in command:

        cpu = psutil.cpu_percent(interval=1)

        ram = psutil.virtual_memory()

        disk = psutil.disk_usage("C:\\")

        free_gb = round(disk.free / (1024**3), 2)

        return (
            f"CPU usage {cpu} percent hai. "
            f"RAM usage {ram.percent} percent hai. "
            f"C drive me {free_gb} GB free hai."
        )

    elif "cpu usage" in command:

        cpu = psutil.cpu_percent(interval=1)

        return f"CPU usage {cpu} percent hai."

    elif "ram usage" in command:

        ram = psutil.virtual_memory()

        return f"RAM usage {ram.percent} percent hai."

    elif "disk usage" in command:

        disk = psutil.disk_usage("C:\\")

        free_gb = round(disk.free / (1024**3), 2)

        return f"C drive me {free_gb} GB free hai."

    # ==========================
    # Time
    # ==========================

    elif "time" in command:

        current_time = datetime.now().strftime("%H:%M")

        return f"Abhi time hai {current_time}"
    
        
    # ==========================
    # Greetings
    # ==========================

    elif command == "hello" or command == "hi":

        return "Hello Adarsh."

    elif command == "how are you":

        return "Main bilkul theek hoon Adarsh."

    elif "your name" in command:

        return "Mera naam Nexus AI hai."

    elif "thank you" in command:

        return "Welcome Adarsh."

    elif "who made you" in command:

        return "Mujhe Adarsh ne Python me banaya hai."

    elif command == "bye":

        return "Bye Adarsh."

    # ==========================
    # Default
    # ==========================

    else:

        return "Mujhe ye command samajh nahi aayi."
    
 
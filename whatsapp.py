import os
import time
import pyautogui
import pyperclip
import pygetwindow as gw


def send_whatsapp(contact, message):

    # WhatsApp kholo
    os.system(r"start shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
    time.sleep(4)

    # WhatsApp window focus
    try:
        wins = gw.getWindowsWithTitle("WhatsApp")
        if wins:
            wins[0].activate()
            time.sleep(1)
    except:
        pass

    # Search box par click
    pyautogui.moveTo(324, 187, duration=1)
    pyautogui.click()
    print("Search box clicked")

    # Search clear
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")

    print("Searching contact")

    # Contact search
    pyperclip.copy(contact)
    pyautogui.hotkey("ctrl", "v")

    time.sleep(2)

    print("Opening chat")

    # Pehla result open
    pyautogui.press("down")
    time.sleep(0.5)
    pyautogui.press("enter")

    time.sleep(1)

    print("Typing message")

    # Message paste
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")

    time.sleep(0.5)

    print("Sending message")

    # Send
    pyautogui.press("enter")

    return True

def whatsapp_call(contact):

    # WhatsApp kholo
    os.system(r"start shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
    time.sleep(4)

    # Window focus
    try:
        wins = gw.getWindowsWithTitle("WhatsApp")
        if wins:
            wins[0].activate()
            time.sleep(1)
    except:
        pass

    # Search box
    pyautogui.moveTo(324, 187, duration=1)
    pyautogui.click()

    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")

    # Contact search
    pyperclip.copy(contact)
    pyautogui.hotkey("ctrl", "v")

    time.sleep(2)

    pyautogui.press("down")
    time.sleep(0.5)
    pyautogui.press("enter")

    # Chat open hone do
    time.sleep(2)

    print("Chat open ho gayi.")
        # Voice call button par click
    pyautogui.moveTo(1273, 114, duration=1)
    pyautogui.click()

    print("Voice call start kar di.")

    return True

def whatsapp_video_call(contact):

    # WhatsApp kholo
    os.system(r"start shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
    time.sleep(4)

    # Window focus
    try:
        wins = gw.getWindowsWithTitle("WhatsApp")
        if wins:
            wins[0].activate()
            time.sleep(1)
    except:
        pass

    # Search box
    pyautogui.moveTo(324, 187, duration=1)
    pyautogui.click()

    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")

    # Contact search
    pyperclip.copy(contact)
    pyautogui.hotkey("ctrl", "v")

    time.sleep(2)

    pyautogui.press("down")
    time.sleep(0.5)
    pyautogui.press("enter")

    # Chat open hone do
    time.sleep(2)

    print("Chat open ho gayi.")

    # Video Call button
    pyautogui.moveTo(1203,114,duration=0.5)
    pyautogui.click()

    print("Video call start kar di.")

    return True
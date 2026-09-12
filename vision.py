import pyautogui
import pygetwindow as gw


def capture_screen():

    try:
        window = gw.getActiveWindow()

        if window is not None:

            left = window.left
            top = window.top
            width = window.width
            height = window.height

            image = pyautogui.screenshot(
                region=(left, top, width, height)
            )

        else:
            image = pyautogui.screenshot()

    except Exception:
        image = pyautogui.screenshot()

    image.save("vision.png")

    return "vision.png"
import ai
import screen
import pyautogui
import pytesseract
import cv2
import time
import pydirectinput
import ctypes

text = True
walk = False
sleepS = 2

def get_capslock_state():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)


def slowClick(coord):
    # move to x y
    pyautogui.moveTo(coord)
    # wait 0.2 seconds
    time.sleep(0.1)
    # click
    pyautogui.click()
    # wait 0.2 seconds
    time.sleep(0.1)

while True:
    # Bot disailitato se maiuscolo attivo
    if get_capslock_state:
        # Check if arrow prensent and configured to skip
        if text and pyautogui.locateOnScreen("arrow.png", confidence=0.8, grayscale=True):
            print("[" + time.strftime("%H:%M:%S") + "] Skipping")
            pydirectinput.press("z")
        # If the 1 image is present on screen
        # Use pyautogui and 1.png with 0.8 confidence to find the 1 image
        if walk and pyautogui.locateOnScreen("1.png", confidence=0.8, grayscale=True):
            print("[" + time.strftime("%H:%M:%S") + "] Walking")
            pydirectinput.keyDown('up')
            time.sleep(sleepS)
            pydirectinput.keyUp('up')
            pydirectinput.keyDown('down')
            time.sleep(sleepS)
            pydirectinput.keyUp('down')
        # check if there is the text "Battle" in the screen
        else:
            if "lotta" in screen.getBattle().lower():
                timeSince = time.time()
                # if there is, click the "Battle" button
                slowClick(screen.battleTXT[0:2])
                pyautogui.moveTo(287,73)
                pyautogui.sleep(0.5)
                ai.newAI()
                pyautogui.sleep(0.5)
                pyautogui.moveTo(287,73)
                timeSince = time.time()
    
            # Check if dead
            if "ps" in screen.getAHealth().lower():
                # Press all pokemon
                slowClick((412, 705))
                slowClick((412, 761))
                slowClick((612, 705))
                slowClick((612, 761))
                slowClick((823, 705))
                slowClick((823, 761))
                pyautogui.moveTo(287,73)

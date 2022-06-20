import ai
import screen
import pyautogui
import pytesseract
import cv2
import time

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
    # check if there is the text "Battle" in the screen
    if "lotta" in screen.getBattle().lower():
        # if there is, click the "Battle" button
        slowClick(screen.battleTXT[0:2])
        pyautogui.moveTo(287,73)
        pyautogui.sleep(0.5)
        ai.newAI()
        pyautogui.sleep(0.5)
        pyautogui.moveTo(287,73)

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

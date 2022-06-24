import numpy
import pyautogui
import pytesseract
import cv2
import threading
import time


# Coordinates
enemy = (287,152,398,169)
move1 = (305,712,406,723)
move2 = (517,712,618,723)
move3 = (305,766,406,779)
move4 = (517,766,618,779)
battleTXT = (370,691,426,711)
aHealth = (340,710,364,724)
pHealth = (1473,572,1554,593)

# internal use only
__move1__ = ""
__move2__ = ""
__move3__ = ""
__move4__ = ""

def takeScreenshot():
    image = pyautogui.screenshot()
    # Convert the image to only black and white
    fn = lambda x : 255 if x > 150 else 0
    image = image.convert('L').point(fn, mode='1')
    return image
    

def oldTakeScreenshot():
    # Take and return a PIL screenshot.
    return pyautogui.screenshot()

def getEnemy():
    # Take a screenshot, cop it based on the coordinates, and run pytesseract on it.
    # Return the result.
    return pytesseract.image_to_string(takeScreenshot().crop(enemy), lang='eng', config='--psm 8 --oem 3')

def getMove1():
    # Take a screenshot, cop it based on the coordinates, and run pytesseract on it.
    # Return the result.
    return pytesseract.image_to_string(takeScreenshot().crop(move1), lang='eng', config='--psm 8 --oem 3')

def getMove2():
    # Take a screenshot, cop it based on the coordinates, and run pytesseract on it.
    # Return the result.
    return pytesseract.image_to_string(takeScreenshot().crop(move2), lang='eng', config='--psm 8 --oem 3')

def getMove3():
    # Take a screenshot, cop it based on the coordinates, and run pytesseract on it.
    # Return the result.
    return pytesseract.image_to_string(takeScreenshot().crop(move3), lang='eng', config='--psm 8 --oem 3')

def getMove4():
    # Take a screenshot, cop it based on the coordinates, and run pytesseract on it.
    # Return the result.
    return pytesseract.image_to_string(takeScreenshot().crop(move4), lang='eng', config='--psm 8 --oem 3')

def getMoves():
    # Take all the move effectiveness and put them in a list
    moves = [getMove1(), getMove2(), getMove3(), getMove4()]
    return moves

def getMultiMove1():
    # Take a screenshot, cop it based on the coordinates, and run pytesseract on it.
    # Return the result.
    global __move1__
    __move1__ = pytesseract.image_to_string(takeScreenshot().crop(move1), lang='eng', config='--psm 8 --oem 3')

def getMultiMove2():
    # Take a screenshot, cop it based on the coordinates, and run pytesseract on it.
    # Return the result.
    global __move2__
    __move2__ = pytesseract.image_to_string(takeScreenshot().crop(move2), lang='eng', config='--psm 8 --oem 3')

def getMultiMove3():
    # Take a screenshot, cop it based on the coordinates, and run pytesseract on it.
    # Return the result.
    global __move3__
    __move3__ = pytesseract.image_to_string(takeScreenshot().crop(move3), lang='eng', config='--psm 8 --oem 3')

def getMultiMove4():
    # Take a screenshot, cop it based on the coordinates, and run pytesseract on it.
    # Return the result..
    global __move4__
    __move4__ = pytesseract.image_to_string(takeScreenshot().crop(move4), lang='eng', config='--psm 8 --oem 3')

def getMultithreadMoves():
    # Clear the thread list
    threads = []
    # Take all the move effectiveness and put them in a list
    # Use multithreading to get the moves in parallel before putting them in the list
    threads.append(threading.Thread(target=getMultiMove1))
    threads.append(threading.Thread(target=getMultiMove2))
    threads.append(threading.Thread(target=getMultiMove3))
    threads.append(threading.Thread(target=getMultiMove4))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    moves = [__move1__, __move2__, __move3__, __move4__]
    return moves

def getAHealth():
    # Take a screenshot, cop it based on the coordinates, and run pytesseract on it.
    # Return the result.
    #takeScreenshot().crop(aHealth).save("aHealth.png")
    return pytesseract.image_to_string(takeScreenshot().crop(aHealth), lang='eng', config='--psm 8 --oem 3')

def getPHealth():
    # Take a screenshot, cop it based on the coordinates, and run pytesseract on it.
    # Return the result.
    return pytesseract.image_to_string(takeScreenshot().crop(pHealth), lang='eng', config='--psm 8 --oem 3')

def getBattle():
    # Take a screenshot, cop it based on the coordinates, and run pytesseract on it.
    # Return the result.
    return pytesseract.image_to_string(takeScreenshot().crop(battleTXT), lang='eng', config='--psm 8 --oem 3')


if __name__ == "__main__":
    print(getAHealth())
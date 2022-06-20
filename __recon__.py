from asyncio import sleep
from unicodedata import name
from numpy import number
import subprocess
import time
import os
import sys
import io
import PIL.Image
import pytesseract
import threading

# Coordinates for important stuff


def takeScreen():
    cmd = "adb shell screencap -p"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    binary_screenshot = process.stdout.read()
    
    binary_screenshot = binary_screenshot.replace(b'\r\r\n', b'\n')
    return binary_screenshot

def click(x, y):
    subprocess.call("adb shell input tap " + str(x) + " " + str(y), shell=True)

while True:
    numbers = []
    numberString = ""
    screenshot = takeScreen()
    img = PIL.Image.open(io.BytesIO(screenshot))
    
    for j in range(SIZE):
        for i in range(SIZE):
            x = BASE_X + i * BUTTON_SIZE
            y = BASE_Y + j * BUTTON_SIZE
            box = (x, y, x + NUMBER_SIZE, y + NUMBER_SIZE)
            while True:
                try:
                    cropped_img = img.crop(box)
                    break
                except:
                    screenshot = takeScreen()
                    img = PIL.Image.open(io.BytesIO(screenshot))
                    continue
            #cropped_img.save('img/' + str(i) + '-' + str(j) + '.png')
            a = pytesseract.image_to_string(cropped_img, lang='eng', config='--psm 13 --oem 0 -c tessedit_char_whitelist=0123456789')
            if a == '':
                a = '0'
            numbers.append(a)
    # Remove all newlines from the list
    numbers = [x.strip() for x in numbers]
    print(numbers)
    # Constract a space separated string with a new line every SIZE numbers
    for i in range(len(numbers)):
        numberString += numbers[i] + " "
        if (i + 1) % SIZE == 0:
            numberString += '\n'
    finalString = str(SIZE) + "\n" + numberString
    print(finalString)
    steps = automator.shitRunner(finalString)
    
    # Take the index of the number that was swapped by a zero in the next step
    # and use it to find the index of the zero in the current step
    for i in range(len(steps)):
        #Find the zero in the next step
        try:
            zero_index = steps[i + 1].index(0)
            # Convert the index in x and y coordinates inside a square big SIZE
            x = zero_index % SIZE
            y = zero_index // SIZE
            # Convert the coordinates to a location based on the base coordinates
            x = BASE_X + x * BUTTON_SIZE
            y = BASE_Y + y * BUTTON_SIZE
            # Use adb commands to press the location
            threading.Thread(target=click, args=(x, y), name="clicker" + str(x) + str(y)).start()
            time.sleep(0.08)
            #subprocess.call(["adb", "shell", "input", "tap", str(x), str(y)])
        except:
            print("Finished!")
    #time.sleep(0.5)
    for thread in threading.enumerate(): 
        if thread.name.__contains__("clicker"):
            thread.join()

    # Check if the screenshot contains "Grande!"
    while True:
        try:
            screenshot = takeScreen()
            img = PIL.Image.open(io.BytesIO(screenshot))
            checker = img.crop((244, 1920, 400, 1977))
            break
        except:
            continue
    

    
    #checker.save("checker.png")
    stringer = pytesseract.image_to_string(checker, lang='eng', config='--psm 13 --oem 0')
    if stringer.__contains__("Grande"):
        subprocess.call("adb shell input tap 490 1960", shell=True)
    
#    subprocess.call("adb shell input tap 490 1960", shell=True)

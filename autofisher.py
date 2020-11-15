# This is my auto fisher app for ff14
# Screen size is x: 3840 (1920x2) y: 1080 - This is a dual monitor setup, both 1080p
# Location for 1 question mark x: 955 y: 437 , The colour of the question mark is 255 255 250
# 4 seconds for 1 exclamation mark, 8 seconds for 2 marks, 10 for 3 marks
# Imports
import sys
import pyautogui
import time
import tkinter as tk

# Global variables
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
# Class declarations

# Function declarations

def sight_loop():
    print("Fishing...")
    posX, posY = pyautogui.position()
    posXString = str(posX)
    posYString = str(posY)
    print("Mouse Position x: "+ posXString + " y: "+ posYString)
    try:
        rgbValues = pyautogui.screenshot().getpixel((954,415))
        print("the three rgb colours are "+ str(rgbValues[0]) +" "+str(rgbValues[1])+" "+str(rgbValues[2]))
        if (pyautogui.pixelMatchesColor(955, 437, (255, 255, 250)) == True):
            print("Statement1")
        elif (rgbValues[0] >= 200 or rgbValues[1] >= 200 or rgbValues[2] >= 200):
            print("we got a fish!")
            time.sleep(0.5)
            pyautogui.typewrite('3')
            time.sleep(8)
            pyautogui.typewrite('6') # mooch
            time.sleep(0.5)
            #pyautogui.typewrite('0') # release
            time.sleep(0.5)
            pyautogui.typewrite('2') # cast
            pass
        else:
            print("Fish not biting..")

    except:
        print("Mouse not on correct screen..")



def main():
    window = tk.Tk()
    title = tk.Label(text="Hello")
    title.pack()
    window.mainloop()
    counter=0
    try:
        while True:
            sight_loop()
            time.sleep(.5)
            counter+=1
            if counter>20:
                counter=0
                pyautogui.typewrite('2')
    except KeyboardInterrupt:
        print("Exiting...")

main()

import random
import time
import keyboard
import pyautogui
import win32api
import win32con


while True:
    if pyautogui.locateOnScreen("sticky.png", confidence=0.8) != None:
        print("Stickman!!")
        time.sleep(0.5)
    else:
        print("No stickman.")
        time.sleep(0.5)

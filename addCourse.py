import sys
import pyautogui
import time
import random
import threading
import os
import time
import pyperclip
imgpath='/Users/bariscicek/Desktop/Projeler/git/odtu-add-course-bot/'

############
def click(point,clicks,interval,button,confidence):
    v = locate(point,True,confidence)
    pyautogui.click(x=v[0],y=v[1],clicks=clicks,interval=interval,button=button)
    if point=='bustericon':
        clickelse()

def clickelse():
    pyautogui.moveTo(500, 500)

def locate(img,graycond,confidence):
    val = pyautogui.locateOnScreen(imgpath+image+'.png',grayscale=graycond,confidence=confidence)
    return val

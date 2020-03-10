import sys
import pyautogui
import time
import random
import threading
import os
import time
import pyperclip
import subprocess
import requests
imgpath='/Users/bariscicek/Desktop/Projeler/git/odtu-add-course-bot/'

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

def addcourse(userid,password,courseid,section,numTrials):
    FNULL = open(os.devnull, 'w')
    time.sleep(1)
    os.system('open -a "Google Chrome" https://register.metu.edu.tr')
    while True:
        if locate('login',True,.7): # login found
           break
    time.sleep(1)
    click('userlog',1,0.1,'left',0.6)
    pyautogui.typewrite(userid, interval=0.1)
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyperclip.copy(passwd)
    pyautogui.hotkey('command', 'v')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    while True:
        if locate('rc',True,.7): # recaptcha found
            recaptcha = 1
            click('courseinp',1,0.1,'left',0.6);
            pyautogui.typewrite(courseid, interval=0.1)
            pyautogui.keyDown('tab')
            pyautogui.keyUp('tab')
            pyautogui.typewrite(section, interval=0.1)

            break
    for cnn in range(numTrials):
        while True:
            if locate('rc',True,.7):
                break
        time.sleep(1)
        click('courseinp',1,0.1,'left',0.6);
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab') # must
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')
        pyautogui.keyDown('down')
        pyautogui.keyUp('down') # free elective
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        time.sleep(1)
        click('emptyre',1,0.1,'left',0.6);


        while True:
            if recaptcha == 0:
                    result = 0
                    break
            elif locate('success',True,.99): # tick located
                click('addcorse',2,0.1,'left',0.99);
                result = 2
                break
            elif locate('bustericon',True,.6): # buster found
                try:
                    click('bustericon',1,0.1,'left',0.6);
                except:
                    pass
if __name__=='__main__':
    metuUserID=''
    Password=''
    CourseID=''
    SectionNumber=''
    numberofTrials=100
    addcourse(metuUserID;Password,CourseID,SectionNumber,numberofTrials)

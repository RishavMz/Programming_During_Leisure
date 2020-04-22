#Author RishavMz
#This code uses pyautogui which allows python script to control the mouse and keyboard
#Run this code and wait. 
#Sorry for the wait. This code has deliberately been made to run slow by me so as to prevent glitches in slow systems.
#works fine in 1920 x 1080 pixel sized laptop screen
import time
import pyautogui
time.sleep(2)
pyautogui.moveTo(26,1053,duration=1)
pyautogui.click(26,1053)
time.sleep(0.5)
pyautogui.typewrite("Notepad \n")
time.sleep(0.5)
pyautogui.moveTo(167,375,duration=1)
pyautogui.click(167,375)
time.sleep(2)
pyautogui.moveTo(300,300,duration=1)
pyautogui.click(300,300)
pyautogui.keyDown('alt')
pyautogui.keyDown('space')
pyautogui.keyUp('alt')
pyautogui.keyUp('space')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite("Hello. This is  how you can use python script to control the mouse and keyboard  for automation in typing and mouse movements.\n ",interval = 0.15)
pyautogui.typewrite("Test : interval 0.25 sec\n",interval = 0.25)
pyautogui.typewrite("Test: interval 0.5 sec\n",interval = 0.50)
pyautogui.moveTo(1078,1053,duration=1)
'''
for i in range(1000):
    print(pyautogui.position())'''
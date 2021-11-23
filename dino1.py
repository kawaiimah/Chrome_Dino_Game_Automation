# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:38:56 2021

"""

# Go to chrome://dino
# Run this program
# Press q to quit

import pyautogui
import keyboard

# Jump/crouch logic given x coordinate
def decide(x,s):
    out = ''

    # sky: 200
    # head-height : 448
    # leg-height: 488  
    sky = pyautogui.pixelMatchesColor(x, 200, (255, 255, 255), tolerance=10)
    
    headcount = 0
    legcount = 0
    for i in range(x,x+s):
        if sky == pyautogui.pixelMatchesColor(x, 448, (255, 255, 255), tolerance=10):
            headcount += 1
        if sky == pyautogui.pixelMatchesColor(x, 488, (255, 255, 255), tolerance=10):
            legcount += 1        
    if headcount > (s-1):
        head = sky
    else:
        head = not sky
    if legcount > (s-1):
        leg = sky
    else:
        leg = not sky
    
    if leg != sky:
        out = 'jump'
    elif head != sky:
        out = 'crouch'
    
    return out


# Locate start screen
# Start game
x, y = pyautogui.locateCenterOnScreen('start.png', confidence=0.9)
pyautogui.click(x, y)
pyautogui.press('space')


# Infinite loop
downflag = False
count = 0
while True:

    x = 1135 + int(count/5)
    if x > 1900: x = 1900
    s = 10
    
    temp = decide(x,s)
    if temp == '':
        next
    elif temp == 'jump':
        if downflag == True:
            pyautogui.keyUp('down') 
            downflag = False
        pyautogui.press('up')
        count += 1
    elif temp == 'crouch':
        pyautogui.keyDown('down')
        downflag = True
        count += 1
    
    if keyboard.is_pressed('q'):
        break

print(count)
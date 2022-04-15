# This is made by CallMeRinChan

# Call this huge aids, but this is my first attempt and im shit at coding
# Have fun judging my code for being shit, ily <3

# This is for Leaf Blower Revolution... the idle game, yes... I want this code to dig for me

# All the stuff you need to install:
# pip install pyautogui
# pip install pillow
# pip install keyboard
# pip install opencv-pythons
# pip install numpy

# importing modules
import pyautogui # for writing stuff to the mouse etc. this does a lot of stuff
import keyboard # for detecting keyboard inputs || also writes stufF?
import time # for time based stuff
import cv2 # for aids color checking
import numpy as np # for even more color checking aids
from PIL import ImageGrab

pyautogui.FAILSAFE = True #the biggest mistake ill make

# variable declaration
screenWidth, screenHeight = pyautogui.size() # gets the size of the screen
centerx = screenWidth/2 # gets the x-axis of the center of the screen
centery = screenHeight/2 # gets the y-axis of the center of the screen
digger = False

# functions i guess
def doDig(x,y): # for going to the center of the screen
    pyautogui.moveTo(x,y)
    pyautogui.mouseDown(button='left')
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

def checkPixel(x,y):
    X=1
    px = ImageGrab.grab().load() # should make a "screenshot" and use that
    while X < x-1: # for every pixel on the x-axis
        Y=1
        X += 1
        while Y < y-1: # for every pixel on the y-axis
            Y += 1
            if np.any(px[X,Y] == (0,0,255)): # if the color matches
                pyautogui.moveTo(X,Y) #move over to grab the leaf
                print("Blauw op X: ",X," en Y; ",Y)
                px = ImageGrab.grab().load() # update the screen after picking up a dug leaf



print("centerx is: ", centerx, " centery is: ", centery)

# print("The resolution is: ",screenWidth, screenHeight); # to print the resolution, nice for debugging i guess
# print("The center is: ", center) # just to show the center, nice for debugging i guess

while True:

    if keyboard.is_pressed('='):
        if digger == True:
            digger = False
        else:
            digger = True
        time.sleep(1)


    if digger == True:
        doDig(centerx,centery) # just move to the center and click
        checkPixel(screenWidth, screenHeight) # check for blue pixels and move the cursor there to collect

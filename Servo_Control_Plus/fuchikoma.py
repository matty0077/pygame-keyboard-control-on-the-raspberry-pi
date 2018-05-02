#/////////////////////////////////pygame stuffs
import pygame
from pygame.locals import *
import sys
import time
#import pyganim
pygame.init()

#//////////set up the window
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Vanity Control')

BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
WHITE = (255, 255, 255)
BGCOLOR = (100, 50, 50)

mainClock = pygame.time.Clock()

instructionSurf = BASICFONT.render('0-calibrate 1-open  2-fist  3-fuck you  4-A-ok  5-Tap  6-Slide  7-vibe  8-metal!', True, WHITE)
instructionRect = instructionSurf.get_rect()
instructionRect.bottomleft = (10, WINDOWHEIGHT - 180)
#//////////////////////////////////////everything else

import numpy as np
from Adafruit_PWM_Servo_Driver import PWM
import traceback as traceback
import time
import sys
#sys.path.append("/home/pi/Desktop/NAVI")
import speech_recognition as sr
from espeak import espeak
from datetime import datetime
t = datetime.now().strftime('%k %M')

# Initialise the PWM device using the default address
pwm = PWM(0x40)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

pwm.setPWMFreq(60)
pygame.init()

class FUCHI:
#///////////////////////////////////////////motion
    def move(servo, angle):#, delta=170):
      #delay = max(delta * 0.003, 0.03)        # calculate delay
      zero_pulse = (servoMin + servoMax) / 2  # half-way == 0 degrees
      pulse_width = zero_pulse - servoMin     # maximum pulse to either side 
      pulse = zero_pulse + (pulse_width * angle / 80)
      #print("angle=%s pulse=%s" % (angle, pulse))
      pwm.setPWM(servo, 0, int(pulse))
      #time.sleep(delay)  # sleep to give the servo time to do its thing
      
    def mini(servo):
        #pwm.setPWM(servo, 0, servoMin)
        FUCHI.move(servo,-77)

    def plus(servo):
        #pwm.setPWM(servo,0, servoMax)
        FUCHI.move(servo, 77)

    def relax(servo):
        FUCHI.move(servo, 0)
#////////////////////////digit test (open/shut)
    def f_cal():
        FUCHI.move(5,-5)
        FUCHI.move(6,15)#25 up#
        FUCHI.plus(0)#close
        time.sleep(.25)
        FUCHI.mini(0)#open
        time.sleep(.25)
        FUCHI.mini(2)#close
        time.sleep(.25)
        FUCHI.plus(2)#open
        time.sleep(.25)
        FUCHI.mini(1)#close
        time.sleep(.25)
        FUCHI.plus(1)#open
        time.sleep(.25)
        FUCHI.plus(4)#close
        time.sleep(.25)
        FUCHI.mini(4)#open
        time.sleep(.25)
        FUCHI.plus(3)#close
        time.sleep(.25)
        FUCHI.mini(3)#open
        time.sleep(.25)


#///////////////////open/shut 
    def fist():
        FUCHI.plus(0)#close
        time.sleep(.25)
        FUCHI.mini(2)#close
        time.sleep(.25)
        FUCHI.mini(1)#close
        time.sleep(.25)
        FUCHI.plus(4)#close
        time.sleep(.25)
        FUCHI.plus(3)#close

    def palm():
        FUCHI.move(5,-5)
        FUCHI.move(6,15)#25 up#
        FUCHI.mini(0)#open
        time.sleep(.25)
        FUCHI.plus(2)#open
        time.sleep(.25)
        FUCHI.plus(1)#open
        time.sleep(.25)
        FUCHI.mini(4)#open
        time.sleep(.25)
        FUCHI.mini(3)#open
        
#/////////////////fuk_u!
    def f_off():
        FUCHI.move(5,-5)
        FUCHI.move(6,15)
        
        FUCHI.plus(0)#close
        time.sleep(.25)
        FUCHI.mini(2)#close
        time.sleep(.25)
        FUCHI.mini(1)#close
        time.sleep(.25)
        FUCHI.mini(4)#open
        time.sleep(.25)
        FUCHI.plus(3)#close


#///////////////a-ok!
    def OK():
        FUCHI.move(5,-5)
        FUCHI.move(6,15)#25 up#
        time.sleep(.25)
        FUCHI.move(0,-33)#close
        FUCHI.plus(3)#close
        FUCHI.plus(2)#open
        time.sleep(.25)
        FUCHI.plus(1)#open
        time.sleep(.25)
        FUCHI.mini(4)#open


#//////////////////////////GUITAR    

    def Tap():
        FUCHI.move(5,-5)
        FUCHI.move(6,5)
        time.sleep(.2)
        FUCHI.mini(0)
        FUCHI.plus(2)#open
        time.sleep(.25)
        FUCHI.plus(1)#open
        time.sleep(.25)
        FUCHI.mini(4)#open
        lore=15
        while lore>0:
            FUCHI.move(3,45)
            time.sleep(.07)
            FUCHI.move(3,-5)
            time.sleep(.07)
            lore-=1
            print(lore)

    def Tap2():
        FUCHI.move(5,-5)
        FUCHI.move(6,5)
        time.sleep(.2)
        FUCHI.mini(0)
        time.sleep(.2)
        FUCHI.move(3,30)
        time.sleep(.2)
        FUCHI.plus(1)#open
        time.sleep(.2)
        FUCHI.mini(4)#open
        lore=5
        while lore>0:
            FUCHI.move(2,-77)
            time.sleep(.25)
            FUCHI.move(2,75)
            time.sleep(.24)
            lore-=1
            print(lore)
        

    def Slide():
        FUCHI.move(5,-5)
        FUCHI.move(6,15)#25 up#
        FUCHI.plus(2)#open
        time.sleep(.25)
        FUCHI.move(3,-5)
        FUCHI.plus(1)#open
        time.sleep(.25)
        FUCHI.move(4,55)
        time.sleep(1.75)
        FUCHI.mini(4)
        

    def Bend():
        FUCHI.move(5,-15)
        FUCHI.move(6,15)
        FUCHI.plus(2)#open
        time.sleep(.25)
        FUCHI.move(3,45)
        FUCHI.plus(1)#open
        lore=9
        while lore>0:
            FUCHI.move(4,20)
            time.sleep(.05)
            FUCHI.move(4,75)
            time.sleep(.05)
            lore-=1
            print(lore)

        
    def Metal():
        FUCHI.move(5,-5)
        FUCHI.move(6,25)#25 up#
        FUCHI.plus(0)#close
        time.sleep(.25)
        FUCHI.plus(2)#open
        time.sleep(.25)
        FUCHI.mini(1)#close
        time.sleep(.25)
        FUCHI.plus(4)#close
        time.sleep(.25)
        FUCHI.mini(3)#open

#//////////////////////////////pygame control
while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get(): # event handling loop

        # handle ending the program
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == K_1:
                FUCHI.palm()
            elif event.key == K_2:
                FUCHI.fist()
            elif event.key == K_3:
                FUCHI.f_off()
            elif event.key == K_4:
                FUCHI.OK()
            elif event.key == K_5:
                FUCHI.Tap()
            elif event.key == K_6:
                FUCHI.Slide()
            elif event.key == K_7:
                FUCHI.Bend()
            elif event.key == K_8:
                FUCHI.Metal()
            elif event.key == K_0:
                FUCHI.f_cal()
            elif event.key == K_s:
                FUCHI.Tap2()

            
    windowSurface.blit(instructionSurf, instructionRect)

    pygame.display.update()
    mainClock.tick(30) # Feel free to experiment with any FPS setting.

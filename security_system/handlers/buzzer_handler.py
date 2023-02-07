from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)


import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


def beep(repeat=3):
   for i in range(0, repeat):
      for pulse in range(60):
         GPIO.output(17, True)
         sleep(0.001)
         GPIO.output(17, False)
         sleep(0.001)
      sleep(0.02)

from signal import pause

from gpiozero import Buzzer

BUZEER_PORT = 3

bz = Buzzer(BUZEER_PORT)


def beep():
    bz.beep(1, 1, 10)
    pause()

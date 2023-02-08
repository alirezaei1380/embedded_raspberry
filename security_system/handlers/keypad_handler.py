from datetime import datetime

import RPi.GPIO as GPIO
import time

from security_system.handlers.buzzer_handler import beep
from security_system.handlers.led_handler import turn_led_off, turn_led_on, turn_lock_led_off, turn_lock_led_on
from security_system.models import Raspberry

L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21

keypadPressed = -1

code_check_time = 0
admin_code = ''
user_code = ''
input = ""

key_press_time = 0
password_time = 0

user_login = False
admin_login = False

security_mode = True
turn_led_on()
turn_lock_led_off()
lock_mode = False
password_retry = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def keypadCallback(channel):
    global keypadPressed
    if keypadPressed == -1:
        keypadPressed = channel


GPIO.add_event_detect(C1, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C2, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C3, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C4, GPIO.RISING, callback=keypadCallback)


def setAllLines(state):
    GPIO.output(L1, state)
    GPIO.output(L2, state)
    GPIO.output(L3, state)
    GPIO.output(L4, state)


def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    char = ''
    if GPIO.input(C1) == 1:
        char = characters[0]
    if GPIO.input(C2) == 1:
        char = characters[1]
    if GPIO.input(C3) == 1:
        char = characters[2]
    if GPIO.input(C4) == 1:
        char = characters[3]
    GPIO.output(line, GPIO.LOW)
    return char


def set_passwords():
    global admin_code, user_code, code_check_time
    if not code_check_time:
        code_check_time = datetime.now().timestamp()
    now_time = datetime.now().timestamp()
    if now_time - code_check_time > 60:
        code_check_time = now_time
        raspberry = Raspberry.objects.last()
        admin_code = raspberry.admin_code
        user_code = raspberry.user_code


def get_char():
    char1 = readLine(L1, ["1", "2", "3", "A"])
    char2 = readLine(L2, ["4", "5", "6", "B"])
    char3 = readLine(L3, ["7", "8", "9", "C"])
    char4 = readLine(L4, ["*", "0", "#", "D"])
    if char1:
        return char1
    if char2:
        return char2
    if char3:
        return char3
    if char4:
        return char4
    return ''


def check_input():
    global input, user_login, user_code, admin_login, admin_code, password_time, password_retry, lock_mode
    if input == admin_code:
        password_time = datetime.now().timestamp()
        password_retry = 0
        admin_login = True
        lock_mode = False
        turn_lock_led_off()
    elif input == user_code:
        password_time = datetime.now().timestamp()
        password_retry = 0
        user_login = True
    else:
        password_retry += 1
        if password_retry == 3:
            password_retry = 0
            lock_mode = True
            turn_lock_led_on()
            beep(3)


def turn_on():
    global user_login, admin_login, security_mode, password_time, lock_mode, input
    now_time = datetime.now().timestamp()
    if ((lock_mode and admin_login) or (not lock_mode and admin_login) or (not lock_mode and user_login)) and now_time - password_time < 10:
        security_mode = True
        turn_led_on()
        beep(1)
    else:
        input = ''
        beep(2)


def turn_off():
    global user_login, admin_login, security_mode, password_time, input, lock_mode
    now_time = datetime.now().timestamp()
    if ((lock_mode and admin_login) or (not lock_mode and admin_login) or (not lock_mode and user_login)) and now_time - password_time < 10:
        security_mode = False
        turn_led_off()
        beep(1)
    else:
        beep(2)
        input = ''


def process_char(char):
    global input, key_press_time
    if not key_press_time:
        key_press_time = datetime.now().timestamp()
    now_time = datetime.now().timestamp()
    if now_time - key_press_time > 60:
        key_press_time = now_time
        input = ''
        return
    key_press_time = now_time
    if char == 'C':
        input = ''
    elif char == 'D':
        check_input()
        input = ''
    elif char == 'A':
        turn_on()
    elif char == 'B':
        turn_off()
    elif char not in ['*', '#']:
        input += char


def get_security_mode():
    global security_mode
    return security_mode


def run_keypad():
    global keypadPressed
    while True:
        if keypadPressed != -1:
            setAllLines(GPIO.HIGH)
            if GPIO.input(keypadPressed) == 0:
                keypadPressed = -1
            else:
                time.sleep(0.1)
        else:
            set_passwords()
            char = get_char()
            if char:
                process_char(char)
            time.sleep(0.1)

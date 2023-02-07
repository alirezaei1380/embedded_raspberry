from gpiozero import MotionSensor
from datetime import datetime

from security_system.handlers.buzzer_handler import beep
from security_system.handlers.camera_handler import take_image
from security_system.handlers.keypad_handler import get_security_mode
from security_system.handlers.security_handler import send_image
from security_system.models import ThiefRecord

MOTION_PORT = 4

pir = MotionSensor(MOTION_PORT)


def run_motion():
    while True:
        pir.wait_for_motion()
        if not get_security_mode():
            continue
        beep()
        image = take_image()
        beep()
        record = ThiefRecord.objects.create(image=image)
        send_image(record)
        pir.wait_for_no_motion()

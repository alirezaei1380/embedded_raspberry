from gpiozero import MotionSensor

from security_system.handlers.buzzer_handler import beep
from security_system.handlers.camera_handler import take_image
from security_system.handlers.keypad_handler import get_security_mode
from security_system.handlers.security_handler import send_image
from security_system.models import ThiefRecord

MOTION_SENSOR_PORT = 4

pir = MotionSensor(MOTION_SENSOR_PORT)
pir.wait_for_on_motion()


def motion_activate():
    if not get_security_mode():
        return
    beep()
    image = take_image()
    beep()
    record = ThiefRecord.objects.create(image=image)
    send_image(record)


pir.when_motion = motion_activate

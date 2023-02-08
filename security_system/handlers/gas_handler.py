import RPi.GPIO as GPIO
import time

from security_system.handlers.security_handler import send_gas
from security_system.models import SmokeRecord

GPIO.setmode(GPIO.BCM)
GAS_PORT = 14
GPIO.setup(GAS_PORT, GPIO.IN)


def run_gas():
    while True:
        gas_sensor_state = GPIO.input(GAS_PORT)
        print(gas_sensor_state)
        if gas_sensor_state != 0:
            print('gas')
            SmokeRecord.objects.create()
            send_gas()
        time.sleep(0.5)

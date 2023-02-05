from time import sleep

from mq2 import MQ2

from security_system.handlers.security_handler import send_gas
from security_system.models import SmokeRecord

GAS_PORT = 5

sensor = MQ2(pinData=GAS_PORT, baseVoltage=3.3)
sensor.calibrate()

SMOKE_LIMIT = 10
LPG_LIMIT = 10
METHAN_LIMIT = 10
HYDROGEN_LIMIT = 10


def run_gas():
    while True:
        smoke = sensor.readSmoke()
        lpg = sensor.readLPG()
        methan = sensor.readMethan()
        hydrogen = sensor.readHydrogen()
        if methan > METHAN_LIMIT or lpg > LPG_LIMIT or smoke > SMOKE_LIMIT or hydrogen > HYDROGEN_LIMIT:
            smoke_record = SmokeRecord.objects.create(methan=methan, lpg=lpg, smoke=smoke, hydrogen=hydrogen)
            send_gas(smoke_record)
        sleep(60)

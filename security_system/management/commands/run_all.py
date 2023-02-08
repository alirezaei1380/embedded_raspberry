from django.core.management import BaseCommand

from security_system.handlers.gas_handler import run_gas
from security_system.handlers.keypad_handler import run_keypad
from security_system.handlers.motion_handler import run_motion
import threading


class Thread(threading.Thread):
    def __init__(self, fn):
        threading.Thread.__init__(self)
        self.fn = fn


    def run(self):
        self.fn()


class Command(BaseCommand):

    def handle(self, *args, **options):
        Thread(run_motion).start()
        Thread(run_keypad).start()
        Thread(run_gas).start()


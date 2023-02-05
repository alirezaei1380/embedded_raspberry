from django.core.management import BaseCommand

from security_system.handlers.keypad_handler import run_keypad


class Command(BaseCommand):

    def handle(self, *args, **options):
        run_keypad()

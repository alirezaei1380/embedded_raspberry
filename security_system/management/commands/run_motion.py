from django.core.management import BaseCommand

from security_system.handlers.motion_handler import run_motion


class Command(BaseCommand):

    def handle(self, *args, **options):
        run_motion()

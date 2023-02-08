from django.core.management import BaseCommand

from security_system.handlers.request_handler import run_server


class Command(BaseCommand):

    def handle(self, *args, **options):
        run_server()

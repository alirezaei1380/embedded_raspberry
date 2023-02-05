from django.core.management import BaseCommand

from security_system.handlers.gas_handler import run_gas


class Command(BaseCommand):

    def handle(self, *args, **options):
        run_gas()

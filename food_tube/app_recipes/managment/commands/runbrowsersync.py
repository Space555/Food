from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = 'Run BrowserSync for live reloading'

    def handle(self, *args, **options):
        subprocess.call([
            'browser-sync', 'start', '--proxy', 'localhost:8000', '--files', 'static/**/*.*',
            '--files', 'templates/**/*.*'
        ])

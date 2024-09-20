import sys
import webbrowser
import threading
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    help = "Runs the server and opens the browser"

    def handle(self, *args, **options):
        self.stdout.write("Starting server...")

        # Run migrations
        call_command("migrate")

        # Start the server in a separate thread
        server_thread = threading.Thread(target=self._run_server)
        server_thread.start()

        # Wait for the server to be ready
        self._wait_for_server()

        # Open the browser
        webbrowser.open("http://127.0.0.1:8000")

        self.stdout.write("Server is running. Press CTRL+C to stop.")

        try:
            # Keep the main thread alive
            server_thread.join()
        except KeyboardInterrupt:
            self.stdout.write("Stopping server...")
            sys.exit(0)

    def _run_server(self):
        call_command("runserver", "127.0.0.1:8000")

    def _wait_for_server(self):
        while True:
            try:
                connections["default"].cursor()
                break
            except OperationalError:
                time.sleep(0.1)

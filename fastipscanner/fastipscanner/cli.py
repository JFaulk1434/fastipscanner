import os
import sys
import webbrowser
from django.core.management import execute_from_command_line


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fastipscanner.settings")

    # Start the Django server
    port = 8099
    server_address = f"http://127.0.0.1:{port}/"

    # Prepare Django server startup
    sys.argv = ["", "runserver", f"0.0.0.0:{port}", "--noreload"]

    # Open web browser
    webbrowser.open(server_address)

    # Start Django server
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

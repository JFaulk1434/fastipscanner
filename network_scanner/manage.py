#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
from django.conf import settings


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "network_scanner.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Use the PORT from settings
    from django.core.management.commands.runserver import Command as runserver

    runserver.default_port = str(settings.PORT)

    if len(sys.argv) == 1:
        # If no arguments are provided, run the server
        sys.argv.extend(["runserver", f"0.0.0.0:{settings.PORT}"])

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

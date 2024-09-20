#!/usr/bin/env python
import os
import sys
import django
import traceback


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "network_scanner.settings")

    try:
        django.setup()
    except Exception as e:
        print(f"Error setting up Django: {e}")
        print(traceback.format_exc())
        input("Press Enter to exit...")
        sys.exit(1)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(f"Error executing command: {e}")
        print(traceback.format_exc())
        input("Press Enter to exit...")
        sys.exit(1)


if __name__ == "__main__":
    print("Starting application...")
    print(f"Current working directory: {os.getcwd()}")
    print(f"sys.executable: {sys.executable}")
    print(f"sys.argv: {sys.argv}")
    print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}")

    if getattr(sys, "frozen", False):
        print("Running as a PyInstaller bundle")
        application_path = sys._MEIPASS
    else:
        print("Running in normal Python environment")
        application_path = os.path.dirname(os.path.abspath(__file__))

    print(f"Application path: {application_path}")
    os.chdir(application_path)
    sys.path.insert(0, application_path)

    main()

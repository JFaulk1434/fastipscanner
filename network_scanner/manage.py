#!/usr/bin/env python
import os
import sys
import django
import traceback
import platform


def print_diagnostic_info():
    print("Diagnostic Information:")
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.machine()}")
    print(f"System: {platform.system()}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"sys.executable: {sys.executable}")
    print(f"sys.argv: {sys.argv}")
    print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}")

    if getattr(sys, "frozen", False):
        print("Running as a PyInstaller bundle")
        print(f"sys._MEIPASS: {sys._MEIPASS}")
    else:
        print("Running in normal Python environment")

    print(f"PATH: {os.environ.get('PATH')}")
    print("Contents of current directory:")
    for item in os.listdir("."):
        print(f"  {item}")


def main():
    """Run administrative tasks."""
    print_diagnostic_info()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "network_scanner.settings")

    try:
        django.setup()
    except Exception as e:
        print(f"Error setting up Django: {e}")
        print(traceback.format_exc())
        return

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        print(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
        print(traceback.format_exc())
        return

    try:
        if getattr(sys, "frozen", False):
            execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])
        else:
            execute_from_command_line(sys.argv)
    except Exception as e:
        print(f"Error executing command: {e}")
        print(traceback.format_exc())


if __name__ == "__main__":
    print("Starting application...")
    main()
    print("Application finished. Press Enter to exit...")
    input()

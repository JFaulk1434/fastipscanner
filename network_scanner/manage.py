#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
from django.core.management.commands.migrate import Command as MigrateCommand
from django.db.migrations.executor import MigrationExecutor
from django.db import connections, DEFAULT_DB_ALIAS


def run_migrations():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "network_scanner.settings")
    try:
        from django.conf import settings

        executor = MigrationExecutor(connections[DEFAULT_DB_ALIAS])
        if executor.migration_plan(executor.loader.graph.leaf_nodes()):
            print("Running migrations...")
            migrate = MigrateCommand()
            migrate.handle(database=DEFAULT_DB_ALIAS, verbosity=1, noinput=True)
        else:
            print("No migrations needed.")
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "network_scanner.settings")

    if getattr(sys, "frozen", False):
        # If running as a bundled exe, check if database exists
        from django.conf import settings

        db_path = settings.DATABASES["default"]["NAME"]
        if not os.path.exists(db_path):
            print("Database not found. Creating and running migrations...")
            run_migrations()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

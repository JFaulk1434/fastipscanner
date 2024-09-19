import os
import sys

print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)
print(f"Added to Python path: {project_root}")

try:
    from network_scanner.network_scanner.app_info import (
        APP_NAME,
        APP_VERSION,
        APP_EXECUTABLE_NAME,
    )

    print(
        f"Successfully imported APP_NAME: {APP_NAME}, APP_VERSION: {APP_VERSION}, APP_EXECUTABLE_NAME: {APP_EXECUTABLE_NAME}"
    )
except ImportError as e:
    print(f"Error: Could not import app_info. Details: {e}", file=sys.stderr)
    print("Contents of current directory:")
    for root, dirs, files in os.walk("."):
        for file in files:
            print(os.path.join(root, file))
    sys.exit(1)

print(
    f'/DMyAppName="{APP_NAME}" /DMyAppVersion="{APP_VERSION}" /DMyAppExeName="{APP_EXECUTABLE_NAME}.exe"'
)

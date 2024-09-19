import os
import sys

print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

project_root = os.path.abspath(os.path.dirname(__file__))
network_scanner_path = os.path.join(project_root, "network_scanner")
sys.path.insert(0, network_scanner_path)
print(f"Added to Python path: {network_scanner_path}")

try:
    from network_scanner.app_info import APP_NAME, APP_VERSION

    print(f"Successfully imported APP_NAME: {APP_NAME}, APP_VERSION: {APP_VERSION}")
except ImportError as e:
    print(f"Error: Could not import app_info. Details: {e}", file=sys.stderr)
    print("Contents of network_scanner directory:")
    for root, dirs, files in os.walk(network_scanner_path):
        for file in files:
            print(os.path.join(root, file))
    sys.exit(1)

print(
    f'/DMyAppName="{APP_NAME}" /DMyAppVersion="{APP_VERSION}" /DMyAppExeName="{APP_NAME}.exe"'
)

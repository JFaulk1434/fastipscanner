import os
import sys

# Add the project root to the Python path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

try:
    from network_scanner.network_scanner.app_info import APP_NAME, APP_VERSION
except ImportError:
    print(
        "Error: Could not import app_info. Make sure the path is correct.",
        file=sys.stderr,
    )
    sys.exit(1)

print(
    f'/DMyAppName="{APP_NAME}" /DMyAppVersion="{APP_VERSION}" /DMyAppExeName="{APP_NAME}.exe"'
)

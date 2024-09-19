import os
import sys

# Add the project root to the Python path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

try:
    from network_scanner.network_scanner.settings import APP_NAME, VERSION
except ImportError:
    print(
        "Error: Could not import settings. Make sure the path is correct.",
        file=sys.stderr,
    )
    sys.exit(1)

print(
    f'/DMyAppName="{APP_NAME}" /DMyAppVersion="{VERSION}" /DMyAppExeName="{APP_NAME}.exe"'
)

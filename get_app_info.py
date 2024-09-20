import os
import sys

project_root = os.path.abspath(os.path.dirname(__file__))
network_scanner_path = os.path.join(project_root, "network_scanner")
sys.path.insert(0, network_scanner_path)

try:
    from network_scanner.app_info import APP_NAME, APP_VERSION

    print(f"APP_NAME={APP_NAME}")
    print(f"APP_VERSION={APP_VERSION}")
except ImportError as e:
    print(f"Error: Could not import app_info. Details: {e}", file=sys.stderr)
    sys.exit(1)

import re
import subprocess
from pathlib import Path


def update_version(file_path, current_version, new_version):
    content = Path(file_path).read_text()
    updated_content = content.replace(f'"{current_version}"', f'"{new_version}"')
    Path(file_path).write_text(updated_content)


def main():
    app_info_path = Path("network_scanner/network_scanner/app_info.py")
    settings_path = Path("network_scanner/network_scanner/settings.py")

    current_version = re.search(
        r'APP_VERSION = "(.*)"', app_info_path.read_text()
    ).group(1)
    major, minor, patch = map(int, current_version.split("."))
    new_version = f"{major}.{minor}.{patch + 1}"

    update_version(app_info_path, current_version, new_version)
    update_version(settings_path, current_version, new_version)

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Bump version to {new_version}"])
    subprocess.run(["git", "tag", new_version])
    subprocess.run(["git", "push"])
    subprocess.run(["git", "push", "--tags"])

    print(f"Version bumped from {current_version} to {new_version}")


if __name__ == "__main__":
    main()

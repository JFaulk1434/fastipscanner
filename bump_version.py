import re
import subprocess
import argparse
from pathlib import Path


def update_version(file_path, current_version, new_version):
    content = Path(file_path).read_text()
    updated_content = content.replace(f'"{current_version}"', f'"{new_version}"')
    Path(file_path).write_text(updated_content)


def increment_version(version, part):
    major, minor, patch = map(int, version.split("."))
    if part == "major":
        return f"{major + 1}.0.0"
    elif part == "minor":
        return f"{major}.{minor + 1}.0"
    else:  # patch
        return f"{major}.{minor}.{patch + 1}"


def main():
    parser = argparse.ArgumentParser(description="Bump version number")
    parser.add_argument(
        "part",
        choices=["major", "minor", "patch"],
        help="Part of the version to increment",
    )
    args = parser.parse_args()

    app_info_path = Path("network_scanner/network_scanner/app_info.py")
    settings_path = Path("network_scanner/network_scanner/settings.py")

    current_version = re.search(
        r'APP_VERSION = "(.*)"', app_info_path.read_text()
    ).group(1)

    new_version = increment_version(current_version, args.part)

    update_version(app_info_path, current_version, new_version)
    update_version(settings_path, current_version, new_version)

    subprocess.run(["git", "add", "."])
    subprocess.run(
        ["git", "commit", "-m", f"Bump {args.part} version to {new_version}"]
    )
    subprocess.run(["git", "tag", new_version])
    subprocess.run(["git", "push"])
    subprocess.run(["git", "push", "--tags"])

    print(f"Version bumped from {current_version} to {new_version}")


if __name__ == "__main__":
    main()

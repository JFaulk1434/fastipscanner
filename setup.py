import os
from setuptools import setup, find_packages

# Get the absolute path to the directory containing this file (setup.py)
here = os.path.abspath(os.path.dirname(__file__))

# Print current directory and its contents
print("Current directory:", here)
print("Contents:", os.listdir(here))

# Construct the path to app_info.py
app_info_path = os.path.join(here, "fastipscanner", "app_info.py")

print("Attempting to read:", app_info_path)
print("Does file exist?", os.path.exists(app_info_path))

# Read app_info.py
about = {}
try:
    with open(app_info_path, "r", encoding="utf-8") as f:
        exec(f.read(), about)
except FileNotFoundError:
    print(f"FileNotFoundError: {app_info_path} does not exist")
    raise

# Read the contents of your README file
with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=about.get("APP_NAME", "fastipscanner"),
    version=about.get("VERSION", "0.1.0"),
    author=about.get("AUTHOR", ""),
    author_email=about.get("AUTHOR_EMAIL", ""),
    description=about.get("DESCRIPTION", ""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about.get("URL", ""),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django",
        "scapy",
        "netifaces",
        "psutil",
        "whitenoise",
        "manuf",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "fastipscanner=fastipscanner.cli:main",
        ],
    },
)

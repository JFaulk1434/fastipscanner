import os
from setuptools import setup, find_packages

VERSION = "1.2.6"
APP_NAME = "fast_ip_scanner"
APP_DISPLAY_NAME = "Fast IP Scanner"
DESCRIPTION = "A clean, user-friendly web interface for fast IP scanning, port scanning, and network analysis. Built with Django and Scapy, Fast IP Scanner provides powerful network tools with an intuitive UI."
SITE_HEADER = APP_DISPLAY_NAME
AUTHOR = "Justin Faulk"
AUTHOR_EMAIL = "deww1434@gmail.com"
URL = "https://github.com/JFaulk1434/fastipscanner"
PORT = 8099

# Get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
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

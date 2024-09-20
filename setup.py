import os
from setuptools import setup, find_packages

# Import directly from app_info.py
from fastipscanner.app_info import (
    VERSION,
    APP_NAME,
    DESCRIPTION,
    AUTHOR,
    AUTHOR_EMAIL,
    URL,
)

# Get the long description from the README file
with open("README.md", encoding="utf-8") as f:
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
    packages=["fastipscanner", "scanner"],  # Explicitly list your packages
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
            "fastip=fastipscanner.cli:main",
        ],
    },
)

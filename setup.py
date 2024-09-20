import os
import sys
from setuptools import setup, find_packages

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

# Import app_info
from fastipscanner import app_info

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=app_info.APP_NAME,
    version=app_info.VERSION,
    author=app_info.AUTHOR,
    author_email=app_info.AUTHOR_EMAIL,
    description=app_info.DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=app_info.URL,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django",
        "scapy",
        "netifaces",
        "psutil",
        "whitenoise",
        "manuf",
        # Add any other dependencies here
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

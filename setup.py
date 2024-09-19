import os
from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Get the version, name, and description
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(
    os.path.join(here, "network_scanner", "app_info.py"), "r", encoding="utf-8"
) as f:
    exec(f.read(), about)

setup(
    name="fast_ip_scanner",
    version=about["APP_VERSION"],
    description=about["APP_NAME"],
    long_description=about["APP_DESCRIPTION"],
    long_description_content_type="text/markdown",
    url="https://github.com/JFaulk1434/webui_network_tools",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django",
        "manuf",
        "netifaces",
        "psutil",
        "scapy",
        "whitenoise",
        # Add other dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "fastip=network_scanner.manage:main",
        ],
    },
)

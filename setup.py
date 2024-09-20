import os
from setuptools import setup, find_packages

# Read app info
app_info = {}
app_info_path = os.path.join(os.path.dirname(__file__), "fastipscanner", "app_info.py")
with open(app_info_path, "r", encoding="utf-8") as f:
    exec(f.read(), app_info)

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=app_info["APP_NAME"],
    version=app_info["VERSION"],
    author=app_info["AUTHOR"],
    author_email=app_info["AUTHOR_EMAIL"],
    description=app_info["DESCRIPTION"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=app_info["URL"],
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

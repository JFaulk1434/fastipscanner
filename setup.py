from setuptools import setup, find_packages
import os

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
    name="fastipscanner",
    version="1.0.1",
    author="JFaulk1434",
    author_email="deww1434@gmail.com",
    description="A fast IP scanner with a web interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JFaulk1434/fastipscanner",
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
            "fastipscanner=fastipscanner.manage:main",
        ],
    },
)

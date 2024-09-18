from setuptools import setup, find_packages

setup(
    name="nettools",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django",
        "scapy",
        "netifaces",
        "manuf",
    ],
    entry_points={
        "console_scripts": [
            "nettools=network_scanner.manage:main",
        ],
    },
)

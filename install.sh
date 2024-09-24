#!/bin/bash

# Create a virtual environment
python3 -m venv ~/.fastipscanner_venv

# Activate the virtual environment
source ~/.fastipscanner_venv/bin/activate

# Install the package
pip install -e .

# Create an alias for fastip
echo "alias fastip='~/.fastipscanner_venv/bin/fastip'" >> ~/.zshrc

# Reload the shell configuration
source ~/.zshrc

echo "Installation complete. Please restart your terminal or run 'source ~/.zshrc', then you can use the 'fastip' command."
# webui_network_tools

Clean WebUI with Scapy for Network Scanning, Port Scanning, Trace Route, Saved results in database.

## Installing Nettools

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. Open your terminal (Command Prompt or PowerShell on Windows, Terminal on Mac/Linux)

2. (Optional) It's recommended to create and activate a virtual environment:

   ```python
   python -m venv nettools_env
   source nettools_env/bin/activate  # On Windows, use: nettools_env\Scripts\activate
   ```

3. Install Nettools:

   ```python
   pip install nettools
   ```

   If installing from GitHub:

   ```python
   pip install git+https://github.com/yourusername/nettools.git
   ```

4. After installation, you can run Nettools by typing:

   ```python
   nettools
   ```

   This will start the server and open a web browser to the application.

5. To stop the server, press CTRL+C in the terminal where it's running.

### Troubleshooting

If you encounter any issues:

- Ensure Python and pip are correctly installed and added to your system PATH.
- If you're using a virtual environment, make sure it's activated before installing or running Nettools.
- Check that all dependencies were correctly installed by running `pip list`.

For further assistance, please open an issue on our GitHub repository.

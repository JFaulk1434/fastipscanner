# Fast IP Scanner

![Network Scanner Logo](network_scanner/static/images/logo_small.png)

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/JFaulk1434/webui_network_tools)](https://github.com/JFaulk1434/webui_network_tools/releases)
[![License](https://img.shields.io/github/license/JFaulk1434/webui_network_tools)](https://github.com/JFaulk1434/webui_network_tools/blob/main/LICENSE)

A clean, user-friendly web interface for fast IP scanning, port scanning, and network analysis. Built with Django and Scapy, Fast IP Scanner provides powerful network tools with an intuitive UI.

## 🚀 Features

- 🌐 Network Scanning
- 🔍 Port Scanning
- 🛤️ Traceroute
- ⚡ Speed Test
- 💾 Saved Results in Database
- 📊 Result Visualization

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Quick Install

```bash
pip install fast_ip_scanner
```

To run the application, simply open a terminal or command prompt and type:

```bash
fastip
```

This will start the Fast IP Scanner on the default port (8099).

For advanced usage or to specify different Django commands, you can use:

```bash
fastip [django_command]
```

For example:

- `fastip runserver 8080` to run on a different port
- `fastip migrate` to run database migrations

For the latest development version:

```bash
git clone https://github.com/JFaulk1434/webui_network_tools.git
cd nettools
pip install -e .
```

### Detailed Installation Steps

1. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv nettools_env
   source nettools_env/bin/activate  # On Windows, use: nettools_env\Scripts\activate
   ```

2. Install Network Scanner:

   ```bash
   pip install nettools
   ```

3. Launch the application:

   ```bash
   nettools
   ```

   This will start the server and open a web browser to the application.

4. To stop the server, press `CTRL+C` in the terminal.

## 📖 Usage

After launching Network Scanner, you can:

1. Perform network scans to discover devices on your network
2. Conduct port scans on specific IP addresses
3. Run traceroute operations to analyze network paths
4. Execute speed tests to measure your internet connection
5. View and analyze saved scan results

## 🐛 Troubleshooting

If you encounter any issues:

- Ensure Python and pip are correctly installed and added to your system PATH.
- If using a virtual environment, make sure it's activated before installing or running Network Scanner.
- Verify all dependencies are correctly installed by running `pip list`.

For further assistance, please [open an issue](https://github.com/yourusername/nettools/issues) on our GitHub repository.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

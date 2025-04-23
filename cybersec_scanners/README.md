This folder will contain some cybersecurity scanners and exploration scripts. 
These tools are designed for scanning devices, networks, and vulnerabilities to assist in security testing and learning.

🔐 Bluetooth Device Scanner and Vendor Finder
📄 Script: bluetooth_scanner.py

🧠 Description
This script scans for nearby Bluetooth devices and checks the vendor information based on the MAC address. 
It then logs the results in a file on the Desktop, categorizing the devices as either real or possibly fake based on the MAC address.

⚙️ How It Works

Uses BleakScanner (via the bleak library) to discover Bluetooth devices.
For each device, it fetches the vendor information by querying an external API (maclookup.app) using the MAC address.
Logs the results in a file on the Desktop, including the devices name, MAC address, and vendor (or a warning if the MAC adress appears fake).

🧪  For Example
# Example log entry:
# ✅ Device: Device_Name, MAC: 01:23:45:67:89:AB, Vendor: Vendor_Name
# ⛔ Device: Unknown, MAC: 12:34:56:78:90:CD, STATUS: ⚠️ Possible fake MAC address!
                                                                                                
🔧 Requirements
Python 3.x
bleak library: For Bluetooth scanning
requests library: For making API requests to maclookup

Install dependencies with:
pip install bleak requests
                                                                                                
▶️ Running the Script
python3 bluetooth_scanner.py
                                                                                                
💾 Log File
The script saves the scan results to a log file located on your Desktop: bluetooth_log.txt.

⚠️ Disclaimer
All scripts in this folder are part of my personal learning journey in cybersecurity and are created solely for educational and academic purposes.


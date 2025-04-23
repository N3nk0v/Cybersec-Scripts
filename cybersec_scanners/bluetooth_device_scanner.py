# Bluetooth Device Scanner and Vendor Finder
# This script scans for Bluetooth devices and checks the vendor based on the MAC address.

import asyncio
import requests
import os
from bleak import BleakScanner

# Automatically find the Desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "bluetooth_log.txt")

# Function to check the vendor by MAC address
def get_device_vendor(mac_address):
    try:
        url = f"https://api.maclookup.app/v2/macs/{mac_address}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            vendor = data.get("company")
            if vendor:
                return vendor  # Real MAC address
            else:
                return "⚠️ Possible fake MAC address!"
        else:
            return "⚠️ Unsuccessful check"
    except Exception as e:
        return f"⚠️ Error during search: {e}"

# Function to scan for Bluetooth devices
async def scan_bluetooth_devices():
    
    print("Starting Bluetooth scan...")
    
    # Scan for devices
    devices = await BleakScanner.discover()

    # Write results to a log file on the Desktop
    with open(desktop_path, "w", encoding="utf-8") as log_file:
        for device in devices:
            mac_address = device.address
            vendor = get_device_vendor(mac_address)  # Check vendor
            
            # If no vendor is found, MAC may be fake
            if "⚠️" in vendor:
                log_entry = f"⛔ Device: {device.name or 'Unknown'}, MAC: {mac_address}, STATUS: {vendor}\n"
            else:
                log_entry = f"✅ Device: {device.name or 'Unknown'}, MAC: {mac_address}, Vendor: {vendor}\n"

            print(log_entry.strip())  # Display in console
            log_file.write(log_entry)
    
    print(f"Scan completed. Results saved in '{desktop_path}'.")

# Run the async function
asyncio.run(scan_bluetooth_devices())

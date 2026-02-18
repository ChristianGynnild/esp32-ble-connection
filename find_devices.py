#!/usr/bin/env python3
import asyncio
from bleak import BleakScanner
from typing import Optional

from dataclasses import dataclass
import draccus

@dataclass
class Config:
    """find BLE devices"""
    name: str = None            # Name to search for

async def scan_for_devices(name):
    """Scans for nearby BLE devices and prints their details."""
    print("Scanning for BLE devices...")
    # Discover devices for a default timeout (e.g., 5 seconds)
    devices = await BleakScanner.discover()
    
    if name is None:
        for device in devices:
            print(f"Device found: {device.name} at {device.address} (RSSI: dBm)")
    else:
        for device in devices:
            if device.name is not None and name in device.name:
                print(f"Device found: {device.name} at {device.address} (RSSI: dBm)")

    

@draccus.wrap()
def main(cfg: Config):
    # Run the asynchronous function
    asyncio.run(scan_for_devices(cfg.name))


if __name__ == "__main__":
    main()
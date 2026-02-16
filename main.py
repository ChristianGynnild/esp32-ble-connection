#!/usr/bin/env python3
import asyncio
from bleak import BleakClient
from time import sleep
from constants import ADDRESS, CHARACTERISTIC_UUID

# Replace with your device's address
# Format differs by operating system (MAC address for Windows/Linux, UUID for macOS)
# Example addresses: "24:71:89:cc:09:05" (Linux) or "ABCDEFG1-XXXX-XXXX-XXXX-XXXXXXXXXX" (macOS)

async def main(address):
    # Use BleakClient as an asynchronous context manager
    async with BleakClient(address) as client:
        # Check if connected
        if client.is_connected:
            print(f"Connected to {address}")
            # You can now read/write characteristics, start notifications, etc.
            # Example: Reading the model number string characteristic (UUID "2A24")
            # MODEL_NBR_UUID = "2A24"
            # model_number = await client.read_gatt_char(MODEL_NBR_UUID)
            # print(f"Model Number: {model_number.decode()}")
            # for characteristic in client.characteristics:
            #     print(characteristic)
            #     print(characteristic.service_uuid)

            # uuid = client.characteristic[0].service_uuid
            # print(uuid)

            for i in range(10):
                sleep(1)

                try:
                    # Read the characteristic value (returns a bytes object)
                    value_bytes = await client.read_gatt_char(CHARACTERISTIC_UUID, use_cached=False)
                    
                    # Decode the bytes into a string
                    decoded_string = value_bytes.decode('utf-8')
                    
                    print(f"Value (Bytes): {value_bytes}")
                    print(f"Value (String): {decoded_string}")

                except Exception as e:
                    print(f"Error reading characteristic: {e}")

        
        else:
            print(f"Failed to connect to {address}")

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main(ADDRESS))

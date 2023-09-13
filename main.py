import asyncio
from bleak import BleakScanner, BleakClient

BLUETOOTH_DISCOVERY_TIMEOUT = 5.0 # seconds

async def main():

    print(f"Discovering Bluetooth devices... (timeout = {BLUETOOTH_DISCOVERY_TIMEOUT}s)")
    devices = await BleakScanner.discover(timeout=BLUETOOTH_DISCOVERY_TIMEOUT)
    for d in devices:
        if "Bluefruit" in d.name:
            print("Device found!")
            device = d
            break
    else:
        raise IOError("Bluefruit device not found.")
    
    async with BleakClient(device.address) as client:
        services = await client.get_services()
        print("Services:")
        for service in services:
            print(service)

        

if __name__ == "__main__":
    asyncio.run(main())

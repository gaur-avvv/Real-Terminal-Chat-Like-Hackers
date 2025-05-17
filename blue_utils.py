import bluetooth

def discover_and_connect_bluetooth():
    print("Searching for nearby Bluetooth devices...")
    devices = bluetooth.discover_devices(duration=8, lookup_names=True)
    if not devices:
        print("No devices found.")
        return None

    for i, (addr, name) in enumerate(devices):
        print(f"{i+1}. {name} - {addr}")

    choice = int(input("Select device number to connect: ")) - 1
    addr = devices[choice][0]
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((addr, port))
    return sock

import bluetooth

def discover_and_connect_bluetooth():
    print("Searching for nearby Bluetooth devices...")
    try:
        devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
    except bluetooth.btcommon.BluetoothError as e:
        print(f"Bluetooth error during device discovery: {e}")
        return None

    if not devices:
        print("No devices found.")
        return None

    print("Found devices:")
    for i, (addr, name) in enumerate(devices):
        print(f"  {i+1}. {name} ({addr})")

    while True:
        try:
            choice = input("Select device number to connect (or '0' to rescan): ")
            if choice == '0':
                return discover_and_connect_bluetooth() # Recursive call to rescan
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(devices):
                addr, name = devices[choice_idx]
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Searching for BluetoothChatService on {name} ({addr})...")
    try:
        services = bluetooth.find_service(address=addr, name="BluetoothChatService")
    except bluetooth.btcommon.BluetoothError as e:
        print(f"Bluetooth error during service discovery: {e}")
        return None

    if not services:
        print("BluetoothChatService not found on the selected device.")
        print("Ensure the server is running and advertising the service, and that devices are paired.")
        return None

    service_info = services[0]
    port = service_info["port"]
    host = service_info["host"] # This is addr

    print(f"Connecting to {name} ({host}) on port {port}...")
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        sock.connect((host, port))
        print("Successfully connected!")
        return sock
    except bluetooth.btcommon.BluetoothError as e:
        print(f"Bluetooth error during connection: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during connection: {e}")
        return None

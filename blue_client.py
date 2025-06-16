import bluetooth # Keep for bluetooth.btcommon.BluetoothError
from datetime import datetime
import threading
from blue_utils import discover_and_connect_bluetooth # Corrected import
import sys # For sys.exit()

sock = discover_and_connect_bluetooth()

if sock is None:
    print("Failed to connect to a Bluetooth device. Exiting.")
    sys.exit(1)

username = input("Enter your username: ")
print("Connected. Type /exit to quit or /clear to clear screen.")

def listen():
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                print("\nDisconnected from server.\n> ", end="")
                break
            print("\n" + data.decode() + "\n> ", end="")
    except bluetooth.btcommon.BluetoothError as e:
        print(f"\nBluetooth error during receive: {e}. Disconnected.\n> ", end="")
    except Exception as e:
        print(f"\nError during receive: {e}. Disconnected.\n> ", end="")
    finally:
        # Potentially signal main thread to exit or attempt reconnection
        print("Listener thread finished.")


listener_thread = threading.Thread(target=listen, daemon=True)
listener_thread.start()

try:
    while True:
        msg = input("> ")
        if msg == "/exit":
            break
        elif msg == "/whoami":
            print(f"You are {username}")
            continue
        elif msg == "/clear":
            # Basic clear, might not work on all terminals perfectly
            print("\033c", end="")
            continue

        timestamp = datetime.now().strftime('%H:%M')
        full_message = f"[{timestamp}] {username}: {msg}"
        try:
            sock.send(full_message.encode())
        except bluetooth.btcommon.BluetoothError as e:
            print(f"Bluetooth error during send: {e}. Message may not have been sent.")
            # Decide if we should break or try to continue
            # For now, let's assume the listener will catch disconnection
            pass
        except Exception as e:
            print(f"Error during send: {e}. Message may not have been sent.")
            pass

except KeyboardInterrupt:
    print("\nExiting due to KeyboardInterrupt...")
finally:
    print("Closing socket...")
    if sock:
        sock.close()
    # Ensure listener thread has finished if it hasn't due to error
    if listener_thread.is_alive():
        print("Waiting for listener thread to join...")
        # listener_thread.join(timeout=1) # sock.recv might be blocking
    print("Client shut down.")

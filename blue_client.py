import bluetooth
from datetime import datetime
import threading
from .utils import discover_and_connect_bluetooth

nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)
print("Found devices:")
for idx, device in enumerate(nearby_devices):
    print(f"{idx + 1}: {device[1]} - {device[0]}")

choice = int(input("Select device to connect: ")) - 1
addr = nearby_devices[choice][0]
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((addr, port))
username = input("Enter your username: ")

print("Connected. Type /exit to quit.")

def listen():
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print("\n" + data.decode() + "\n> ", end="")

threading.Thread(target=listen, daemon=True).start()

while True:
    msg = input("> ")
    if msg == "/exit":
        break
    timestamp = datetime.now().strftime('%H:%M')
    full_message = f"[{timestamp}] {username}: {msg}"
    sock.send(full_message.encode())

sock.close()

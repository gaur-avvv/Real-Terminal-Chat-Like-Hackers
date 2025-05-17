import bluetooth
from datetime import datetime
import threading

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)
port = server_sock.getsockname()[1]

bluetooth.advertise_service(server_sock, "BluetoothChatService",
                            service_classes=[bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE])
print("[Bluetooth] Waiting for connection on RFCOMM channel", port)

client_sock, client_info = server_sock.accept()
print("[Bluetooth] Accepted connection from", client_info)

username = input("Enter your username: ")

def listen():
    while True:
        data = client_sock.recv(1024)
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
    client_sock.send(full_message.encode())

client_sock.close()
server_sock.close()

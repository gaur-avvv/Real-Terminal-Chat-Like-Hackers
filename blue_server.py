import bluetooth
from datetime import datetime
import threading
import sys # For sys.exit()

def start_bluetooth_server():
    server_sock = None
    client_sock = None
    listener_thread = None

    try:
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.bind(("", bluetooth.PORT_ANY))
        server_sock.listen(1)
        port = server_sock.getsockname()[1]

        bluetooth.advertise_service(server_sock, "BluetoothChatService",
                                    service_id = bluetooth.SERIAL_PORT_CLASS, # Using common UUID
                                    service_classes=[bluetooth.SERIAL_PORT_CLASS], # String UUID
                                    profiles=[bluetooth.SERIAL_PORT_PROFILE]) # String UUID
        print(f"[Bluetooth] Waiting for connection on RFCOMM channel {port}")
        print("Ensure your device is discoverable and paired if necessary.")

        try:
            client_sock, client_info = server_sock.accept()
            print(f"[Bluetooth] Accepted connection from {client_info}")
        except bluetooth.btcommon.BluetoothError as e:
            print(f"Bluetooth error during accept: {e}. Server may need to be restarted.")
            return # Exit function if accept fails

        username = input("Enter your username: ")
        print("Connected. Type /exit to quit or /clear to clear screen.")

        def listen_fn(sock):
            try:
                while True:
                    data = sock.recv(1024)
                    if not data:
                        print("\nClient disconnected.\n> ", end="")
                        break
                    print("\n" + data.decode() + "\n> ", end="")
            except bluetooth.btcommon.BluetoothError as e:
                print(f"\nBluetooth error during receive: {e}. Client disconnected.\n> ", end="")
            except Exception as e:
                print(f"\nError during receive: {e}. Client disconnected.\n> ", end="")
            finally:
                print("Listener thread finished.")
                # Potentially signal main thread or close client_sock here if appropriate
                # For now, main loop will handle client_sock closure on exit/error

        listener_thread = threading.Thread(target=listen_fn, args=(client_sock,), daemon=True)
        listener_thread.start()

        while True:
            msg = input("> ")
            if msg == "/exit":
                break
            elif msg == "/whoami":
                print(f"You are {username}")
                continue
            elif msg == "/clear":
                print("\033c", end="") # Basic clear
                continue

            timestamp = datetime.now().strftime('%H:%M')
            full_message = f"[{timestamp}] {username}: {msg}"
            try:
                client_sock.send(full_message.encode())
            except bluetooth.btcommon.BluetoothError as e:
                print(f"Bluetooth error during send: {e}. Message may not have been sent.")
                # If send fails, client might be disconnected. Listener should pick this up.
                # Consider breaking here if send errors are critical
            except Exception as e:
                print(f"Error during send: {e}. Message may not have been sent.")


    except bluetooth.btcommon.BluetoothError as e:
        print(f"A critical Bluetooth error occurred: {e}")
        print("Please ensure Bluetooth is enabled and drivers are correctly installed.")
    except KeyboardInterrupt:
        print("\nServer shutting down due to KeyboardInterrupt...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Closing sockets...")
        if client_sock:
            client_sock.close()
        if server_sock:
            server_sock.close()
        # Ensure listener thread has finished
        if listener_thread and listener_thread.is_alive():
            print("Waiting for listener thread to join...")
            # listener_thread.join(timeout=1) # client_sock.recv might be blocking
        print("Server shut down.")

if __name__ == "__main__":
    start_bluetooth_server()

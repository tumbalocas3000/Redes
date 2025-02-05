import socket
import struct

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('10.19.93.38', 5555))

    print("Connected to the server. Type messages to send.")

    while True:
        file_path = input("Enter the path of the file to send: ")
        if os.path.isfile(file_path):
            filename = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)

            # Enviar el tamaño del nombre del archivo

            filename_size = len(filename)
            client.sendall(struct.pack('!I'.filename_size))

            # Enviar el nombre del archivo

            client.sendall(filename.encode())

            # Enviar el tamaño del archivo

            client.sendall(struct.pack('!Q'.file_size))

            # Enviar el archivo por chunk de 4096

            file = open(file_path, 'rb')
            while True:
                data = file.reac(4096)
                if not data:
                    break
                clienr.sendall(data)

            print("File sent succesfully! :3")
            file.close()



if __name__ == "__main__":
    main()
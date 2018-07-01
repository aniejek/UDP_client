import socket

if __name__ == "__main__":
    print("xD")
    # a = Server()
    UDP_PORT = 5005
    UDP_IP = "192.168.0.40"
    MESSAGE = "Hello World!"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # sock.sendto(bytes(MESSAGE, 'utf-8'), (UDP_IP, UDP_PORT))
    sock.bind(("192.168.0.241", UDP_PORT))
    data, addr = sock.recvfrom(1024)
    print(str(data))
    pass

# from server import Server
import socket

if __name__ == '__main__':
    print('xD')
    # a = Server()
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    # UDP_PORT = 5005
    # MESSAGE = "Hello World!"
    # UDP_IP = "127.0.0.1"
    # UDP_PORT = 5005
    # MESSAGE = "Hello, World!"
    # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        sock.sendto(bytes([100, 17]), (UDP_IP, 9876))
        pass
    pass

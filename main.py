from server import Server
import socket

if __name__ == '__main__':
    print('xD')
    a = Server()
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    MESSAGE = "Hello World!"
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    MESSAGE = "Hello, World!"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    sock.bind((UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024)

class Server:
    _DEFAULT_START_PORT = 5050
    _DEFAULT_IP = '127.0.0.1'

    class Receiver:
        def __init__(self, ip, port):
            self.ip = ip
            self.port = port

    class Sender:
        def __init__(self, ip, port):
            self.ip = ip
            self.port = port

    class Player:
        def __init__(self, ip, port, message):
            self.ip = ip
            self.port = port
            self.message = message
            self.sender = Server.Sender(ip, port)
            self.receiver = Server.Receiver(ip, port)

    def __init__(self, ip=_DEFAULT_IP, start_port=_DEFAULT_START_PORT, players_number=3):
        self.ip = ip
        self.players = []
        while len(self.players) != players_number:
            self.__find_player__()

        # self.start_port = start_port
        # self.senders = [self.Sender(ip, start_port)]
        # self.receivers = [self.Receiver(ip, start_port)]

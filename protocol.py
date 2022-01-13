PORT = 11111
MAXBYTES = 7


def send_data(sock, data):
    sock.send(str(str(len(data)).zfill(MAXBYTES) + data).encode())


def recive_data(sock):
    data_length = int(sock.recv(MAXBYTES).decode())
    return sock.recv(data_length).decode()

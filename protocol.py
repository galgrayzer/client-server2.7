from time import sleep

PORT = 11111
MAXBYTES = 7


def send_data(sock, data):
    if type(data) == str:
        sock.send(str(str(len(data)).zfill(MAXBYTES) + data).encode())
    else:
        sock.send(str(len(data)).zfill(MAXBYTES).encode())
        sleep(0.1)
        sock.send(data)


def recive_data(sock, client=False):
    try:
        if not client:
            data_length = int(sock.recv(MAXBYTES).decode())
            return sock.recv(data_length).decode()
        else:
            data_length = int(sock.recv(MAXBYTES).decode())
            return sock.recv(data_length)
    except:
        return "Error"

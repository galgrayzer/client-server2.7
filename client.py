import protocol
from socket import *
from os import system


def main():
    system('cls')
    client_sock = socket(AF_INET, SOCK_STREAM)
    client_sock.connect(('localhost', protocol.PORT))
    print("""
    You can use one of the following commands:
    DIR, DELETE, EXECUTE, COPY, TAKE_SCREENSHOT
    """)
    while True:
        protocol.send_data(client_sock, input('~ '))
        print(protocol.recive_data(client_sock))


if __name__ == '__main__':
    main()

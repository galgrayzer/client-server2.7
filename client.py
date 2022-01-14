import protocol
from socket import *
from os import system


def main():
    system('cls')
    client_sock = socket(AF_INET, SOCK_STREAM)
    client_sock.connect(('localhost', protocol.PORT))
    print("""
    You can use one of the following commands:
    DIR, DELETE, EXECUTE, COPY, TAKE_SCREENSHOT, SEND_PHOTO, EXIT
    """)
    while True:
        user_input = input('~ ')
        match user_input:
            case 'SEND_PHOTO':
                protocol.send_data(client_sock, user_input)
                data = protocol.recive_data(client_sock, True)
                try:
                    data = data.decode()
                    print(data)
                except:
                    with open('client_image.png', 'wb') as image:
                        image.write(data)
                        print('Image was arived!')
            case 'EXIT':
                protocol.send_data(client_sock, user_input)
                break
            case _:
                protocol.send_data(client_sock, user_input)
                print(protocol.recive_data(client_sock))
    client_sock.close()


if __name__ == '__main__':
    main()

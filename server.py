import protocol
from socket import *
from os import *
from subprocess import call
from shutil import copy
from pyautogui import *


def split_requset(request):
    """
    Spliting the request to the following parms:
    ~ The validation of the request - True / False
    ~ The command that given - DIR, DELETE, EXECUTE, COPY, TAKE_SCREENSHOT
    ~ The data given - path's / None
    """
    try:
        command, data = request.split(' ', 1)
        match command:
            case 'DIR' | 'DELETE' | 'EXECUTE':
                return True, command, [data]
            case 'COPY':
                return True, command, list(data.split(' ', 1))
            case _:
                raise
    except:
        if request == 'TAKE_SCREENSHOT':
            return True, request, None
        return False, None, None


def check_request(vaild, command, data):
    """
    Checking if the request is vaild.
    Returning - True / False
    """
    if vaild:
        match command:
            case 'DIR' | 'DELETE' | 'EXECUTE':
                if path.exists(data[0]):
                    return True
                return False
            case 'COPY':
                if path.exists(data[0]) and path.exists(data[1]):
                    return True
                return False
            case 'TAKE_SCREENSHOT':
                return True
    else:
        return False


def handle_request(command, data):
    """
    Handeling the client request by the command.
    """
    match command:
        case 'DIR':
            try:
                files = listdir(data[0])
                return '\n'.join(files)
            except:
                return "Can't acsses the folder"
        case 'DELETE':
            try:
                remove(data[0])
                return 'File deleted!'
            except:
                return "Can't delete the file"
        case 'EXECUTE':
            try:
                call(data[0])
                return 'The app is up and running!'
            except:
                return 'Faild lunching the app'
        case 'COPY':
            try:
                copy(data[0], data[1])
                return "The file was copied sucssfuly!"
            except:
                return 'Faild copying the file to the destination'
        case 'TAKE_SCREENSHOT':
            image = screenshot()
            image.save('server_screenshot.png')
            return 'Sucssfuly taken a screenshot'


def main():
    system('cls')
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.bind(('0.0.0.0', protocol.PORT))
    server_sock.listen(1)
    client_sock, client_adress = server_sock.accept()
    print(f'A new connection from - {client_adress}')
    while True:
        request = protocol.recive_data(client_sock)
        vaild, command, data = split_requset(request)
        if check_request(vaild, command, data):
            protocol.send_data(client_sock, handle_request(command, data))
        else:
            protocol.send_data(
                client_sock, "Can't prosses the request, please try again")


if __name__ == '__main__':
    main()

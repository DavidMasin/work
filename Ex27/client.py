#   Ex. 2.7 template - client side
#   Author: Barak Gonen, 2017
#   Modified for Python 3, 2020


import socket

import protocol

IP = "192.168.1.249"
# IP = "127.0.0.1"
SAVED_PHOTO_LOCATION = "C:\\Users\\user\\Downloads\\screen.jpg"  # The path + filename where the copy of the screenshot at the client should be saved


def handle_server_response(my_socket, cmd):
    """
    Receive the response from the server and handle it, according to the request
    For example, DIR should result in printing the contents to the screen,
    Note - special attention should be given to SEND_PHOTO as it requires and extra receive
    """
    if (cmd != "SEND_PHOTO"):
        response = my_socket.recv(1024).decode()
        print(response)

    # (8) treat all responses except SEND_PHOTO

    # (10) treat SEND_PHOTO
    else:  # for SEND_PHOTO
        # First, receive the size of the photo
        length = int(my_socket.recv(protocol.LENGTH_FIELD_SIZE).decode())
        bytes_received = 0
        with open(SAVED_PHOTO_LOCATION, 'wb') as f:
            while bytes_received < length:
                data = my_socket.recv(min(1024, length - bytes_received))
                if not data:
                    break
                f.write(data)
                bytes_received += len(data)
        print("Photo received and saved.")


def main():
    # open socket with the server
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, protocol.PORT))

    # (2)

    # print instructions
    print('Welcome to remote computer application. Available commands are:\n')
    print('TAKE_SCREENSHOT\nSEND_PHOTO\nDIR\nDELETE\nCOPY\nEXECUTE\nEXIT')

    # loop until user requested to exit
    while True:
        cmd = input("Please enter command:\n")
        if protocol.check_cmd(cmd):
            packet = protocol.create_msg(cmd)
            my_socket.send(packet)
            handle_server_response(my_socket, cmd)
            if cmd == 'EXIT':
                break
        else:
            print("Not a valid command, or missing parameters\n")

    my_socket.close()


if __name__ == '__main__':
    main()

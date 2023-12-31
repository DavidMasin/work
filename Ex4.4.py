# Ex 4.4 - HTTP Server Shell
# Author: Barak Gonen
# Purpose: Provide a basis for Ex. 4.4
# Note: The code is written in a simple way, without classes, log files or other utilities, for educational purpose
# Usage: Fill the missing functions and constants

# TO DO: import modules
import socket

# TO DO: set constants
IP = '0.0.0.0'
PORT = 80
SOCKET_TIMEOUT = 0.1



def get_file_data(filename):
    """ Get data from file """
    # access and open file of figure
    filename.file = open("wsi.png", "rb")
    # read file of figure
    filename.b_file = filename.file.read()
    return


def handle_client_request(resource, client_socket, ):
    """ Check the required resource, generate proper HTTP response and send to client"""
    # TO DO : add code that given a resource (URL and parameters) generates the proper response



    if resource == '':
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    else:
        url = resource
    REDIRECTION_DICTIONARY=''
    # TO DO: check if URL had been redirected, not available or other error code. For example:
    if url in REDIRECTION_DICTIONARY:
        client_socket.send("ERROR CODE: 302".encode())
    filetype = type(url)
    # TO DO: extract requested file tupe from URL (html, jpg etc)
    if filetype == 'html':
        http_header =  # TO DO: generate proper HTTP header
    elif filetype == 'jpg':
        http_header = # TO DO: generate proper jpg header
    # TO DO: handle all other headers

    # TO DO: read the data from the file
    data = get_file_data(resource)
    http_response = http_header + data
    client_socket.send(http_response.encode())


def validate_http_request(request):
    """
    Check if request is a valid HTTP request and returns TRUE / FALSE and the requested URL
    """
    # TO DO: write function
    request2 = request.split(' ')
    if request2[0] == 'GET'and request2[2] == 'HTTP/1.1':
        return True, request2[1]

    return False, request2[1]

def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')
    client_socket.send("You have been connected to a server".encode())

    while True:
        # TO DO: insert code that receives client request
        # ...
        valid_http, resource = validate_http_request(client_socket.recv(1024).decode())
        if valid_http:
            print('Got a valid HTTP request')
            handle_client_request(resource, client_socket)
            break
        else:
            print('Error: Not a valid HTTP request')
            break

    print('Closing connection')
    client_socket.close()


def main():
    # Open a socket and loop forever while waiting for clients
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("Listening for connections on port {}".format(PORT))

    while True:
        client_socket, client_address = server_socket.accept()
        print('New connection received')
        client_socket.settimeout(SOCKET_TIMEOUT)
        handle_client(client_socket)


if __name__ == "__main__":
    # Call the main handler function
    main()

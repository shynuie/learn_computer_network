import socket

SERVER_NAME = '192.168.0.180' # could be a URL/IP/Hostname
SERVER_PORT = 12000
BUF_MEMORY = 2048 # byte

# Build server socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", SERVER_PORT))  # binding the socket to specifying IP and port #

server_socket.listen(1)
print('Server is ready to receive')

while True:
    connection_socket, addr = server_socket.accept()  # codes will hold on this line till there's a connection built by client
    msg = connection_socket.recv(BUF_MEMORY).decode()
    if msg == "shutdown":
        break
    reply_msg = msg.upper()
    connection_socket.send(reply_msg.encode())

connection_socket.close()
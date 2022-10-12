import socket
import time

SERVER_NAME = '192.168.0.180' # could be a URL/IP/Hostname
SERVER_PORT = 12000
BUF_MEMORY = 2048 # byte


# Build client socket and connect to server window socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET for IPv4, SOCK_STREAM for TCP
client_socket.connect((SERVER_NAME, SERVER_PORT))

# input a msg and send to server
msg = input('Enter a lowercase sentence:\n')
client_socket.send(msg.encode())

time.sleep(0.1)

# receive reply msg and parse it to show
reply_msg = client_socket.recv(BUF_MEMORY)
print(f'From server:{reply_msg.decode()}')
client_socket.close()
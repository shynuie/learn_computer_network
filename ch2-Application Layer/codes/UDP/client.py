import socket
import time

SERVER_NAME = '192.168.0.180' # could be a URL/IP/Hostname
SERVER_PORT = 12000
BUF_MEMORY = 2048 # byte

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input('Enter a lowercase sentence:\n')
client_socket.sendto(msg.encode(), (SERVER_NAME, SERVER_PORT))
time.sleep(0.1)
reply_msg, (server_ip, server_port) = client_socket.recvfrom(BUF_MEMORY)
print(reply_msg.decode())
client_socket.close()
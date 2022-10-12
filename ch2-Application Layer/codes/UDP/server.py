import socket

SERVER_PORT = 120000
BUF_MEMORY = 2048

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', SERVER_PORT))  # specifying the IP address only if we want to receive datagram from particular network device
print("The server is ready to receive")

while True:
    msg, client_address = server_socket.recvfrom(BUF_MEMORY)  # the client_address is a tuple containing (ip, port)
    output_msg = msg.decode().upper()
    server_socket.sendto(output_msg.encode(), client_address)
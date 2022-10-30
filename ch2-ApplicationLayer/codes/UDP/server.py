import socket

SERVER_PORT = 12000
BUF_MEMORY = 2048

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', SERVER_PORT))  # specifying the IP address only if we want to receive datagram from particular network device
print("The server is ready to receive via UDP...")

while True:
    msg, client_address = server_socket.recvfrom(BUF_MEMORY)  # the client_address is a tuple containing (ip, port)
    if msg.decode() == "shutdown":
        output_msg = f'Shutdown the server'
        server_socket.sendto(output_msg.encode(), client_address)
        break
    output_msg = msg.decode().upper()
    server_socket.sendto(output_msg.encode(), client_address)
server_socket.close()
print("Close socket")
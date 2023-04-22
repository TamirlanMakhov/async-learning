import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = ('127.0.0.1', 8000)
server_socket.bind(address)

server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f'got connection request from {client_address}')

    buffer = b''

    while buffer[-2:] != b'\r\n':
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f'got data {data}')
            buffer += data
        print(f'all data: {buffer}')
        connection.sendall(buffer)
finally:
    server_socket.close()
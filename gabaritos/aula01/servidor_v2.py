import socket
from pathlib import Path
from utils import extract_route, read_file, build_response
from views import index

#https://realpython.com/python-sockets/
CUR_DIR = Path(__file__).parent
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print(local_ip)

    print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

    while True:
        client_connection, client_address = server_socket.accept()

        with client_connection:
            request = client_connection.recv(16384).decode()

            if request.startswith("POST") and len(request.split('\n\n'))==1:
                request+= client_connection.recv(16384).decode()
            print(request)

            route = extract_route(request)

            filepath = CUR_DIR / route
            if filepath.is_file():
                response = build_response() + read_file(filepath)
            elif route == '':
                response = index(request)
            else:
                response = build_response()

            client_connection.sendall(response)

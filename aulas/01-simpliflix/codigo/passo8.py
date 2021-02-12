import socket
from pathlib import Path
from utils import extract_route, read_file, load_data

CUR_DIR = Path(__file__).parent
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

SERIE_TEMPLATE = '''  <li>
    <a href="/{slug}">
      <img src="{image}">
      {title}
    </a>
  </li>
'''

RESPONSE_TEMPLATE = '''HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Simpliflix - Para quem gosta de assistir Netflix, não os filmes</title>
</head>
<body>

<h1>Simpliflix</h1>
<p>Para quem gosta de assistir Netflix, não os filmes</p>

<ul>
{series}
</ul>

</body>
</html>
'''

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    print(request)

    route = extract_route(request)
    filepath = CUR_DIR / route
    if filepath.is_file():
        response = 'HTTP/1.1 200 OK\n\n'.encode() + read_file(filepath)
    else:
        # Cria uma lista de <li>'s para cada série
        # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        series_li = [
            SERIE_TEMPLATE.format(title=dados['titulo'], slug=dados['slug'], image=dados['imagem'])
            for dados in load_data('series.json')
        ]
        series = '\n'.join(series_li)

        response = RESPONSE_TEMPLATE.format(series=series).encode()
    client_connection.sendall(response)

    client_connection.close()

server_socket.close()

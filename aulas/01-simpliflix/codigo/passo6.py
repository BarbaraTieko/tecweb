import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

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
  <li>
    <a href="/breakingbad">
      <img src="/img/breakingbad/breaking-bad.jpg">
      Breaking Bad
    </a>
  </li>
  <li>
    <a href="/friends">
      <img src="/img/friends/friends.jpg">
      Friends
    </a>
  </li>
  <li>
    <a href="/gameofthrones">
      <img src="/img/gameofthrones/game-of-thrones.jpg">
      Game of Thrones
    </a>
  </li>
  <li>
    <a href="/himym">
      <img src="/img/himym/himym.jpg">
      How I Met Your Mother
    </a>
  </li>
  <li>
    <a href="/houseofcards">
      <img src="/img/houseofcards/showcase.png">
      House of Cards
    </a>
  </li>
  <li>
    <a href="/narcos">
      <img src="/img/narcos/narcos.jpg">
      Narcos
    </a>
  </li>
  <li>
    <a href="/prisonbreak">
      <img src="/img/prisonbreak/prison-break.jpg">
      Prison Break
    </a>
  </li>
  <li>
    <a href="/strangerthings">
      <img src="/img/strangerthings/stranger-things.jpg">
      Stranger Things
    </a>
  </li>
  <li>
    <a href="/walkingdead">
      <img src="/img/walkingdead/walking-dead.jpg">
      Walking Dead
    </a>
  </li>
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

    client_connection.sendall(RESPONSE_TEMPLATE.encode())

    client_connection.close()

server_socket.close()

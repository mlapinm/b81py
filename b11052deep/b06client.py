

# создание сокета, клиент

import socket


sock = socket.create_connection(("127.0.0.1", 8888))
sock.sendall("ping".encode("utf8"))
sock.close()
print('client')




# создание сокета, клиент

import socket
import time
import re


class ClientError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        print(*args)
    pass

def strs_to_json(s):
    obj = {}
    ss = s.split('\n')
    ss = [e.split(' ') for e in ss if len(e.split(' ')) == 3]
    obj = {}
    for e in ss:
        l = obj.get(e[0], [])
        l.append((e[1], e[2]))
        obj[e[0]] = l
    return obj


class Client():

    def __init__(self, ip, port, timeout =1150864247):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        try:
            self.sock = socket.create_connection((self.ip, self.port))
        except Exception as exc:
            ClientError("aa")

    def put(self, cpu, load, timestamp=None):
        timestamp = timestamp and int(time.time())
        req = "put {} {} {}\n".format(cpu, load, timestamp)
        try:
          self.sock.sendall(req.encode("utf8"))
        except Exception as exc:
            ClientError("bb")

    def get(self, cpu):
        req = "get {}\n".format(cpu)
        try:
            self.sock.sendall(req.encode("utf8"))
            res = self.sock.recv(1024)
        except Exception as exc:
            ClientError("bb")
        json2 = strs_to_json(res.decode('utf8'))
        return json2

    def __del__(self):
        self.sock.close()
        pass


if __name__ == "__main__":
    client = Client("127.0.0.1", 8888, timeout=3)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    j = client.get("*")
    print(j)
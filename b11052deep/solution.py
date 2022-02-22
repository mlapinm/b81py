

# создание сокета, клиент

import socket
import time
import re


class ClientError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        print(*args)
    pass



class Client():

    def __init__(self, ip, port, timeout =1150864247):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        try:
            self.sock = socket.create_connection((self.ip, self.port))
        except Exception as exc:
            ClientError("aa")

    def strs_to_json(self, s):
        obj = {}
        if s == "ok\n\n":
            return obj
        ss = s.split('\n')
        ss = [e.split(' ') for e in ss if len(e.split(' ')) == 3]

        if len(ss) == 0:
            raise ClientError

        for e in ss:
            if self.cpu != '*':
                if e[0] != self.cpu:
                    raise ClientError

        obj = {}
        for e in ss:
            l = obj.get(e[0], [])
            l.append(( int(e[2]), float(e[1]) ))
            obj[e[0]] = l

        for e in obj:
            l = obj[e]
            l.sort(key = lambda a: a[0])
            obj[e] = l

        return obj


    def put(self, cpu, load, timestamp=None):
        if not timestamp:
            timestamp = int(time.time())
        req = "put {} {} {}\n".format(cpu, load, timestamp)
        try:
          self.sock.sendall(req.encode("utf8"))
        except Exception as exc:
            ClientError("bb")
        res = self.sock.recv(1024)
        if res.decode() != "ok\n\n":
            raise ClientError
            

    def get(self, cpu):
        self.cpu = cpu
        req = "get {}\n".format(cpu)
        try:
            self.sock.sendall(req.encode("utf8"))
            res = self.sock.recv(1024)
        except Exception as exc:
            ClientError("bb")
        resp_str = res.decode('utf8')
        match = re.search(r'^error', resp_str)
        if match:
            raise ClientError()
        json2 = self.strs_to_json(resp_str)
        return json2

    def __del__(self):
        self.sock.close()
        pass





if __name__ == "__main__":
    client = Client("127.0.0.1", 8888, timeout=3)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 0.5)
    j = client.get("*")
    print(j)


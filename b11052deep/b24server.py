import re
import asyncio


def process_data(data):
    strs = data.split('\n')
    strs = [e for e in strs if e]
    print(strs)
    str2 = ''
    if len(strs) > 0:
        str2 = strs[-1]
    return str2


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode())
        match = re.search(r'^get', resp)
        if match:
            resp2 = "ok\npalm.cpu 2.0 1150864247\npalm.cpu 0.5 1150864248\n\n"
            resp2 = 'error\nwrong command\n\n'
            self.transport.write(resp2.encode())

        match = re.search(r'^put', resp)
        if match:
            self.transport.write("ok\n\n".encode())

loop = asyncio.get_event_loop()
coro = loop.create_server(
    ClientServerProtocol,
    '127.0.0.1', 8888
)

print('start', '127.0.0.1', 8888)
server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()


print('server')


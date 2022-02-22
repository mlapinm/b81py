import sys
import re
import asyncio

cpus = {}

def process_data(data):
    print(data)
    
    cmd, line = data.split(' ', 1)

    print(cmd, 33, line)

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
        self.transport.write(resp.encode())

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
    print('Interrupted')
    sys.exit(0)
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()


print('server')


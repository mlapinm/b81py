import sys
import re
import asyncio


def run_server(host, port):

    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    print('start', host, port)
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

cpus = {
    # 'test_key1': [(123, 0.2), (124, 0.2), (125, 0.2)],
    # 'test_key2': [(123, 0.3), (124, 0.4), (125, 0.5)],
}

def process_data(data):
    res = ''
    cmd = ''
    other = '' 
    try:   
        cmd, other = data.split(' ', 1)
        cmd = cmd.strip()
        other = other.strip()
        # print(1, cmd, 2, other, 3)
        if cmd == 'get':
            if len(other.split()) != 1:
                raise ValueError
        if cmd == 'put':
            if len(other.split()) != 3:
                raise ValueError
    except Exception:
        print('ValueError')
        cmd = 'error'
    cmd = cmd.strip()
    other = other.strip()
    if cmd == "get":
        res = 'ok\n'
        if other == '*':
            for e in cpus:
                for t in cpus[e]:
                    s = '{} {} {}'.format(e, t[1], t[0])
                    s += '\n\n'
                    res += s
            if res == 'ok\n':
                res = 'ok\n\n'
        else:
            cpu = cpus.get(other, '')
            if not other in cpus:
                res = 'ok\n\n'
            else:
                for e in cpus[other]:
                    s = '{} {} {}'.format(other, e[1], e[0])
                    s += '\n\n'
                    res += s 
    elif cmd == "put":

        def append_list(e, l):
            res = []
            l0 = [e[0] for e in l]
            e0 = e[0]
            if not e0 in l0:
                l.append(e)
                l.sort(key = lambda e: e[0])
                res = l
            else:
                i = l0.index(e0)
                l[i] = e
                res = l
            return res

        strs = other.split(' ')
        strs = [e.strip() for e in strs]
        if len(strs) == 3:
            try:
                load = float(strs[1])
                time2 = int(strs[2])
                l = cpus.get(strs[0], [])

                l = append_list((time2, load), l)

                cpus[strs[0]] = l
                res = 'ok\n\n'
            except Exception:
                res = 'error\nwrong command\n\n'
    else:
        res = 'error\nwrong command\n\n'
    return res

class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        req = data.decode()
        reqs = req.split('\n')
        resp = ''
        if len(reqs) > 1:
            for e in reqs:
                e += '\n'
                if e.strip() != '':
                    resp = process_data(e)
                    print(e,' resp = ', resp)
        elif len(reqs) == 2 and reqs[-1] != '':
            resp = process_data(req)
        resp = process_data(req)
        self.transport.write(resp.encode())


if __name__ == "__main__":

    run_server("127.0.0.1", 8181)

    pass




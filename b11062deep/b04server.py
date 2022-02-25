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


    def cpus_all():
        cpu_str = ''
        for e in cpus:
            for t in cpus[e]:
                s = '{} {} {}'.format(e, t[1], t[0])
                s += '\n'
                cpu_str += s

        return cpu_str

    def cpus_key(cpu):
        cpu_str = ''
        if not cpu in cpus:
            cpu_str = ''
        else:
            for e in cpus[cpu]:
                s = '{} {} {}'.format(cpu, e[1], e[0])
                s += '\n'
                cpu_str += s 
        return cpu_str


    def get_request(data):
        req_method = 'error'
        req_payload = ''
        if ' ' in data:
            req_method, req_payload = data.split(' ', 1)

        req = (req_method, req_payload)
        # print(req)
        return req

    def get_response(payload):
        response = 'get'
        if '*\n' in payload:
            cpu_str = cpus_all()
            response = 'ok\n' + cpu_str + '\n'
        else:
            match = re.search(r'^([\w\.]+)\n', payload)
            cpu = match and match[1]
            cpu = cpu or ''
            cpu_str = cpus_key(cpu)
            if cpu != '':
                response = 'ok\n' + cpu_str + '\n'
            else:
                response = 'error\nwrong command\n\n'
        return response
        pass

    def put_response(payload):
        response = ''
        payload = payload.strip()
        rows = payload.splitlines()
        try:
            for row in rows:
                cpu, load, timestamp = row.split()

                loads = cpus.get(cpu, [])

                loads = append_list((int(timestamp), float(load)), loads)

                # loads += [(int(timestamp), float(load))]
                # loads.sort(key = lambda e: e[0])

                cpus[cpu] = loads
            response = 'ok\n\n'
        except Exception:
            response = 'error\nwrong command\n\n'
        return response
        pass

    def error_response():
        return 'error\nwrong command\n\n'

    req_method, req_payload = get_request(data)
    # print('req_method:',req_method, ', req_payload:', req_payload)
    response = ''
    if req_method == 'get' and req_payload.strip() != '':
        response = get_response(req_payload)
    elif req_method == 'put':
        response = put_response(req_payload)
    else:
        response = error_response()

    # print('response =', response)
    return response


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        req = data.decode()
        resp = process_data(req)
        self.transport.write(resp.encode())


if __name__ == "__main__":

    run_server("127.0.0.1", 8181)

    pass



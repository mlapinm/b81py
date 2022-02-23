


cpus = {
    'test_key1': [(123, 0.2), (124, 0.2), (125, 0.2)],
    'test_key2': [(123, 0.3), (124, 0.4), (125, 0.5)],
}

def process_data(data):
    res = ''    
    cmd, other = data.split(' ', 1)
    cmd = cmd.strip()
    other = other.strip()
    if cmd == "get":
        res = 'ok\n'
        if other == '*':
            for e in cpus:
                for t in cpus[e]:
                    s = '{} {} {}'.format(e, t[1], t[0])
                    s += '\n'
                    res += s
        else:
            cpu = cpus.get(other, '')
            if not other in cpus:
                res = 'ok\n\n'
            else:
                for e in cpus[other]:
                    s = '{} {} {}'.format(other, e[1], e[0])
                    s += '\n'
                    res += s 
    elif cmd == "put":
        strs = other.split(' ')
        strs = [e.strip() for e in strs]
        if len(strs) == 3:
            try:
                load = float(strs[1])
                time2 = int(strs[2])
                l = cpus.get(strs[0], [])
                l.append((time2, load))
                l.sort(key = lambda e: e[0])
                cpus[strs[0]] = l
                res = 'ok\n\n'
            except Exception:
                res = 'error\nwrong command\n\n'
    else:
        res = 'error\nwrong command\n\n'
    return res

if __name__ == "__main__":
    # 1
    # data = "get  test_key"
    # 2
    # data = 'get *'
    # 3
    # data = 'get test_key1'
    # 4
    data = 'put test_key3 a0.8 144'
    # 5
    # data = 'got test_key'

    resp = process_data(data)
    print(data)
    print(resp)
    print(cpus)



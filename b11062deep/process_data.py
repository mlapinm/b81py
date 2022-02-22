
cpus = {
    'test_key': [1, 2]
}

def process_data(data):
    res = ''    
    cmd, other = data.split(' ', 1)
    cmd = cmd.strip()
    other = other.strip()
    print(other)

    if cmd == "get":
        cpu = cpus.get(other, '')
        if cpu == '':
            res = 'ok\n\n'
        else:
            res = cpu
    
    elif cmd == "put":

        pass


    return res





if __name__ == "__main__":
    # 1
    data = "get  test_key"

    resp = process_data(data)

    print(data)
    print(resp)



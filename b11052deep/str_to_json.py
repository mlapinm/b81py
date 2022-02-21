import re

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

if __name__ == "__main__":
    s = "ok\npalm.cpu 2.0 1150864247\npalm.cpu 0.5 1150864248\n\n"
    s += "ok\npalm2.cpu 2.0 1150864247\npalm2.cpu 0.5 1150864248\n\n"

    obj = strs_to_json(s)
    print(obj)
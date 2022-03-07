def calculate(data, findall):
    matches = findall(r"([abc])([+-]?)=([+-]?)([abc])?([+-]?\d+)?")  # Если придумать хорошую регулярку, будет просто
    # print(len(matches), matches)
    k = 0
    for v1, s1, s2, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
        if s1 == '+':
          if s2 == '-':
            if data.get(v2, 0) == 0:
              data[v1] += - int(n or 0)
            else:
              data[v1] += - int(data.get(v2, 0)) + int(n or 0)
          else:
            data[v1] += int(data.get(v2, 0)) + int(n or 0)
        elif s1 == '-':
          if s2 == '-':
            if data.get(v2, 0) == 0:
              data[v1] -= - int(n or 0)
            else:
              data[v1] -= - int(data.get(v2, 0)) + int(n or 0)
          else:
            data[v1] -= int(data.get(v2, 0)) + int(n or 0)
        else:
          if s2 == '-':
            if data.get(v2, 0) == 0:
              data[v1] = - int(n or 0)
            else:
              data[v1] = - int(data.get(v2, 0)) + int(n or 0)
          else:
            data[v1] = int(data.get(v2, 0)) + int(n or 0)

        # print(matches[k])
        # print(data[v1], v1, s1, s2, v2, n, k)

        k += 1

    return data

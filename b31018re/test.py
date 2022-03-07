import re
from regexp import calculate

def calculate2(data, findall):
    matches = findall(r"([abc])([+-])?=([+-])?([abc])?([+-]?\d+)?")  # Если придумать хорошую регулярку, будет просто
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

        print(matches[k])
        print(data)
        # print(data[v1], v1, s1, s2, v2, n, k)

        k += 1

    return data


def findall(regexp):
    text = """
    a=1
    a=+1
    a=-1
    a=b
    a=b+100
    a=b-100
    
    b+=10
    b+=+10
    b+=-10
    b+=b
    b+=b+100
    b+=b-100
    
    c-=101
    c-=+101
    c-=-101
    c-=b
    c-=b+101
    c-=b-101
    """

    text2= """
    x=y+100ecbdfax=y-100adcefby+=10cfdabex-=-101abdecfx-=101febdac
    """


    return re.findall(regexp, text)


result = calculate({'a': 1, 'b': 2, 'c': 3}, findall)
correct = {"a": -98, "b": 196, "c": -686}
if result == correct:
    print ("Correct")
else:
    print ("Incorrect: %s != %s" % (result, correct))

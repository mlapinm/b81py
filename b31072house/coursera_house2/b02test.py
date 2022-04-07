# b02test.py

from unicodedata import numeric


a = [(1, 'on'), (3, 4)]
b = [(1, 'on'), (3, 5)]

for i,e in enumerate(a):
  if e != b[i]:
    print(i, e)
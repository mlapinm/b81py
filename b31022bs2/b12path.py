# b12path.py


refs = [*range(7)]
refs[0] = [49, [50]]
refs[1] = [50, [51]]
refs[2] = [51, [52, 55]]
refs[3] = [52, [53, 54]]
refs[4] = [53, [49]]
refs[5] = [54, [50]]
refs[6] = [55, [52]]

def get_n(v):
  n = 0
  for e in refs:
    if v in e[1]:
      n += 1
  return n

def get_times():
  dtimes = {}
  for e in refs:
    n = get_n(e[0])
    dtimes[e[0]] = n
  return dtimes

def get_parents(v):
  parents = []
  for e in refs:
    if v in e[1]:
      parents += [e[0]]
  return [v, parents]

def get_path(v1, v):
  end = False
  all_parents = []
  parents = get_parents(v)
  all_parents += [get_parents(v)]
  l0 = [v]
  l0 += parents[1]
  k = 0
  n = 1
  l = 0
  p = all_parents[0]
  while k < 3000:
    if l < len(p[1]):
      pp = get_parents(p[1][l])
      for e in pp[1]:
        l2 = []
        if not e in l0:
          l0 += [e]
          l2 += [e]
          if e == v1:
            end = True
      ppp = [pp[0], l2]
      if len(l2):
        all_parents += [ppp]
      if end:
        break
      l += 1
    else:
      if n < len(all_parents):
        p = all_parents[n]
        n += 1
        l = 0
      else:
        break
    k += 1
  return all_parents

res = get_path(50, 55)
print(res)
for e in refs:
  res = get_path(None, e[0])
  # print(res)
  
def get_for_parents():
  parents = []
  for e in refs:
    parents += [get_parents(e[0])]
  return parents

dtimes = get_times()
# print(dtimes)

parents = get_for_parents()
# print('parents =', parents)

def get_path(v1, v2):
  print(v1, v2)

res = get_path(50, 55)  
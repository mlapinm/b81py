import requests
import datetime

def get_json():
  path_ = 'b81py/b31016friends/'
  text = ''
  with open(path_ + 'res.json') as f:
    text = f.read()
  djson = eval(text)
  return djson

def get_age(d1_string):
  try:
    d1 = datetime.datetime.strptime(d1_string, '%d.%m.%Y')
  except Exception:
    return -1
  d2 = datetime.datetime.today()
  age = d2.year - d1.year
  if (d2.month, d2.day) > (d1.month, d1.day):
    # age += 1
    pass
  age = age if age < 80 else -1  
  return age


def calc_age(uid):
    url = 'https://api.vk.com/method/friends.get?v=5.81&access_token=17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711&user_id={}&fields=bdate'.format(uid)  

    djson = get_json()  
    # res = requests.get(url)
    # djson = res.json()

    ages = []
    for e in djson['response']['items']:
      if 'bdate' in e:
        age = get_age(e['bdate'])
        if age != -1:
          ages += [age]

    dage = {}
    for e in ages:
      dage[e] = dage.get(e, 0) + 1
      
    tages = [*dage.items()]
    tages.sort(key=lambda e: e[0])
    tages.sort(key=lambda e: e[1], reverse=True)
    return tages

if __name__ == '__main__':

  uid = 6489613
  res = calc_age(uid)
  print(res)




from urllib import request


def calc_age(uid):
    print('uid =',uid)

    res = requests('https://google.com')
    print(res)

    return [(26, 8), (21, 6)]


if __name__ == '__main__':
  url = 'https://api.vk.com/method/friends.get?v=5.81&access_token=17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711&user_id=6489613&fields=bdate'
  res = calc_age('reigning')
  print(res)

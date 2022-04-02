from bs4 import BeautifulSoup
import re
import os

text = ''
FILE = 'Blacklist.html'
PATH = 'b81py/b31022bs/'

def get_soup(file):
  with open(file, encoding='utf-8') as f:
    text = f.read()
  # print(text)
  soup = BeautifulSoup(text, 'lxml')
  # soup = BeautifulSoup(soup.prettify(), 'lxml')
  return soup

def get_imgs(soup):
  imgs = soup('img')
  imgs = [e for e in imgs if int(e.get('width', 0)) >= 200]
  len_imgs = len(imgs)
  # print(len_imgs, imgs)
  # print(len_imgs)
  return len_imgs

def get_headers(soup):
  hh = soup('h1') + soup('h2') + soup('h3') + soup('h4') + soup('h5') + soup('h6')

  k=0
  hhs = ['h' + str(e) for e in range(1, 7)]
  # print(hhs)
  hs = []
  for e in hhs:
    for e2 in soup(e):
      s2 = e2.text
      if s2:
        match = re.search(r'^[ETC]', s2.strip())
        if match:
          hs += [s2]
        #   print(k, e2)
        #   print(k, s2)
          k += 1
      pass
  # print(hs)
  # print(len(hs))
  return len(hs)

from bs4 import BeautifulSoup

def get_linkslen(soup):
  aa = soup.find_all('a')
  kk = []
  k = 1
  for e in aa:
      a = e.find_next_sibling()
      if a and a.name == 'a':
          k +=1
      else:
          kk += [k]
          k = 1
  return max(kk)

def get_lists(soup):
  ll = soup('ul')
  ll += soup('ol')

  k = 0
  ll2 = []
  for e in ll:
    parents = [tag.name for tag in e.parents]
    if (not 'ul' in parents) and (not 'ol' in parents):
      ll2 += [e]
      # print(e.name, e.text[:10].strip())
  # print('k', k, len(ll2))
  k = len(ll) - k
  # print(k)
  return len(ll2)


def parse(path_to_file):
    soup = get_soup(path_to_file)
    soup = soup.find(id='bodyContent')
    imgs = get_imgs(soup)    
    headers = get_headers(soup)    
    linkslen = get_linkslen(soup)    
    lists = get_lists(soup)    

    return [imgs, headers, linkslen, lists] 




if __name__ == '__main__':
    path_ = 'b81py/b31022bs/'
    file1 = 'Stone_Age'
    file2 = 'Brain'
    file3 = 'Artificial_intelligence'

    res = parse("wiki/Brain")

# [19, 5, 25, 11] +
# [19, 5, 24, 11]

    # res = parse(path_ + 'wiki/' + file1)
    print(res)

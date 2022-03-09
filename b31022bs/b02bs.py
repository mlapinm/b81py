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
  imgs = [e for e in imgs if int(e['width']) >= 200]
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
          # print(e2)
          # print(s2)
      pass
  # print(hs)
  # print(len(hs))
  return len(hs)

def get_linkslen(soup):
  aa = soup('a')
  kk = []
  for e in aa:
    k = 0
    n = 0
    while e.find_next_sibling('a'):
      k += 1
      kk += [k]
      e = e.find_next_sibling('a')

  # print(kk)
  # print(max(kk))
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
    imgs = get_imgs(soup)    
    headers = get_headers(soup)    
    linkslen = get_linkslen(soup)    
    lists = get_lists(soup)    

    return [imgs, headers, linkslen, lists] 

def get_links(path, page):
  with open(os.path.join(path, page), encoding="utf-8") as file:
    links1 = re.findall(r"(?<=/wiki/)[\w()]+", file.read())
  set1 = set(links1)
  links = [*set1]
  files = os.listdir(path)
  links1 = []
  for e in links:
    if e in files:
      links1 += [e]
      # print(e)
  return links1

def get_parents(path, page):
  print(path+page)
  files = os.listdir(path)
  files = [e for e in files if e != page]
  parents = []
  for e in files:
    l1 = get_links(path, e)
    if page in l1:
      parents += [e]

  # print(len(files), page, parents)
  return parents


def build_bridge(path, page1, page2):
  links1 = get_links(path + 'wiki/', page1)
  # print(links1)
  parents = get_parents(path + 'wiki/', page2)
  print(len(parents), page1, page2, parents)




if __name__ == '__main__':
    path_ = 'b81py/b31022bs/'
    file1 = 'Stone_Age'
    file2 = 'Brain'
    
    res = parse(path_ + 'wiki/' + file1)
    # print(res)

    res = build_bridge(path_, file1, file2)
    # print(res)

    # ('wiki/Stone_Age', [13, 10, 12, 40]),
    # ('wiki/Brain', [19, 5, 25, 11]),
    # ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
    # ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
    # ('wiki/Spectrogram', [1, 2, 4, 7]),)

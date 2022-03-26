from decimal import Decimal
import requests
from bs4 import BeautifulSoup
from decimal import *

def save(text, name='b12curr.txt'):
  with open(name, "wb") as f:
    f.write(text)

def save2(text, name='b12curr.txt'):
  with open(name, "w") as f:
    f.write(text)

def load():
  with open('b12curr.txt', 'rb') as f:
    return f.read()

def nom(soup, char_code):    
  chcode = soup.find('CharCode', text=char_code)
  nom_value = chcode.find_next_sibling('Value').string
  nom_value = Decimal(nom_value.replace(',','.'))
  nominal = chcode.find_next_sibling('Nominal').string
  nominal = Decimal(nominal)
  value = nom_value/nominal
  return value


def get_currency():
  url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req=17/02/2005"
  resp = requests.get(url)
  # print(resp.content)
  save(resp.content)
  text = load()
  print(text)
  # soup = BeautifulSoup(resp.text, 'xml')
  soup = BeautifulSoup(text, 'xml')
  print(333, len(soup.prettify()), soup.prettify()[-200:])
  save2(soup.prettify(), 'b14soup.txt')
  chcodes = ['EUR', 'USD', 'AMD']
  nom_fr = nom(soup, chcodes[0])
  nom_to = nom(soup, chcodes[1])
  val = nom_fr/nom_to
  print(nom_fr, nom_to, val)



  # value = Decimal(nom_value/nominal).quantize(Decimal('.0001'), rounding=ROUND_DOWN)

if __name__ == "__main__":
  get_currency()
  pass
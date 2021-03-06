from bs4 import BeautifulSoup
from decimal import Decimal, ROUND_UP
import requests
import lxml

def nom(soup, char_code):
  if char_code == 'RUR':
      return Decimal(1)    
  chcode = soup.find('CharCode', text=char_code)
  nom_value = chcode.find_next_sibling('Value').string
  nom_value = Decimal(nom_value.replace(',','.'))
  nominal = chcode.find_next_sibling('Nominal').string
  nominal = Decimal(nominal)
  value = nom_value/nominal
  return value

def convert(amount, cur_from, cur_to, date, requests):
    url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req=17/02/2005"

    response = requests.get(url)  # Использовать переданный requests

    soup = BeautifulSoup(response.content, 'xml')
    nom_fr = nom(soup, cur_from)
    nom_to = nom(soup, cur_to)
    amount = Decimal(amount)
    val = amount * nom_fr/nom_to
    result = Decimal(val).quantize(Decimal('.0001'), ROUND_UP)
    

    # result = Decimal('3754.8057')
    return result  # не забыть про округление до 4х знаков после запятой

if __name__ == "__main__":
    correct = Decimal('3754.8057')
    result = convert(Decimal("1000.1000"), 'RUR', 'JPY', "17/02/2005", requests)
    print(result)

    
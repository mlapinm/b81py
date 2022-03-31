#b12bot.py 
import re

import telebot
token = '5208277121:AAFDcV3sKkK7ccuwq4efwWiKS20IzKWMVXw'

bot = telebot.TeleBot(token)
items = []

def get_closest_bank(location):
  lat = location.latitude
  lon = location.longitude
  print(lat, lon)
  bank_address = 'Красноармейская, 20'
  bank_lat, bank_lon = 55.800389, 37.543710
  return bank_address, bank_lat, bank_lon


@bot.message_handler(content_types=['location'])
def handle_location(message):
  location = message.location
  bank_address, bank_lat, bank_lon = get_closest_bank(location)
  logo = open('bank.png', 'rb')
  bot.send_photo(message.chat.id, logo, caption='Ближайший банк находится по адресу, {}'.format(bank_address))
  bot.send_location(message.chat.id, bank_lat, bank_lon)

bot.polling()



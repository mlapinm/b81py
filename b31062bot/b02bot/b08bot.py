#b08bot.py 
import re

import telebot
token = '5162619904:AAFH6YahnWvGSzxzteRT0Tz9VJJaF8vEdMk'

bot = telebot.TeleBot(token)
items = []



@bot.message_handler(commands=['start'])
def handle_message(message):
    print(message.text)
    text = '/start, /add <message>, /list, /reset'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['add'])
def handle_message(message):
    global items
    text = message.text
    match = re.search(r'/add (.*)$', text)
    item = ' '
    if match:
        item = match[1]
        items += [item] 
        print(item)

@bot.message_handler(commands=['list'])
def handle_message(message):
    global items
    print(333)
    print(bot.get_me().username)
    for e in items[-10:]:
        bot.send_message(message.chat.id, e)
        print(e)

@bot.message_handler(commands=['reset'])
def handle_message(message):
    global items
    for e in items:
        bot.send_message(message.chat.id, e)
        print(e)
    items = []

bot.polling()



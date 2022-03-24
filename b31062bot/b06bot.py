#b06bot.py 


import telebot
token = '5162619904:AAFH6YahnWvGSzxzteRT0Tz9VJJaF8vEdMk'

bot = telebot.TeleBot(token)

@bot.message_handler()
def handle_message(message):
    print(message.text)

bot.polling()

print(333)

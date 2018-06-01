import telebot
import constants
import requests
import io

bot = telebot.TeleBot(constants.token)

@bot.message_handler(commands=['ping'])
def handele_text(message):
    bot.send_message(message.chat.id, "I'm stil here, don't warry!")

@bot.message_handler(commands=['pic'])
def handele_text(message):
    bot.send_message(message.chat.id, "Sending cute picture...")
    response = requests.get(constants.url)
    picture = io.BytesIO(response.content)
    picture.seek(0);
    bot.send_photo(message.chat.id, photo=picture, caption='Your new picture')

@bot.message_handler(content_types=['text'])
def handele_text(message):
    bot.send_message(message.chat.id, "Hello")

bot.polling(none_stop=True, interval=0)
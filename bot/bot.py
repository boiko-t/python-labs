import telebot
import constants
import picture_loader
import dbworker

bot = telebot.TeleBot(constants.token)
picture_topic = ''

@bot.message_handler(commands=['start'])
def handele_start_command(message):
    dbworker.set_state(message.chat.id, constants.States.UNDEFINED)        
    bot.send_message(message.chat.id, constants.text_messages['start'])

@bot.message_handler(commands=['ping'])
def handele_ping_command(message):
    bot.send_message(message.chat.id, constants.text_messages['ping'])

@bot.message_handler(commands=['random'])
def handele_random_command(message):
    bot.send_message(message.chat.id, constants.text_messages['send_picture'])
    picture = picture_loader.get_random_picture()
    send_picture(message.chat.id, picture)

@bot.message_handler(commands=['picture'])
def handele_picture_command(message):
    bot.send_message(message.chat.id, constants.text_messages['enter_picture_topic'])
    dbworker.set_state(message.chat.id, constants.States.ENTER_PICTURE_TOPIC)

@bot.message_handler(content_types=['text'])
def handele_text(message):
    conversation_state = dbworker.get_current_state(message.chat.id)
    if conversation_state == constants.States.ENTER_PICTURE_TOPIC:
        dbworker.set_state(message.chat.id, constants.States.SENT_PICTURE_TOPIC)
        send_picture_by_topic(message.chat.id, message.text)
    else:
        bot.reply_to(message, constants.text_messages['plain_text'])

def send_picture_by_topic(chat_id, topic):
    bot.send_message(chat_id, constants.text_messages['send_picture_on_topic'] + topic + '...')
    picture = picture_loader.get_picture_from_collection(topic)
    send_picture(chat_id, picture)
    dbworker.set_state(chat_id, constants.States.UNDEFINED)    

def send_picture(chat_id, picture):
    bot.send_photo(chat_id, photo=picture, caption=constants.text_messages['picture_caption'])    

bot.polling(none_stop=True, interval=0)
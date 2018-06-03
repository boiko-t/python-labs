# -*- coding: utf-8 -*-
from enum import Enum

token = "450009427:AAGn13bqoPpjo4w-W-bzGqMPVBP26CM0XBg"
url_random = "https://source.unsplash.com/random"
url_collection = "https://source.unsplash.com/1600x900/?"

db_file = "database.vdb"
class States(Enum):
    UNDEFINED = "0"
    ENTER_PICTURE_TOPIC = "1"
    SENT_PICTURE_TOPIC = "2"

text_messages = {
    "start": "Hi there! I can find some pictures for you 😊",
    "ping": "I'm stil here, don't worry!",
    "send_picture": "Sending cute picture...",
    "send_picture_on_topic": "Sending cute picture of ",
    "enter_picture_topic": "Please tell me which picture should I look for",
    "picture_caption": "Your new picture",
    "plain_text": "Hello, my friend.\nI'd love to chat with you, but I'm not intelligent enough for that 😢\nPlease select command"
}
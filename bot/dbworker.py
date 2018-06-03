# -*- coding: utf-8 -*-
from vedis import Vedis
import constants

def get_current_state(chat_id):
    with Vedis(constants.db_file) as db:
        try:
            return db[chat_id]
        except KeyError:      
            return constants.States.UNDEFINED


def set_state(chat_id, value):
    with Vedis(constants.db_file) as db:
        try:
            db[chat_id] = value
            return True
        except:
            return False
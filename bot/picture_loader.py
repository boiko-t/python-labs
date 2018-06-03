import constants
import requests
import io

def get_random_picture():
    response = requests.get(constants.url_random)
    picture = io.BytesIO(response.content)
    picture.seek(0)
    return picture

def get_picture_from_collection(collection):
    response = requests.get(constants.url_collection + collection)
    picture = io.BytesIO(response.content)
    picture.seek(0)
    return picture
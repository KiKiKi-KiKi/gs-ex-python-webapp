from urllib.request import urlopen
from random import shuffle
from flask import Blueprint, jsonify
from bs4 import BeautifulSoup
from http_exception import bad_request
from scraping import get_web_data

api = Blueprint('api', __name__)

scraping_data = None


def get_data():
    global scraping_data

    if scraping_data != None:
        return scraping_data
    else:
        scraping_data = get_web_data()
        return scraping_data


@api.route('/api/get_random', methods=['GET'])
def get_one():
    data = get_data()
    shuffle(data)
    return jsonify({
        'status': 'ok',
        'data': data[0]
    })

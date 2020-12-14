from urllib.request import urlopen
from random import shuffle
from flask import Blueprint, jsonify
from bs4 import BeautifulSoup
from http_exception import bad_request
from scraping import get_web_data

api = Blueprint('api', __name__)


@api.route('/api/get_random', methods=['GET'])
def get_one():
    data = get_web_data()
    shuffle(data)
    return jsonify({
        'status': 'ok',
        'data': data[0]
    })

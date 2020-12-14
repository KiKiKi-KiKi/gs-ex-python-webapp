from random import shuffle
from flask import Blueprint, jsonify, request
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


@api.route('/api/random', methods=['GET'])
def get_one():
    data = get_data()
    shuffle(data)
    return jsonify({
        'status': 'ok',
        'data': data[0]
    })


@api.route('/api/stories/<int:story_no>', methods=['GET'])
def get_one_by_index(story_no):
    no = int(story_no)

    if not no:
        return bad_request('NO DATA!')

    res = None
    data = get_data()
    max = len(data)

    if no > max:
        return jsonify({
            'status': 'ok',
            'data': res
        })

    for story in data:
        if story[0] == no:
            res = story
            break

    return jsonify({
        'status': 'ok',
        'data': res
    })


@api.route('/api/search', methods=['GET', 'POST'])
def api_search():
    keyword = request.args.get('keyword')

    if not keyword:
        return bad_request('NO DATA!')

    res = []
    data = get_data()

    for story in data:
        story_str = " ".join(map(str, story))
        # keyword が含まれているかチェック
        match = keyword in story_str
        if match:
            res.append(story)

    return jsonify({
        'status': 'ok',
        'data': res
    })

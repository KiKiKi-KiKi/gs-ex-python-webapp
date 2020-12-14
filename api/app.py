import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, jsonify
from logger import info_handler, error_handler
from api import api as api_controller

# load .env
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

# 日本語文字化け対策
app.config['JSON_AS_ASCII'] = False
# ソートをそのままにする
app.config['JSON_SORT_KEYS'] = False

# set log
app.logger.addHandler(info_handler)
app.logger.addHandler(error_handler)


# Controller
app.register_blueprint(api_controller)


@app.route('/')
def index():
    return 'Hello Flask!'

# App start


def main():
    """main
    """
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', '5000'))
    mode = os.environ.get('MODE', None)
    debug = mode == 'development'
    print('Mode >', mode, 'DEBUG:', debug)
    app.run(debug=debug, host=host, port=port)


if __name__ == '__main__':
    main()

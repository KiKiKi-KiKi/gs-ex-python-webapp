import os
from flask import Flask, jsonify
from logger import info_handler, error_handler
from api import api as api_controller

app = Flask(__name__)

# 日本語文字化け大作
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
    app.run(host=host, port=port)


if __name__ == '__main__':
    main()

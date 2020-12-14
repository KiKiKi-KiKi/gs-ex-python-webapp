import os
from flask import Flask
from logger import info_handler, error_handler

app = Flask(__name__)

# set log
app.logger.addHandler(info_handler)
app.logger.addHandler(error_handler)


@app.route('/')
def index():
    return 'Hello Flask!'


def main():
    """main
    """
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', '5000'))
    app.run(host=host, port=port)


if __name__ == '__main__':
    main()

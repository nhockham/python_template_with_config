"""Simple flask app with logging, testing and containerisation."""

from flask import Flask
import logging
from modules import calc


logger = logging.getLogger('app')


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! ' + str(calc.my_function(5, 6))


if __name__ == '__main__':
    logger.info('starting up')
    app.run(host='0.0.0.0', debug=True)

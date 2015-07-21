"""A simple function to test unittest"""

import logging


logger = logging.getLogger('app')


def my_function(arg1, arg2):
    logger.info('adding inputs')
    return arg1 + arg2

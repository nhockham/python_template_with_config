"""Tests for calc.py"""

import unittest
import logging
from modules import calc


logger = logging.getLogger('testing')


class CalcTest(unittest.TestCase):

    def test1(self):
        logger.info('performing calc unittest')
        result = calc.my_function(2, 3)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()

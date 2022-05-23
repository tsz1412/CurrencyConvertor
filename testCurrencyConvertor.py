import unittest
from CurrencyConvertor import *


class TestCurrencyConvertorCase(unittest.TestCase):
    def test_special_cases_1(self):
        self.assertEqual(CurrencyConvertor('$153', 'CAD').get_converted_currency(), '195.640335')


if __name__ == '__main__':
    unittest.main()

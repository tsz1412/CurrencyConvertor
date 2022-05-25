from constants import *
import requests
import helpers
import json
import math


class CurrencyConvertor:
    def __init__(self, amount: str, target: str):
        self.__amount = amount[1:]
        self.__currency = helpers.get_key(amount[0], ALLOWED_CURRENCIES)
        self.__target = target
        self.__response = ""
        self.__convert()
        self.__converted = ""
        self.__roundup()

    def __str__(self):
        return self.__amount + ' ' + self.__currency + ' --> ' + self.__converted + ' ' + self.__target

    def __roundup(self):
        s_num = math.modf(float(self.__response['result']))
        pre_decimal_length = len(str(int(s_num[1])))
        if pre_decimal_length < 3:
            self.__converted = str(math.ceil(float(self.__response['result']))-0.01)
        elif pre_decimal_length == 4:
            self.__converted = str(math.ceil(float(self.__response['result']) / 10) * 10)
        else:
            self.__converted = str(math.ceil(float(self.__response['result']) / 100) * 100)

    def __convert(self):
        """
        Call the Convertion Rate API
        :return:
        """
        url = BASE_URL + CONVERTION_ENDPOINT + "?to="+self.__target+"&from="+self.__currency+"&amount="+self.__amount

        headers = {
            'apikey': APIKEY
        }

        response = requests.request("GET", url, headers=headers)

        self.__response = json.loads(response.text)


if __name__ == '__main__':
    currency = CurrencyConvertor('$11527.49', 'ILS')
    print(currency)

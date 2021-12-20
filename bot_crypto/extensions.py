import json
import requests
from config import exchanger


class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(values):
        if len(values) != 3:
            raise APIException('Введите ровно 3 параметра - правила ввода по команде /help')
        quote, base, amount = values

        if quote == base:
            raise APIException('Валюты должны отличаться!')

        try:
            quote_1 = exchanger[quote]
        except KeyError:
            raise APIException('Не удалось обработать валюту')

        try:
            base_1 = exchanger[base]
        except KeyError:
            raise APIException('Не удалось обработать валюту')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException('Не удалось обработать количество')

        R = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_1}&tsyms={base_1}')
        num = float(json.loads(R.content)[base_1]) * amount

        return round(num, 3)

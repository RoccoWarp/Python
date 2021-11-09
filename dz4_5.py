from requests import get
from decimal import Decimal


def main(argv):
    program, code = argv
    response = get('https://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding).split('<CharCode>')
    for el in content:
        if code.upper() in el:
            currency_price = el.split('<Value>')
            currency_price = currency_price[1].replace(',', '.').split('</')
            currency_price = Decimal(currency_price[0])
            currency_price = currency_price.quantize(Decimal('1.00'))
            print(f'{currency_price} RUB')
            return 0


# print(currency_rates('eur'))
if __name__ == '__main__':
    import sys

    exit(main(sys.argv))

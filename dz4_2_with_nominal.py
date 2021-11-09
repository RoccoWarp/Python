from requests import get
from decimal import Decimal


def currency_rates(code):
    response = get('https://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding).split('<CharCode>')
    for el in content:
        if code.upper() in el:
            currency_price = el.split('<Value>')
            currency_price = currency_price[1].replace(',', '.').split('</')
            currency_price = Decimal(currency_price[0])
            currency_price = currency_price.quantize(Decimal('1.00'))
    for el in content:
        if code.upper() in el:
            currency_nom = el.split('<Nominal>')[1]
            currency_nom = currency_nom.split('</')
    return f'{currency_nom[0]} {code} {currency_price} RUB '


print(currency_rates('eur'))

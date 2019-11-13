from currencies.connections import RatesConnection
from currencies.models import Currency


def generate_exchange_rates():
    exchange_rates = []
    conn = RatesConnection()
    base, rates = conn.get_rates()
    currencies = list(Currency.objects.select_related().only().all())
    for source in currencies:
        for target in currencies:
            if source != target:
                rate = calculate_rate(base, rates, source, target)
                exchange_rates.append(rate)
    return exchange_rates


def calculate_rate(base, rates, source, target):
    if source.code != target.code:
        result = {'source': source, 'target': target, 'rate': None}
        if source.code == base:
            result['rate'] = rates.get(target.code)
            return result
        elif target.code == base:
            result['rate'] = 1.0 / rates.get(source.code)
            return result
        else:
            result['rate'] = rates.get(target.code) / rates.get(source.code)
            return result

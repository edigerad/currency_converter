import requests

import environ

env = environ.Env()


class RatesConnection(object):
    """
        Used to retrieve data from external currency api service
    """
    url = env('CURRENCY_API_URL', default='https://openexchangerates.org/api/latest.json')

    def get_rates(self):
        app_id = env('CURRENCY_API_KEY', default='ddf5e90057d14fb6b12d22d4a30cc1e3')
        url = f'{self.url}?app_id={app_id}'
        response = {'error': True}
        while response.get('error'):
            response = requests.get(url=url).json()
        return response.get('base'), response.get('rates')
